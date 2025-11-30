from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import models, database
import datetime
import socket
import asyncio
import time

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dependency ---
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Pydantic Models ---
class PatientCreate(BaseModel):
    name: str

class PatientResponse(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    class Config:
        orm_mode = True

class SessionCreate(BaseModel):
    patient_id: int
    duration_seconds: float
    max_angle_esq: float
    max_angle_dir: float
    avg_emg_esq: float
    avg_emg_dir: float
    raw_data_blob: str

# --- UDP Configuration ---
UDP_IP = "0.0.0.0"
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
sock.setblocking(False)

# --- State ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()

# Buffer for latest data
latest_data = {
    "ESQ": {"angle": 0, "emg": 0, "ecg": 0, "last_seen": 0},
    "DIR": {"angle": 0, "emg": 0, "ecg": 0, "last_seen": 0}
}

# --- Background UDP Listener ---
async def udp_listener():
    print(f"Listening for UDP on {UDP_PORT}...")
    loop = asyncio.get_event_loop()
    while True:
        try:
            data = await loop.sock_recv(sock, 1024)
            raw_msg = data.decode('utf-8').strip()
            parts = raw_msg.split(',')
            
            if len(parts) == 4:
                dev_id, angle, emg, ecg = parts[0], float(parts[1]), int(parts[2]), int(parts[3])
                
                # Update State
                if dev_id in latest_data:
                    latest_data[dev_id] = {
                        "angle": angle,
                        "emg": emg,
                        "ecg": ecg,
                        "last_seen": time.time()
                    }
                    
                    # Broadcast immediately
                    payload = {
                        "type": "data",
                        "id": dev_id,
                        "timestamp": time.time(),
                        "values": latest_data[dev_id]
                    }
                    await manager.broadcast(payload)
                    
        except Exception as e:
            print(f"UDP Error: {e}")
            await asyncio.sleep(0.1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(udp_listener())

# --- API Routes ---
@app.post("/patients", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = models.Patient(name=patient.name)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients", response_model=List[PatientResponse])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = db.query(models.Patient).offset(skip).limit(limit).all()
    return patients

@app.post("/sessions")
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    db_session = models.Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return {"status": "success", "id": db_session.id}

@app.get("/patients/{patient_id}/history")
def get_history(patient_id: int, db: Session = Depends(get_db)):
    sessions = db.query(models.Session).filter(models.Session.patient_id == patient_id).all()
    return sessions

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
