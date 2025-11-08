"""Utilities for persisting clinic data in a SQLite database.

This module centralises the persistence layer used by the Streamlit
dashboard.  The database stores a catalogue of patients as well as the
sessions collected for each person.  Session payloads are saved as JSON
so the existing in-memory structure can be written without additional
transformations.

The goal is to keep the API extremely small and explicit so newcomers to
the project can read the call sites in ``app.py`` and immediately grasp
how data flows between the UI and the storage layer.
"""

from __future__ import annotations

import datetime as _dt
import json
import sqlite3
from pathlib import Path
from typing import Dict, Iterable, List, Optional


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "clinic.db"


def init_db() -> None:
    """Create the database file and schema if they do not exist."""

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                collected_at TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                FOREIGN KEY(patient_id) REFERENCES patients(id)
            )
            """
        )

        conn.commit()


def seed_patients(default_names: Iterable[str]) -> None:
    """Ensure a basic list of patients is present for demos/tests."""

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT OR IGNORE INTO patients(name) VALUES (?)",
            [(name,) for name in default_names]
        )
        conn.commit()


def list_patients() -> List[Dict[str, object]]:
    """Return the registered patients ordered alphabetically."""

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, name FROM patients ORDER BY name COLLATE NOCASE"
        ).fetchall()
    return [dict(row) for row in rows]


def add_patient(name: str) -> Optional[int]:
    """Insert a new patient and return its id.

    The function returns ``None`` if the patient already exists.
    """

    cleaned = name.strip()
    if not cleaned:
        return None

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO patients(name) VALUES (?)",
                (cleaned,),
            )
        except sqlite3.IntegrityError:
            return None
        conn.commit()
        return cursor.lastrowid


def get_sessions(patient_id: int) -> List[Dict[str, object]]:
    """Return all sessions for a patient ordered from newest to oldest."""

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT id, collected_at, payload_json
            FROM sessions
            WHERE patient_id = ?
            ORDER BY collected_at DESC
            """,
            (patient_id,),
        ).fetchall()

    sessions: List[Dict[str, object]] = []
    for row in rows:
        payload = json.loads(row["payload_json"])
        sessions.append(
            {
                "id": row["id"],
                "date": row["collected_at"],
                "data": payload,
            }
        )
    return sessions


def add_session(patient_id: int, session_payload: Dict[str, List[float]]) -> None:
    """Persist a monitoring session for the given patient."""

    timestamp = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload_json = json.dumps(session_payload)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO sessions(patient_id, collected_at, payload_json)
            VALUES (?, ?, ?)
            """,
            (patient_id, timestamp, payload_json),
        )
        conn.commit()


def get_patient(patient_id: int) -> Optional[Dict[str, object]]:
    """Retrieve a single patient by id."""

    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, name FROM patients WHERE id = ?",
            (patient_id,),
        ).fetchone()

    return dict(row) if row else None
