"use client";

export default function McpPacks() {
  const packs = [
    {
      id: "pack_eu_ai_act",
      name: "EU AI Act Emergency Pack",
      desc: "7 MCP servers designed specifically to enforce EU AI Act Article 50 transparency and risk classification at runtime.",
      price: "£999",
      billing: "one-time",
      servers: ["csoai-layer0-compliance", "csoai-risk-classifier", "csoai-article50-watermark", "csoai-human-oversight-trigger"]
    },
    {
      id: "pack_growth",
      name: "Brand & Distribution Pack",
      desc: "Automate your entire Go-To-Market strategy. The exact MCP tools CSOAI uses to get 200,000 downloads.",
      price: "£499",
      billing: "one-time",
      servers: ["csoai-brand-authority", "csoai-aeo-geo-optimizer", "csoai-conversion-funnel", "csoai-social-automation"]
    },
    {
      id: "pack_finance",
      name: "Agentic Finance Pack",
      desc: "Pre-check compliance before any agent executes a payment via Stripe ACP, x402, or AP2.",
      price: "£1,499",
      billing: "annually",
      servers: ["csoai-payment-precheck", "csoai-aml-kyc-validator", "csoai-x402-tunnel", "csoai-stripe-acp-tunnel"]
    }
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white selection:bg-emerald-500/30">
      <div className="max-w-7xl mx-auto px-4 py-24">
        <div className="text-center mb-20">
          <h1 className="text-6xl font-black mb-6 tracking-tighter bg-gradient-to-r from-white to-emerald-500 bg-clip-text text-transparent">PREMIUM MCP PACKS</h1>
          <p className="text-slate-400 text-xl max-w-2xl mx-auto leading-relaxed">
            Monetizing 290+ open-source assets into production-ready governance bundles. The missing software for the agentic economy.
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {packs.map((p) => (
            <div key={p.id} className="p-10 rounded-3xl bg-white/5 border border-white/10 hover:border-emerald-500/30 transition-all group flex flex-col">
              <h3 className="text-2xl font-bold mb-4 text-emerald-400">{p.name}</h3>
              <p className="text-sm text-slate-400 mb-8 flex-grow leading-relaxed">{p.desc}</p>
              <div className="mb-8">
                 <div className="text-4xl font-black">{p.price}</div>
                 <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest mt-1">{p.billing}</div>
              </div>
              <div className="border-t border-white/5 pt-6 mb-10">
                 <span className="text-[10px] font-black text-slate-500 uppercase tracking-widest block mb-4">Includes</span>
                 <ul className="space-y-2">
                    {p.servers.map(s => (
                       <li key={s} className="text-xs font-mono text-slate-300">/ {s}</li>
                    ))}
                 </ul>
              </div>
              <button className="w-full py-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold transition shadow-lg shadow-emerald-500/20">
                Purchase Pack
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
