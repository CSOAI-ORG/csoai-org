"use client";

export default function Verify() {
  return (
    <div className="min-h-screen bg-slate-950 text-white selection:bg-emerald-500/30">
      <div className="max-w-3xl mx-auto px-4 py-20 text-center">
        <h1 className="text-5xl font-black mb-4 tracking-tighter text-emerald-400 uppercase">Verification Engine</h1>
        <p className="text-slate-400 text-lg mb-12">Verify CSOAI Watchdog Certificates and Agent Identities instantly via Polygon PoA.</p>
        
        <div className="flex gap-2 p-2 rounded-2xl bg-white/5 border border-white/10 shadow-2xl">
          <input 
            type="text" 
            placeholder="did:csoai:8822-15e9c129d0c2..." 
            className="flex-1 bg-transparent border-none px-6 py-4 font-mono text-white outline-none"
          />
          <button className="px-8 py-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold transition">
            VERIFY
          </button>
        </div>

        <div className="mt-20 p-8 rounded-3xl bg-slate-900/50 border border-white/5 text-sm text-slate-500 leading-relaxed text-left">
           <strong className="text-white block mb-2 uppercase tracking-widest text-[10px]">Layer 0 Proof:</strong>
           All certificates are signed using <code className="text-emerald-400">Ed25519</code> and anchored to the Polygon PoA network. Verification is performed in real-time against the latest PDCA policy snapshot.
        </div>
      </div>
    </div>
  );
}
