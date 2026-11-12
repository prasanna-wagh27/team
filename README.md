# Outgrid Labs: sales workspace

## The three documents

| Document | Use it for |
|---|---|
| [Sales Sheet](sheet/Outgrid_Sales_Sheet.pdf) | One page to keep open during chats and calls: who we sell to, first two questions, price list, steps, who we don't take. |
| [Sales Playbook](playbook/Outgrid_Sales_Playbook.pdf) | 4 pages: the six steps to the advance, what each price includes, proof to show, what the agreement covers. |
| [Strategy + Content](strategy/Outgrid_Strategy_and_Content.pdf) | 4 pages: goals, who we serve, decisions and why, the content rule, next reels, what comes later. |

## Proposals

| Proposal | Prices |
|---|---|
| [Quick-delivery app](proposals/Outgrid_Quick_Delivery_App_Proposal.pdf) | Launch ₹2L · Growth ₹3L · Scale ₹4.5L |

Fill in the date on the cover and your phone and email on the last page before sending.

## Working files

- [`sales/tracker.csv`](sales/tracker.csv): every lead, stage, value, next step.
- [`brand/outgrid-brand-board.png`](brand/outgrid-brand-board.png): logo, colours (Charcoal `#0B0D12`, Yellow `#FFD014`, Stone `#E5E7EB`, Cloud `#F9FAFB`). Documents use Poppins.
- [`reference/`](reference/): the original v1 playbook, kept for reference.

## Rebuilding a PDF

Each folder has its HTML source in `src/`. Edit it, then:

```bash
cd sheet/src && node build.js
cd playbook/src && node build.js Outgrid_Sales_Playbook.html
cd strategy/src && node build.js Outgrid_Strategy_and_Content.html
cd proposals/src && node build.js Outgrid_Quick_Delivery_App_Proposal.html
```

Fonts live in `assets/fonts/`. Commit both the source and the PDF.
