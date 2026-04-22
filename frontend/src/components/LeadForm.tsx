import { useState } from "react";
import api from "../services/api";

export default function LeadForm({ onSuccess }: { onSuccess: () => void }) {
  const [data, setData] = useState({
    nome: "",
    whatsapp: "",
    origem: "",
    status: "frio",
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await api.post("/leads", data);
    setData({ nome: "", whatsapp: "", origem: "", status: "frio" });
    onSuccess();
  };

  return (
    <form className="glass p-4 mb-6 flex gap-2 flex-wrap" onSubmit={handleSubmit}>
      <input
        className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
        placeholder="Nome"
        value={data.nome}
        onChange={(e) => setData({ ...data, nome: e.target.value })}
        required
      />
      <input
        className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
        placeholder="+55XXXXXXXXX"
        value={data.whatsapp}
        onChange={(e) => setData({ ...data, whatsapp: e.target.value })}
        required
      />
      <input
        className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
        placeholder="Origem"
        value={data.origem}
        onChange={(e) => setData({ ...data, origem: e.target.value })}
      />
      <select
        className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white"
        value={data.status}
        onChange={(e) => setData({ ...data, status: e.target.value })}
      >
        <option value="quente">Quente</option>
        <option value="morno">Morno</option>
        <option value="frio">Frio</option>
        <option value="fechado">Fechado</option>
      </select>
      <button type="submit" className="btn-primary">
        Criar Lead
      </button>
    </form>
  );
}
