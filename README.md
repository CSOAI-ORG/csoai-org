# Nicholas Templeman

Founder of **[Council of AI](https://councilof.ai)** (CSOAI Ltd, UK 16939677). London.

We measure AI systems against the rules that govern them, sign the result (Ed25519), and re-attest when it changes. **Measurement, not certification.** Not a notified body. We do not sell ratings, remediate, or take money from anything we rank.

---

### Living board

Scores live here — this file is not the source of truth:

**[GET councilof.ai/api/gspc](https://councilof.ai/api/gspc)** · schema `csoai.gspc-axes/0.5`

| Live GET /api/gspc | |
|---|---|
| Slots | **22** |
| Measured | **22** = **14 model-comparison + 8 fact runs** |
| Not | 22/22 grades · not certified · TIE is TIE |
| Signed cards | **335** |
| councilof.ai/root.json | **SIGNED** public-root-v0 · merkle `d438fb12…` |
| csoai.org/root.json | **STALE unsigned** merkle `4a9a5036…` — do not quote as the envelope |
| Method | [doi:10.5281/zenodo.21991104](https://doi.org/10.5281/zenodo.21991104) |

[![GSPC](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcouncilof.ai%2Fapi%2Fgspc&query=%24.totals.public_count&label=GSPC&color=0B1F33)](https://councilof.ai/gspc-scoreboard)

If this file and the API disagree, the API is right. Measurement, not certification.

**Verify (free, no login):** [councilof.ai/gspc-verify](https://councilof.ai/gspc-verify/) · [csoai.org/verify](https://csoai.org/verify)  
DID: [csoai.org/.well-known/did.json](https://csoai.org/.well-known/did.json)

---

### Sites (Cloudflare Pages + Wrangler — not Vercel)

| | |
|---|---|
| [councilof.ai](https://councilof.ai) | Measurement body |
| [csoai.org](https://csoai.org) | Public site / DID apex |
| [meok.ai](https://meok.ai) | MEOK OS — yours, on your keys |

---

### Method

Deterministic gold labels · no model judges another · unparsed → UNMEASURED, never “wrong” · nothing quoted below n≥30 · a TIE is a TIE · corrections published, never silently edited.

Banks: [huggingface.co/csoai](https://huggingface.co/csoai) · [csoai/gspc-boards](https://huggingface.co/datasets/csoai/gspc-boards)

---

`nicholas@csoai.org` · London
