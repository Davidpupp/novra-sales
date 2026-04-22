import { useState } from "react";
import api from "../services/api";

export default function SalesAI() {
  const [form, setForm] = useState({
    nome: "",
    segmento: "",
    interesse: "",
    temperatura: "quente" as const,
  });
  const [result, setResult] = useState<any>(null);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    const { data } = await api.post("/sales/generate-message", form);
    setResult(data);
  };

  return (
    <section className="p-8 text-white">
      <h2 className="text-2xl mb-4">IA de Vendas</h2>
      <form className="glass p-6 flex flex-col gap-4 mb-6" onSubmit={handleSend}>
        <input
          className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
          placeholder="Nome cliente"
          value={form.nome}
          onChange={(e) => setForm({ ...form, nome: e.target.value })}
          required
        />
        <input
          className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
          placeholder="Segmento"
          value={form.segmento}
          onChange={(e) => setForm({ ...form, segmento: e.target.value })}
          required
        />
        <input
          className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white placeholder-white/50"
          placeholder="Interesse"
          value={form.interesse}
          onChange={(e) => setForm({ ...form, interesse: e.target.value })}
          required
        />
        <select
          className="input bg-white/10 border border-white/20 rounded px-3 py-2 text-white"
          value={form.temperatura}
          onChange={(e) =>
            setForm({ ...form, temperatura: e.target.value as any })
          }
        >
          <option value="quente">Quente</option>
          <option value="morno">Morno</option>
          <option value="frio">Frio</option>
          <option value="fechado">Fechado</option>
        </select>
        <button className="btn-primary self-start">GERAR MENSAGEM</button>
      </form>

      {result && (
        <div className="glass p-4">
          <h3 className="text-xl mb-2">Resultado</h3>
          <p><strong>WhatsApp:</strong> {result.mensagem_whatsapp}</p>
          <p><strong>Tom:</strong> {result.tom}</p>
          <p><strong>Chance de Fechamento:</strong> {(result.chance_fechamento * 100).toFixed(1)}%</p>
        </div>
      )}
    </section>
  );
}
