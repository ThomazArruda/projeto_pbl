import React, { useState, useEffect } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import { Activity, PlayCircle, ArrowLeft, History } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

function PatientDetails() {
    const { id } = useParams();
    const location = useLocation();
    const navigate = useNavigate();
    const patient = location.state?.patient || { name: "Paciente", id: id };
    const [history, setHistory] = useState([]);

    useEffect(() => {
        fetchHistory();
    }, []);

    const fetchHistory = async () => {
        try {
            const res = await fetch(`http://localhost:8000/patients/${id}/history`);
            const data = await res.json();
            // Format data for chart
            const formattedData = data.map(session => ({
                date: new Date(session.timestamp).toLocaleDateString(),
                fullDate: new Date(session.timestamp).toLocaleString(),
                max_angle_esq: session.max_angle_esq,
                max_angle_dir: session.max_angle_dir,
                avg_emg_esq: session.avg_emg_esq,
                avg_emg_dir: session.avg_emg_dir
            }));
            setHistory(formattedData);
        } catch (err) {
            console.error("Error fetching history:", err);
        }
    };

    const handleStartSession = () => {
        navigate(`/dashboard/${id}`, { state: { patient } });
    };

    return (
        <div className="min-h-screen bg-background text-white p-8 font-sans flex flex-col items-center">
            <div className="w-full max-w-4xl">
                <header className="flex items-center gap-3 mb-8">
                    <button onClick={() => navigate('/')} className="hover:bg-surface p-2 rounded-full transition">
                        <ArrowLeft className="text-slate-400" />
                    </button>
                    <Activity className="text-primary w-8 h-8" />
                    <h1 className="text-2xl font-bold tracking-tight">Neuro<span className="text-primary">Passo</span></h1>
                </header>

                <div className="bg-surface p-8 rounded-2xl shadow-lg border border-slate-700/50 mb-8">
                    <div className="flex items-center gap-6 mb-8">
                        <div className="w-24 h-24 bg-slate-700 rounded-full flex items-center justify-center text-4xl">👤</div>
                        <div>
                            <h2 className="text-3xl font-bold">{patient.name}</h2>
                            <p className="text-slate-400 text-lg">ID: #{patient.id}</p>
                        </div>
                        <div className="ml-auto">
                            <button
                                onClick={handleStartSession}
                                className="flex items-center gap-3 bg-primary hover:bg-blue-600 text-white px-8 py-4 rounded-xl font-bold text-lg transition shadow-lg shadow-primary/20 active:scale-95">
                                <PlayCircle size={24} /> Iniciar Nova Sessão
                            </button>
                        </div>
                    </div>

                    <div className="border-t border-slate-700 pt-6">
                        <h3 className="text-xl font-semibold mb-6 flex items-center gap-2 text-slate-300">
                            <History /> Histórico de Evolução
                        </h3>

                        {/* Angle Chart */}
                        <div className="h-80 bg-background/50 rounded-xl border border-slate-700/50 p-4 mb-8">
                            <h4 className="text-lg font-medium mb-4 text-slate-400 text-center">Amplitude de Movimento (Máx)</h4>
                            {history.length > 0 ? (
                                <ResponsiveContainer width="100%" height="100%">
                                    <LineChart data={history}>
                                        <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                                        <XAxis dataKey="date" stroke="#94a3b8" />
                                        <YAxis domain={[0, 180]} stroke="#94a3b8" label={{ value: 'Ângulo (°)', angle: -90, position: 'insideLeft', fill: '#94a3b8' }} />
                                        <Tooltip
                                            contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155' }}
                                            labelStyle={{ color: '#e2e8f0' }}
                                        />
                                        <Legend verticalAlign="top" height={36} />
                                        <Line name="Perna Esquerda (Parética)" type="monotone" dataKey="max_angle_esq" stroke="#ef4444" strokeWidth={3} strokeDasharray="5 5" dot={{ r: 4 }} activeDot={{ r: 6 }} />
                                        <Line name="Perna Direita (Controle)" type="monotone" dataKey="max_angle_dir" stroke="#22c55e" strokeWidth={3} dot={{ r: 4 }} activeDot={{ r: 6 }} />
                                    </LineChart>
                                </ResponsiveContainer>
                            ) : (
                                <div className="h-full flex items-center justify-center text-slate-500">
                                    Nenhuma sessão registrada.
                                </div>
                            )}
                        </div>

                        {/* Activation Chart */}
                        <div className="h-80 bg-background/50 rounded-xl border border-slate-700/50 p-4">
                            <h4 className="text-lg font-medium mb-4 text-slate-400 text-center">Ativação Muscular Média (EMG + ECG)</h4>
                            {history.length > 0 ? (
                                <ResponsiveContainer width="100%" height="100%">
                                    <LineChart data={history}>
                                        <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                                        <XAxis dataKey="date" stroke="#94a3b8" />
                                        <YAxis domain={[0, 4095]} stroke="#94a3b8" label={{ value: 'Ativação (0-4095)', angle: -90, position: 'insideLeft', fill: '#94a3b8' }} />
                                        <Tooltip
                                            contentStyle={{ backgroundColor: '#1e293b', borderColor: '#334155' }}
                                            labelStyle={{ color: '#e2e8f0' }}
                                        />
                                        <Legend verticalAlign="top" height={36} />
                                        <Line name="Perna Esquerda (Parética)" type="monotone" dataKey="avg_emg_esq" stroke="#ef4444" strokeWidth={3} strokeDasharray="5 5" dot={{ r: 4 }} activeDot={{ r: 6 }} />
                                        <Line name="Perna Direita (Controle)" type="monotone" dataKey="avg_emg_dir" stroke="#22c55e" strokeWidth={3} dot={{ r: 4 }} activeDot={{ r: 6 }} />
                                    </LineChart>
                                </ResponsiveContainer>
                            ) : (
                                <div className="h-full flex items-center justify-center text-slate-500">
                                    Nenhuma sessão registrada.
                                </div>
                            )}
                        </div>

                    </div>
                </div>
            </div>
        </div>
    );
}

export default PatientDetails;
