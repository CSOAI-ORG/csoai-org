# Council of AI (CSOAI Ltd · UK 16939677)

**We measure AI systems against the rules that govern them, sign the result (Ed25519), and re-attest when the measurement changes.**

Not a certifier. Not an enforcer. No accreditation chain. An independent measurement instrument.

Live scores are never stored in this file. They live on the board:

**[GET https://councilof.ai/api/gspc](https://councilof.ai/api/gspc)** · schema `csoai.gspc-axes/0.5`

Snapshot taken 31 Aug 2026 from that API (quote the API, not this paragraph, if they disagree):

| | |
|---|---|
| Slots on the board | **22** |
| Measured | **15** |
| UNMEASURED (declared empty slots) | **7** |
| Behavioural GSPC axes measured | **14 / 14** (13 canonical + jail) |
| Signed cards | **335** (`n_cards == n_cells`) |
| Living stamp | **SIGNED** · `did:web:csoai.org#board-attestation-1` · Ed25519 |
| Methodology DOI | [10.5281/zenodo.21991104](https://doi.org/10.5281/zenodo.21991104) |

UNMEASURED is first-class. A published empty slot is a visible gap, not a fail, not a score.

### Verify (free, no login)

- [councilof.ai/gspc-verify](https://councilof.ai/gspc-verify/)
- [csoai.org/verify](https://csoai.org/verify)

DID: [csoai.org/.well-known/did.json](https://csoai.org/.well-known/did.json)

### Hosting (as of 31 Aug 2026)

Live sites are **Cloudflare Pages + Wrangler**. Not Vercel.

| Host | Pages project |
|---|---|
| [councilof.ai](https://councilof.ai) | `councilof-ai` |
| [csoai.org](https://csoai.org) | `csoai-site` |
| [meok.ai](https://meok.ai) | `meok-os` |

Vercel Git links on this repo were disconnected and the leftover Vercel projects deleted. Deploys: `wrangler pages deploy`.

### Method

Deterministic gold labels · no model judges another model · unparsed counts as UNMEASURED, never as wrong · nothing quoted below n≥30 · a TIE is a TIE, not a win · every published number recomputable from its rows · corrections published, never silently edited.

### Surfaces

| Surface | What it is |
|---|---|
| [councilof.ai](https://councilof.ai) | Measurement body — board, verify, credentials |
| [csoai.org](https://csoai.org) | Public site / DID apex |
| [meok.ai](https://meok.ai) | MEOK OS — yours, on your keys |

### Banks

- [Hugging Face @csoai](https://huggingface.co/csoai)
- Boards dataset: [csoai/gspc-boards](https://huggingface.co/datasets/csoai/gspc-boards)

Open tooling: [carder](https://github.com/CSOAI-ORG/carder) · [inspect-receipts](https://github.com/CSOAI-ORG/inspect-receipts) · [a2a-signed-receipts](https://github.com/CSOAI-ORG/a2a-signed-receipts) · [codabench-gspc](https://github.com/CSOAI-ORG/codabench-gspc)

---

CSOAI Ltd · UK Companies House 16939677 · [nicholas@csoai.org](mailto:nicholas@csoai.org) · We measure. We sign. We re-attest.
