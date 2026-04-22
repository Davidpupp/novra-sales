import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Header from "../components/Header";
import Dashboard from "../pages/Dashboard";
import Leads from "../pages/Leads";
import SalesAI from "../pages/SalesAI";
import CrmKanban from "../pages/CrmKanban";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/leads" element={<Leads />} />
        <Route path="/sales" element={<SalesAI />} />
        <Route path="/crm" element={<CrmKanban />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
