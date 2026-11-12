# Outgrid Labs: sales workspace

Everything for selling and delivering Outgrid Labs projects: playbooks, proposals, brand assets and the lead tracker.

## Read these

| Document | What it is |
|---|---|
| [Sales Playbook (phone)](docs/01_Outgrid_Sales_Playbook.pdf) | The only sales document: qualify, discovery call, demo, close, collect. Scripts in Marathi + English, 20 objections, training. |
| [Strategy + Content (phone)](docs/02_Outgrid_Strategy_and_Content.pdf) | Who we sell to, offers and pricing, locked decisions, sprint plan, and the reel calendar with ready-to-shoot scripts. |
| [A4 print versions](docs/print/) | Same two documents, A4, for printing. |
| [Original playbook v1](docs/reference/Outgrid_Sales_Playbook_v1_original.pdf) | The first playbook, kept for reference. |

## Proposals

| Proposal | Prices | Status |
|---|---|---|
| [Quick-delivery app (Blinkit-style)](proposals/Outgrid_Quick_Delivery_App_Proposal.pdf) | Launch ₹2L · Growth ₹3L · Scale ₹4.5L | Ready to send. Fill client name, date, phone, email. |
| [Spare parts marketplace (draft)](sales/spare-parts-proposal-draft.md) | Launch ₹1.75L · Growth ₹2.95L · Scale ₹4.25L | Draft. Fill after discovery call. |

## Working files

- [`sales/tracker.csv`](sales/tracker.csv): every lead, checks passed (0–5), stage, value, next step and date. Update it every night.
- [`brand/outgrid-brand-board.png`](brand/outgrid-brand-board.png): logo, colours (Charcoal `#0B0D12`, Yellow `#FFD014`, Stone `#E5E7EB`, Cloud `#F9FAFB`), patterns. Proposals use Poppins.

## Rebuilding the PDFs

PDFs are generated from HTML with Playwright (Chromium).

```bash
# Sales Playbook + Strategy (phone + A4)
cd docs/src && node build.js

# A proposal (phone-sized)
cd proposals/src && node build.js Outgrid_Quick_Delivery_App_Proposal.html
```

Edit the `.html` source, rebuild, commit both the source and the PDF.
