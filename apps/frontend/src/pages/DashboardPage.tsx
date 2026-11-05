export function DashboardPage() {
  return (
    <div className="space-y-6">
      <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
        <p className="text-sm uppercase tracking-[0.2em] text-cyan-400">Overview</p>
        <h1 className="mt-3 text-3xl font-semibold text-white">Healthcare dashboard</h1>
        <p className="mt-2 text-slate-400">
          This foundation is ready for clinical, operational, and reporting modules to be added after approval.
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-3">
        {[
          { label: 'Appointments', value: '184', tone: 'bg-cyan-500/10 text-cyan-300' },
          { label: 'Patients', value: '2,490', tone: 'bg-emerald-500/10 text-emerald-300' },
          { label: 'Pending Tasks', value: '23', tone: 'bg-amber-500/10 text-amber-300' },
        ].map((card) => (
          <div key={card.label} className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">{card.label}</p>
            <div className={`mt-4 inline-flex rounded-full px-3 py-1 text-sm font-medium ${card.tone}`}>
              {card.value}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
