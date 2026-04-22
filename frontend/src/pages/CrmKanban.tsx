import { useEffect, useState } from "react";
import {
  DragDropContext,
  Droppable,
  Draggable,
  DropResult,
} from "react-beautiful-dnd";
import api from "../services/api";

type Stage = "novo_lead" | "contato" | "proposta" | "negociacao" | "fechado";

interface Lead {
  id: number;
  nome: string;
  whatsapp: string;
  status: Stage;
}

export default function CrmKanban() {
  const [columns, setColumns] = useState<Record<Stage, Lead[]>>({
    novo_lead: [],
    contato: [],
    proposta: [],
    negociacao: [],
    fechado: [],
  });

  const loadLeads = async () => {
    const { data } = await api.get<Lead[]>("/leads");
    const grouped = data.reduce((acc, lead) => {
      (acc[lead.status] = acc[lead.status] || []).push(lead);
      return acc;
    }, {} as Record<Stage, Lead[]>);
    setColumns({ ...columns, ...grouped });
  };

  useEffect(() => {
    loadLeads();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const onDragEnd = async (result: DropResult) => {
    const { source, destination, draggableId } = result;
    if (!destination) return;
    if (
      source.droppableId === destination.droppableId &&
      source.index === destination.index
    )
      return;

    const movedLeadId = Number(draggableId);
    const newStatus = destination.droppableId as Stage;

    // Optimistic UI update
    const srcList = Array.from(columns[source.droppableId as Stage]);
    const [moved] = srcList.splice(source.index, 1);
    const destList = Array.from(columns[newStatus]);
    destList.splice(destination.index, 0, moved);

    setColumns({
      ...columns,
      [source.droppableId]: srcList,
      [newStatus]: destList,
    });

    // Persist change
    await api.put(`/leads/${movedLeadId}`, { status: newStatus });
  };

  const stageOrder: Stage[] = [
    "novo_lead",
    "contato",
    "proposta",
    "negociacao",
    "fechado",
  ];
  const stageLabel: Record<Stage, string> = {
    novo_lead: "Novo Lead",
    contato: "Contato",
    proposta: "Proposta",
    negociacao: "Negociação",
    fechado: "Fechado",
  };

  return (
    <section className="p-6 bg-gray-900/30 min-h-screen text-white">
      <h2 className="text-2xl mb-4">CRM Kanban</h2>
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="grid grid-cols-5 gap-4 overflow-x-auto">
          {stageOrder.map((stage) => (
            <Droppable droppableId={stage} key={stage}>
              {(provided, snapshot) => (
                <div
                  className={`glass p-4 h-[70vh] overflow-y-auto ${
                    snapshot.isDraggingOver ? "border-2 border-blue-500" : ""
                  }`}
                  ref={provided.innerRef}
                  {...provided.droppableProps}
                >
                  <h3 className="text-lg font-medium mb-2">{stageLabel[stage]}</h3>
                  {columns[stage].map((lead, idx) => (
                    <Draggable
                      draggableId={lead.id.toString()}
                      index={idx}
                      key={lead.id}
                    >
                      {(pr, snap) => (
                        <div
                          className={`glass p-2 mb-2 cursor-move ${
                            snap.isDragging ? "shadow-xl" : ""
                          }`}
                          ref={pr.innerRef}
                          {...pr.draggableProps}
                          {...pr.dragHandleProps}
                        >
                          <p className="font-medium">{lead.nome}</p>
                          <p className="text-sm">{lead.whatsapp}</p>
                        </div>
                      )}
                    </Draggable>
                  ))}
                  {provided.placeholder}
                </div>
              )}
            </Droppable>
          ))}
        </div>
      </DragDropContext>
    </section>
  );
}
