import { useEffect, useState } from "react";
import api from "../services/api";
import LeadForm from "../components/LeadForm";
import LeadsTable from "../components/LeadsTable";

export default function Leads() {
  const [leads, setLeads] = useState<any[]>([]);

  const fetchLeads = () => {
    api.get("/leads")
      .then((r) => setLeads(r.data))
      .catch(console.error);
  };

  useEffect(fetchLeads, []);

  return (
    <section className="p-8 text-white">
      <h2 className="text-2xl mb-4">Leads</h2>
      <LeadForm onSuccess={fetchLeads} />
      <LeadsTable leads={leads} refresh={fetchLeads} />
    </section>
  );
}
