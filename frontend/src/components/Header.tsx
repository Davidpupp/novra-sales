import { Link } from "react-router-dom";
import { useState } from "react";

export default function Header() {
  const [dark, setDark] = useState(true);
  return (
    <header
      className={`glass p-4 flex justify-between items-center ${
        dark ? "bg-gray-900/40" : "bg-white/30"
      }`}
    >
      <h1 className="text-2xl font-bold text-white">NOVRA SALES AI</h1>
      <nav className="flex gap-4">
        <Link to="/" className="text-white hover:underline">
          Dashboard
        </Link>
        <Link to="/leads" className="text-white hover:underline">
          Leads
        </Link>
        <Link to="/sales" className="text-white hover:underline">
          IA Vendas
        </Link>
        <Link to="/crm" className="text-white hover:underline">
          CRM
        </Link>
      </nav>
      <button className="btn-primary" onClick={() => setDark(!dark)}>
        {dark ? "Light" : "Dark"}
      </button>
    </header>
  );
}
