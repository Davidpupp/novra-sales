import api from "../services/api";

export default function LeadsTable({
  leads,
  refresh,
}: {
  leads: any[];
  refresh: () => void;
}) {
  const deleteLead = async (id: number) => {
    if (confirm("Excluir lead?")) {
      await api.delete(`/leads/${id}`);
      refresh();
    }
  };
  return (
    <table className="w-full glass text-sm">
      <thead className="bg-gray-800/30">
        <tr>
          <th className="p-2">Nome</th>
          <th className="p-2">WhatsApp</th>
          <th className="p-2">Status</th>
          <th className="p-2">Origem</th>
          <th className="p-2">Ações</th>
        </tr>
      </thead>
      <tbody>
        {leads.map((l) => (
          <tr key={l.id} className="border-b border-gray-700/30">
            <td className="p-2">{l.nome}</td>
            <td className="p-2">{l.whatsapp}</td>
            <td className="p-2 capitalize">{l.status}</td>
            <td className="p-2">{l.origem}</td>
            <td className="p-2 flex gap-2">
              <button className="text-blue-400 hover:text-blue-300">✏️</button>
              <button className="text-red-400 hover:text-red-300" onClick={() => deleteLead(l.id)}>🗑️</button>
              <button className="text-green-400 hover:text-green-300">🏷️</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
