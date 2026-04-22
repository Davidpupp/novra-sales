interface CardProps {
  title: string;
  value: string | number;
}
export default function Card({ title, value }: CardProps) {
  return (
    <div className="glass p-6 text-center text-white">
      <h3 className="text-lg font-medium">{title}</h3>
      <p className="text-3xl font-bold mt-2">{value}</p>
    </div>
  );
}
