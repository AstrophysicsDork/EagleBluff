# Maps

> **Populated.** Travel-time route maps + Google Earth context. Canonical location — docs link here.

Property reference: **22604** (Herron Island). Routes use **Herron Island Ferry Dock** as mainland start point unless noted.

---

## Google Earth — Island & Region

| File | Shows |
|------|--------|
| [island-south-beach-lighthouse.png](island-south-beach-lighthouse.png) | **South Herron Island** — South Beach Park, Miniature Lighthouse, beach, homes |
| [region-case-inlet-herron-harstine.png](region-case-inlet-herron-harstine.png) | **Case Inlet** — Herron Island, Harstine Island, Joemma Beach, Ballow |
| [region-puget-sound-wide-rainier.png](region-puget-sound-wide-rainier.png) | **Wide Puget Sound** — Seattle, Tacoma, islands, Mt. Rainier |
| [region-south-sound-tacoma-olympia.png](region-south-sound-tacoma-olympia.png) | **South Sound** — Tacoma, Olympia, Anderson/Fox/Harstine islands, Rainier & Hood |

Use in: `docs/12-IslandAndNearby.md`, welcome book intro.

---

## Travel Times — Mainland Ferry Dock → …

All routes start at **Herron Island Ferry Dock** (Google: 20801 Isted Rd — verify vs. 201 Isted Rd NW in ferry docs).

| File | Time | Destination | Address / notes |
|------|------|-------------|-----------------|
| [route-07min-2-margaritas.png](route-07min-2-margaritas.png) | **7 min** · 3.4 mi | **2 Margaritas** | 1509 Key Peninsula Hwy NW |
| [route-20min-key-iga.png](route-20min-key-iga.png) | **20 min** · 12.3 mi | **Key IGA** (grocery) | 9021 Key Peninsula Hwy NW |
| [route-28min-massimo-italian-purdy.png](route-28min-massimo-italian-purdy.png) | **28–30 min** · ~17 mi | **Massimo Italian Bar & Grill** | 13802 Purdy Dr NW, Purdy |
| [route-36min-gig-harbor.png](route-36min-gig-harbor.png) | **36 min** · 22.2 mi | **Gig Harbor** | Waterfront town |
| [route-48min-tacoma-narrows-toll.png](route-48min-tacoma-narrows-toll.png) | **48 min** · 34.8 mi | **Tacoma** | Via WA-16 E · **Narrows Bridge toll** |
| [route-75min-seatac-to-island.png](route-75min-seatac-to-island.png) | **1 hr 15 min** · 53.1 mi | **SeaTac → Herron Island** | Airport to property |
| [route-125min-mt-rainier.png](route-125min-mt-rainier.png) | **~2 hr** · ~87 mi | **Mt. Rainier National Park** | Day trip · tolls on some routes |
| [route-133min-olympic-np.png](route-133min-olympic-np.png) | **~2 hr 13 min** · ~106 mi | **Olympic National Park** | Day trip via US-101 |

Use in: `docs/11-SurroundingArea.md`, `docs/12-IslandAndNearby.md` (day trips).

---

## Naming Convention

| Prefix | Meaning | Example |
|--------|---------|---------|
| `route-{NN}min-` | Drive from mainland ferry dock | `route-20min-key-iga.png` |
| `island-` | Herron Island satellite | `island-south-beach-lighthouse.png` |
| `region-` | Wider geographic context | `region-case-inlet-herron-harstine.png` |
| `property-22604-` | *(future)* Site-specific | `property-22604-walk-south-beach.png` |

---

## Still Missing (on-site visit)

- [ ] `property-22604-grounds.png` — annotated deck, fire pit, beach path
- [ ] `property-22604-walk-south-beach.png` — route from house to South Beach
- [ ] Confirm ferry dock street number (201 vs 20801 Isted Rd)

---

## How to Add More

1. Google Maps → directions from **Herron Island Ferry Dock**
2. Screenshot → name `route-{NN}min-{slug}.png`
3. Drop in `assets/maps/` (property photos go in `assets/photos/`)
4. Add row to this README + link from docs
