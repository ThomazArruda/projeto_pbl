import React, { useState, useEffect, useRef } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Activity, Wifi, WifiOff, User, Save, RotateCcw, StopCircle, ArrowLeft } from 'lucide-react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';

const MAX_DATA_POINTS = 100;

function Dashboard() {
    const { id } = useParams();
    const location = useLocation();
    const navigate = useNavigate();
    const patient = location.state?.patient || { name: "Paciente", id: id };

    const [connected, setConnected] = useState(false);
    const [data, setData] = useState([]);
    const [currentValues, setCurrentValues] = useState({
        ESQ: { angle: 0, emg: 0, ecg: 0 },
        DIR: { angle: 0, emg: 0, ecg: 0 }
    });
    const [isSessionActive, setIsSessionActive] = useState(true);
    const [showSaveOptions, setShowSaveOptions] = useState(false);

    const ws = useRef(null);
    const sessionDataRef = useRef([]);

    useEffect(() => {
        connectWebSocket();
        return () => {
            if (ws.current) ws.current.close();
        };
    }, []);

    const connectWebSocket = () => {
        ws.current = new WebSocket('ws://localhost:8000/ws');

        ws.current.onopen = () => {
            setConnected(true);
            console.log('Connected to WebSocket');
        };

        ws.current.onclose = () => {
            setConnected(false);
            console.log('Disconnected');
            setTimeout(connectWebSocket, 3000); // Reconnect
        };

        ws.current.onmessage = (event) => {
            if (!isSessionActive) return; // Don't update if stopped

            const message = JSON.parse(event.data);
            if (message.type === 'data') {
                const { id, values, timestamp } = message;

                // Update Current Values (Instant)
                setCurrentValues(prev => ({
                    ...prev,
                    [id]: values
                }));

                const newDataPoint = {
                    time: new Date().toLocaleTimeString(),
                    [`${id}_angle`]: values.angle,
                    [`${id}_emg`]: values.emg,
                    [`${id}_ecg`]: values.ecg
                };

                // Accumulate ALL data for saving (Full History)
                // We need to merge with the last point if it has the same timestamp or just push
                // For simplicity in this high-frequency stream, we push individual updates
                // But to keep it cleaner, we might want to merge updates from different legs if they come close together.
                // For now, simple push is safer to not lose data.
                sessionDataRef.current.push(newDataPoint);

                // Update Graph Data (Windowed History for UI)
                setData(prevData => {
                    const newData = [...prevData, newDataPoint];
                    if (newData.length > MAX_DATA_POINTS) newData.shift();
                    return newData;
                });
            }
        };
    };

    const handleStop = () => {
        setIsSessionActive(false);
        setShowSaveOptions(true);
    };

    const handleRestart = () => {
        setData([]);
        sessionDataRef.current = []; // Clear full history
        setIsSessionActive(true);
        setShowSaveOptions(false);
    };

    const handleSave = async () => {
        try {
            const fullSessionData = sessionDataRef.current;

            if (fullSessionData.length === 0) {
                alert("Nenhum dado coletado para salvar.");
                return;
            }

            // Calculate simple stats for the session using FULL data
            const maxAngleEsq = Math.max(...fullSessionData.map(d => d.ESQ_angle || 0), 0);
            const maxAngleDir = Math.max(...fullSessionData.map(d => d.DIR_angle || 0), 0);

            // Calculate Average Muscle Activation (EMG + ECG combined)
            // Since ECG is used as a second EMG channel, we average them to get a "Total Activation" metric
            const avgEmgEsq = fullSessionData.reduce((acc, curr) => {
                const val = ((curr.ESQ_emg || 0) + (curr.ESQ_ecg || 0)) / 2;
                return acc + val;
            }, 0) / (fullSessionData.length || 1);

            const avgEmgDir = fullSessionData.reduce((acc, curr) => {
                const val = ((curr.DIR_emg || 0) + (curr.DIR_ecg || 0)) / 2;
                return acc + val;
            }, 0) / (fullSessionData.length || 1);

            const sessionData = {
                patient_id: patient.id,
                duration_seconds: fullSessionData.length * 0.1, // Approx, assuming 10Hz
                max_angle_esq: maxAngleEsq,
                max_angle_dir: maxAngleDir,
                avg_emg_esq: avgEmgEsq,
                avg_emg_dir: avgEmgDir,
                raw_data_blob: JSON.stringify(fullSessionData)
            };

            const res = await fetch('http://localhost:8000/sessions', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(sessionData)
            });

            if (res.ok) {
                alert("Sessão salva com sucesso!");
                navigate(`/patient/${patient.id}`, { state: { patient } });
            } else {
                alert("Erro ao salvar sessão.");
            }
        } catch (err) {
            console.error("Error saving session:", err);
            alert("Erro ao salvar sessão.");
        }
    };

    const getStatusColor = (val, max) => {
        const pct = val / max;
        if (pct > 0.8) return "text-success";
        if (pct > 0.4) return "text-warning";
        return "text-danger";
    };

    return (
        <div className="min-h-screen bg-background text-white p-6 font-sans">
            {/* Header */}
            <header className="flex justify-between items-center mb-8 border-b border-surface pb-4">
                <div className="flex items-center gap-3">
                    <button onClick={() => navigate(`/patient/${patient.id}`, { state: { patient } })} className="hover:bg-surface p-2 rounded-full transition">
                        <ArrowLeft className="text-slate-400" />
                    </button>
                    <Activity className="text-primary w-8 h-8" />
                    <h1 className="text-2xl font-bold tracking-tight">Neuro<span className="text-primary">Passo</span></h1>
                </div>
                <div className="flex items-center gap-4">
                    <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-sm font-medium ${connected ? 'bg-success/20 text-success' : 'bg-danger/20 text-danger'}`}>
                        {connected ? <Wifi size={16} /> : <WifiOff size={16} />}
                        {connected ? "Online" : "Offline"}
                    </div>
                    <button className="bg-surface hover:bg-slate-700 p-2 rounded-full transition">
                        <User size={20} />
                    </button>
                </div>
            </header>

            {/* Main Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

                {/* Sidebar / Controls */}
                <div className="lg:col-span-1 space-y-6">
                    {/* Patient Card */}
                    <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50">
                        <h2 className="text-lg font-semibold mb-4 text-slate-300">Sessão Atual</h2>
                        <div className="flex items-center gap-4 mb-6">
                            <div className="w-16 h-16 bg-slate-700 rounded-full flex items-center justify-center text-2xl">👤</div>
                            <div>
                                <h3 className="text-xl font-bold">{patient.name}</h3>
                                <p className="text-sm text-slate-400">ID: #{patient.id}</p>
                            </div>
                        </div>

                        {!showSaveOptions ? (
                            <button
                                onClick={handleStop}
                                className="w-full flex items-center justify-center gap-2 bg-danger hover:bg-red-600 text-white py-4 rounded-xl font-bold text-lg transition active:scale-95 shadow-lg shadow-danger/20">
                                <StopCircle size={24} /> Parar Sessão
                            </button>
                        ) : (
                            <div className="grid grid-cols-2 gap-3">
                                <button
                                    onClick={handleSave}
                                    className="flex items-center justify-center gap-2 bg-success hover:bg-green-600 text-white py-3 rounded-xl font-medium transition active:scale-95">
                                    <Save size={20} /> Salvar
                                </button>
                                <button
                                    onClick={handleRestart}
                                    className="flex items-center justify-center gap-2 bg-surface hover:bg-slate-700 border border-slate-600 text-white py-3 rounded-xl font-medium transition active:scale-95">
                                    <RotateCcw size={20} /> Reiniciar
                                </button>
                            </div>
                        )}
                    </div>

                    {/* Metrics / Biofeedback */}
                    <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50">
                        <h2 className="text-lg font-semibold mb-4 text-slate-300">Biofeedback (Tempo Real)</h2>

                        {/* Left Leg */}
                        <div className="mb-6">
                            <div className="flex justify-between items-center mb-2">
                                <span className="text-sm font-medium text-slate-400">Perna Esquerda (ESQ)</span>
                                <span className="text-xs bg-slate-700 px-2 py-0.5 rounded">Parética</span>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="bg-background p-3 rounded-lg text-center">
                                    <div className="text-xs text-slate-500 uppercase">Ângulo</div>
                                    <div className="text-2xl font-bold font-mono">{currentValues.ESQ.angle.toFixed(1)}°</div>
                                </div>
                                <div className="bg-background p-3 rounded-lg text-center">
                                    <div className="text-xs text-slate-500 uppercase">EMG</div>
                                    <div className={`text-2xl font-bold font-mono ${getStatusColor(currentValues.ESQ.emg, 4095)}`}>
                                        {currentValues.ESQ.emg}
                                    </div>
                                </div>
                            </div>
                        </div>

                        {/* Right Leg */}
                        <div>
                            <div className="flex justify-between items-center mb-2">
                                <span className="text-sm font-medium text-slate-400">Perna Direita (DIR)</span>
                                <span className="text-xs bg-slate-700 px-2 py-0.5 rounded">Controle</span>
                            </div>
                            <div className="grid grid-cols-2 gap-4">
                                <div className="bg-background p-3 rounded-lg text-center">
                                    <div className="text-xs text-slate-500 uppercase">Ângulo</div>
                                    <div className="text-2xl font-bold font-mono">{currentValues.DIR.angle.toFixed(1)}°</div>
                                </div>
                                <div className="bg-background p-3 rounded-lg text-center">
                                    <div className="text-xs text-slate-500 uppercase">EMG</div>
                                    <div className={`text-2xl font-bold font-mono ${getStatusColor(currentValues.DIR.emg, 4095)}`}>
                                        {currentValues.DIR.emg}
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

                {/* Charts Area */}
                <div className="lg:col-span-2 space-y-6">
                    {/* Angle Chart - Lilac */}
                    <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50 h-[250px]">
                        <h2 className="text-lg font-semibold mb-2 text-slate-300">Cinemática (Ângulo do Joelho)</h2>
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={data}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                                <XAxis dataKey="time" hide />
                                <YAxis domain={[0, 180]} stroke="#94a3b8" />
                                <Tooltip contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155' }} />
                                <Line type="monotone" dataKey="ESQ_angle" stroke="#a78bfa" strokeWidth={2} strokeDasharray="5 5" dot={false} isAnimationActive={false} />
                                <Line type="monotone" dataKey="DIR_angle" stroke="#a78bfa" strokeWidth={2} dot={false} isAnimationActive={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>

                    {/* EMG Chart - Blue */}
                    <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50 h-[250px]">
                        <h2 className="text-lg font-semibold mb-2 text-slate-300">Ativação Muscular (EMG)</h2>
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={data}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                                <XAxis dataKey="time" hide />
                                <YAxis domain={[0, 4095]} stroke="#94a3b8" />
                                <Tooltip contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155' }} />
                                <Line type="monotone" dataKey="ESQ_emg" stroke="#3b82f6" strokeWidth={2} strokeDasharray="5 5" dot={false} isAnimationActive={false} />
                                <Line type="monotone" dataKey="DIR_emg" stroke="#3b82f6" strokeWidth={2} dot={false} isAnimationActive={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>

                    {/* ECG Chart - Brown/Amber */}
                    <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50 h-[250px]">
                        <h2 className="text-lg font-semibold mb-2 text-slate-300">Eletrocardiograma (ECG)</h2>
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={data}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                                <XAxis dataKey="time" hide />
                                <YAxis domain={[0, 4095]} stroke="#94a3b8" />
                                <Tooltip contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155' }} />
                                <Line type="monotone" dataKey="ESQ_ecg" stroke="#d97706" strokeWidth={2} strokeDasharray="5 5" dot={false} isAnimationActive={false} />
                                <Line type="monotone" dataKey="DIR_ecg" stroke="#d97706" strokeWidth={2} dot={false} isAnimationActive={false} />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>
                </div>

            </div>
        </div>
    );
}

export default Dashboard;
