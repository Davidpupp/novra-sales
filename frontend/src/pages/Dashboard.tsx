import { useEffect, useState } from "react";
import api from "../services/api";
import Card from "../components/Card";

interface Stats {
  total_leads: number;
  leads_quentes: number;
  taxa_conversao: number;
  vendas_fechadas: number;
  ticket_medio: number;
}

export default function Dashboard() {
  const [stats, setStats] = useState<Stats | null>(null);

  useEffect(() => {
    api.get("/dashboard")
      .then((r) => setStats(r.data))
      .catch(console.error);
  }, []);

  if (!stats) return <div className="p-8 text-white">Carregando…</div>;

  const cards = [
    { title: "Leads Hoje", value: stats.total_leads },
    { title: "Leads Quentes", value: stats.leads_quentes },
    { title: "Conversão", value: `${(stats.taxa_conversao * 100).toFixed(1)}%` },
    { title: "Receita (R$)", value: (stats.vendas_fechadas * stats.ticket_medio).toFixed(2) },
  ];

  return (
    <section className="p-8 grid gap-6 grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
      {cards.map((c) => (
        <Card key={c.title} title={c.title} value={c.value} />
      ))}
    </section>
  );
}
