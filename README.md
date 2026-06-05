# Eagle Bluff

Short-term rental documentation and operations for **Eagle Bluff** on **Herron Island, Washington**.

This repository is the single source of truth for guest guides, house rules, operations, marketing, and (eventually) content surfaced in a .NET MAUI guest app.

---

## Quick Start

1. **Capture ideas** → [`docs/00-TODO.md`](docs/00-TODO.md)
2. **Log guest questions** → [`operations/GuestQuestions.md`](operations/GuestQuestions.md)
3. **Fill guest docs** → [`docs/`](docs/) (start with Welcome Book and House Rules)
4. **AI assistants** → read [`CLAUDE.md`](CLAUDE.md) for project context and rules

---

## Documentation

| Document | Purpose |
|----------|---------|
| [Welcome Book](docs/10-WelcomeBook.md) | Main guest guide (20–30 pages) |
| [House Rules](docs/20-HouseRules.md) | Standalone rules (2–4 pages) |
| [Quick Start Sheet](docs/25-QuickStartSheet.md) | One-page kitchen counter sheet |
| [Ferry & Arrival Guide](docs/30-FerryArrivalGuide.md) | Ferry logistics (critical) |
| [Emergency Guide](docs/35-EmergencyGuide.md) | Standalone emergency reference |
| [Checkout Checklist](docs/40-CheckoutChecklist.md) | Departure checklist |
| [Guest Registration](docs/45-GuestRegistration.md) | Check-in acknowledgement form |

---

## Operations (host-only)

| Document | Purpose |
|----------|---------|
| [Guest Questions](operations/GuestQuestions.md) | Question log → feeds welcome book |
| [Cleaner Checklist](operations/CleanerChecklist.md) | Turnover procedures |
| [Inventory](operations/Inventory.md) | Property inventory for insurance |
| [Maintenance Log](operations/MaintenanceLog.md) | Repairs and scheduled service |

---

## Structure

```
EagleBluff/
├── CLAUDE.md           # AI assistant instructions
├── docs/               # Guest-facing documentation
├── operations/         # Host procedures
├── marketing/          # Listing and promotional content
├── legal/              # Agreements and legal templates
└── assets/             # Photos, maps, ferry materials
    ├── photos/
    ├── maps/
    └── ferry/
```

---

## Phased Rollout

| Phase | Focus |
|-------|-------|
| **1 — Now** | TODO backlog, Welcome Book, House Rules |
| **2 — Weeks** | Ferry guide, emergency, checkout, quick start |
| **3 — After guests** | Refine from GuestQuestions log; harden operations |

---

## Future: MAUI App

Planned .NET MAUI app will:

- Surface guest documentation
- Answer common questions
- Track wildlife observations (orcas, eagles)

Content model TBD — markdown in this repo is the source of truth.
