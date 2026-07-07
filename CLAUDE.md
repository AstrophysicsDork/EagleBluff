# EagleBluff AI Assistant Instructions

## Project Overview

This repository contains all documentation, operational procedures, guest-facing materials, business records, and marketing content for **Eagle Bluff**, a short-term rental property located on **Herron Island, Washington**.

The property is owned primarily by Jeff (51%) and is being prepared as a seasonal vacation rental, primarily targeting peak-season guests (roughly May–September).

This repository is intended to become the single source of truth for:

- Guest documentation
- House rules
- Welcome materials
- Emergency procedures
- Property operations
- Maintenance history
- Marketing content
- Airbnb listing content
- Business procedures

**Future:** Content in this repo will surface in a .NET MAUI app for guests (guides, Q&A) and for tracking wildlife observations (orcas, eagles).

---

## What We Know About The Property

Herron Island is a private island in Puget Sound.

Key characteristics:

- Access is primarily via **private HMCHI ferry** — **not** Washington State Ferries (WSDOT)
- Ferry info: [hmchi.org/p/FERRY](https://www.hmchi.org/p/FERRY)
- **Valid guest pass required** to board; coordinated by **Haidee Clingman** (cleaner / on-island contact) for rental guests
- Mainland dock: **201 Isted Rd NW, Lakebay, WA**
- **$25 per vehicle + $5 per guest, per crossing — cash** (no practical vehicle limit per reservation)
- Guest vehicles: **license plate sent to ferry crew in advance**; host HMCHI member number 349
- Crossing time ~7–10 minutes
- Guests must understand ferry logistics before arrival
- Grocery and supply access is limited after crossing
- The island is quiet and residential
- Wildlife is common
- Guests are seeking a peaceful escape experience
- Guests may have unrealistic expectations about services and convenience
- Setting expectations is extremely important

The rental experience is not simply a house rental. It is an **island retreat experience**.

Documentation should emphasize:

- Peace
- Nature
- Slower pace
- Scenic views
- Wildlife
- Beach access
- Disconnecting from city life

---

## Documentation Philosophy

Documentation is expected to evolve continuously. Never assume documentation is complete.

Whenever information is discovered:

1. Add it somewhere
2. Do not discard partial information
3. Prefer creating TODO items rather than losing details
4. Favor incremental improvement over perfection

**Capture rule:** When a guest asks a question, add it to `operations/GuestQuestions.md` before answering. That file eventually becomes 80% of the welcome book.

---

## Repository Goals

1. Reduce guest confusion
2. Reduce repetitive guest questions
3. Reduce owner support burden
4. Improve guest reviews
5. Protect the property
6. Protect septic and utility systems
7. Create repeat guests
8. Build a professional rental operation

---

## Highest Priority Documents

Create and maintain these first:

| Priority | Document | Path |
|----------|----------|------|
| 1 | Welcome Book (hub) | `docs/10-WelcomeBook.md` |
| 1a | Surrounding area & getting here | `docs/11-SurroundingArea.md` |
| 1b | Island & nearby | `docs/12-IslandAndNearby.md` |
| 1c | The home (inside/out) | `docs/13-TheHome.md` |
| 2 | House Rules | `docs/20-HouseRules.md` |
| 3 | Quick Start Sheet | `docs/25-QuickStartSheet.md` |
| 4 | Ferry & Arrival Guide | `docs/30-FerryArrivalGuide.md` |
| 4b | Ferry Schedules | `docs/31-FerrySchedules.md` |
| 5 | Emergency Guide | `docs/35-EmergencyGuide.md` |
| 6 | Checkout Checklist | `docs/40-CheckoutChecklist.md` |

All other documentation is secondary.

---

## Guest Experience Priorities

### Before Arrival

- Ferry information
- Arrival instructions
- Grocery recommendations
- Packing recommendations
- Parking information
- Access instructions

### During Stay

- WiFi
- Appliance instructions
- Heating instructions
- Fireplace instructions
- Wildlife information
- Things to do
- Island etiquette

### Departure

- Checkout process
- Trash procedures
- Lockup instructions

---

## Important Operational Risks

Document these clearly and early:

### Septic System

Guests must understand what may be flushed, what may not, and consequences of misuse.

### Water Systems

Conservation requirements, water source information, leak reporting.

### Ferry Dependence

Private HMCHI ferry (not WSDOT). Guest pass required. **Seasonal PDF schedules** plus a **cancellations/low-tide bulletin** updated regularly — guests must check both. Summer vs winter grids; IS/ML departure pairs. Low tide (~−1.5 ft) cancels runs. Many guests mistakenly search for Washington State Ferries — set this expectation early. Future: dock cameras on both sides; not live yet.

### Power Outages

What to do, who to contact, what resources are available.

---

## Working Style

When generating content:

- Use markdown
- Prefer concise sections
- Use bullet lists extensively
- Assume guests skim rather than read
- Keep instructions simple
- Use headings aggressively

When uncertain:

- Add TODO items to `docs/00-TODO.md`
- Ask questions
- **Never invent property-specific facts** (addresses, phone numbers, WiFi passwords, appliance models, etc.)

---

## Repository Structure

```
EagleBluff/
├── CLAUDE.md                 # AI assistant instructions (this file)
├── README.md                 # Project overview for humans
├── docs/                     # Guest-facing documentation
│   ├── 00-TODO.md            # Capture bucket
│   ├── 10-WelcomeBook.md     # Hub — welcome letter, why people love it
│   ├── 11-SurroundingArea.md # Mainland, drives, stock-up (NOT ferry)
│   ├── 12-IslandAndNearby.md # Island life, beaches, wildlife, day trips
│   ├── 13-TheHome.md         # Property inside & out
│   ├── _future/              # Ideas not yet live (e.g. GuestImpact)
│   ├── 20-HouseRules.md
│   ├── 25-QuickStartSheet.md
│   ├── 30-FerryArrivalGuide.md  # Ferry — its own concern
│   ├── 31-FerrySchedules.md
│   ├── 35-EmergencyGuide.md
│   ├── 40-CheckoutChecklist.md
│   └── 45-GuestRegistration.md
├── operations/               # Host/operator procedures (not for guests)
│   ├── GuestQuestions.md
│   ├── _future/              # Ops ideas not yet live
│   ├── CleanerChecklist.md
│   ├── Inventory.md
│   └── MaintenanceLog.md
├── marketing/                # Listing and promotional content
│   ├── AirbnbListing.md
│   ├── PropertyDescription.md
│   └── GuestReviewsIdeas.md
├── legal/
│   └── RentalAgreement.md
└── assets/
    ├── photos/
    ├── maps/
    └── ferry/
```

---

## Phased Rollout

### Phase 1 (Now)

Focus on `docs/00-TODO.md`, `10-WelcomeBook.md`, and `20-HouseRules.md`. Dump everything into TODO; move items into docs as they mature.

### Phase 2 (Next few weeks)

Fill welcome book and house rules. Split ferry, emergency, and checkout content into dedicated docs as sections grow.

### Phase 3 (After first guests)

Refine based on `operations/GuestQuestions.md`. Harden cleaner checklist, inventory, and emergency procedures.

---

## Special Instruction

Whenever a new fact is learned about the property, island, guest behavior, ferry operations, amenities, utilities, appliances, wildlife, or local attractions — **capture it immediately**.

Information lost is more expensive than imperfect organization.
