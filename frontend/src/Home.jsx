import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Users, Plus, Activity, ChevronRight } from 'lucide-react';

function Home() {
    const [patients, setPatients] = useState([]);
    const [newPatientName, setNewPatientName] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        fetchPatients();
    }, []);

    const fetchPatients = async () => {
        try {
            const res = await fetch('http://localhost:8000/patients');
            const data = await res.json();
            setPatients(data);
        } catch (err) {
            console.error("Error fetching patients:", err);
        }
    };

    const handleAddPatient = async (e) => {
        e.preventDefault();
        if (!newPatientName) return;
        try {
            const res = await fetch('http://localhost:8000/patients', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name: newPatientName })
            });
            if (res.ok) {
                setNewPatientName("");
                fetchPatients();
            }
        } catch (err) {
            console.error("Error adding patient:", err);
        }
    };

    return (
        <div className="min-h-screen bg-background text-white p-8 font-sans flex flex-col items-center">
            <div className="w-full max-w-2xl">
                <header className="flex items-center gap-3 mb-12">
                    <Activity className="text-primary w-10 h-10" />
                    <h1 className="text-3xl font-bold tracking-tight">Neuro<span className="text-primary">Passo</span></h1>
                </header>

                <div className="bg-surface p-6 rounded-2xl shadow-lg border border-slate-700/50 mb-8">
                    <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
                        <Plus className="text-primary" /> Novo Paciente
                    </h2>
                    <form onSubmit={handleAddPatient} className="flex gap-3">
                        <input
                            type="text"
                            placeholder="Nome do Paciente"
                            value={newPatientName}
                            onChange={(e) => setNewPatientName(e.target.value)}
                            className="flex-1 bg-background border border-slate-600 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition"
                        />
                        <button type="submit" className="bg-primary hover:bg-blue-600 text-white px-6 py-3 rounded-xl font-medium transition">
                            Cadastrar
                        </button>
                    </form>
                </div>

                <div className="space-y-4">
                    <h2 className="text-xl font-semibold mb-4 flex items-center gap-2 text-slate-300">
                        <Users size={20} /> Pacientes Cadastrados
                    </h2>
                    {patients.map(patient => (
                        <div
                            key={patient.id}
                            onClick={() => navigate(`/patient/${patient.id}`, { state: { patient } })}
                            className="bg-surface p-4 rounded-xl border border-slate-700/50 hover:border-primary cursor-pointer transition flex justify-between items-center group"
                        >
                            <div className="flex items-center gap-4">
                                <div className="w-10 h-10 bg-slate-700 rounded-full flex items-center justify-center text-lg">👤</div>
                                <div>
                                    <h3 className="font-bold text-lg">{patient.name}</h3>
                                    <p className="text-sm text-slate-400">ID: #{patient.id}</p>
                                </div>
                            </div>
                            <ChevronRight className="text-slate-500 group-hover:text-primary transition" />
                        </div>
                    ))}
                    {patients.length === 0 && (
                        <p className="text-slate-500 text-center py-8">Nenhum paciente cadastrado.</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Home;
