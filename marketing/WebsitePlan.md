# Eagle Bluff — Website Plan

> Goal: get domains pointing at *something* ASAP, then grow into a real site. Booking still flows through Airbnb for now.

**Status:** Planning. Need registrar + domain list from Jeff (see bottom).

---

## The 3-Phase Path (fastest → fullest)

### Phase 0 — "Domains do something" (today, ~10 min, $0)

Use your **registrar's built-in URL forwarding** to redirect every domain to the live Airbnb listing:

> `https://www.airbnb.com/rooms/1698780813654737500`

- Pro: live in minutes, zero hosting, looks intentional
- Con: it's just a redirect (no branding, no SEO of your own)
- Good enough until Phase 1

### Phase 1 — One-page landing site (this week, $0 hosting)

A single branded page: hero photo, tagline, "Book on Airbnb" button, ferry-aware blurb, contact.

- **Host:** Cloudflare Pages **or** Netlify **or** GitHub Pages (all free; repo is already on GitHub)
- **Recommended:** Cloudflare Pages — free, fast, and Cloudflare also makes the domain redirects (Phase 2) trivial
- Pick **ONE canonical domain** (e.g. `eaglebluffretreat.com`); the rest **301-redirect** to it
- Content can reuse `marketing/PropertyDescription.md` + a hero from `assets/photos/`

### Phase 2 — Full site from the repo (later)

Multi-page site generated from the markdown you already have:

| Page | Source doc |
|------|------------|
| Home | `marketing/PropertyDescription.md` |
| The Home | `docs/13-TheHome.md` |
| Island & Area | `docs/12-IslandAndNearby.md`, `docs/11-SurroundingArea.md` |
| Ferry & Arrival | `docs/30-FerryArrivalGuide.md`, `docs/31-FerrySchedules.md` |
| Gallery | `assets/photos/` |
| FAQ | `operations/GuestQuestions.md` (curated) |
| Contact / Book | Airbnb link + form |

- **Tooling options:** Astro (great fit, matches your `AstroDork` handle 😄), Eleventy, or MkDocs
- Keeps the repo as the single source of truth — site rebuilds from markdown

---

## How Domain Redirects Work (registrar-agnostic)

You have two jobs: **(1) host the site somewhere**, **(2) point domains at it**.

### Option A — Registrar URL forwarding (Phase 0)
Most registrars (GoDaddy, Namecheap, Squarespace/Google, Porkbun, Cloudflare) have a **"Forwarding"** setting:
`Domain → Forwarding → forward to <URL>` with **301 (permanent)**. Done.

### Option B — Point DNS at a host (Phase 1+)
1. Host the page (Cloudflare Pages / Netlify / GitHub Pages)
2. In the host, **add your custom domain** — it gives you DNS records
3. In the registrar (or move DNS to Cloudflare), set those records:
   - `CNAME` (or `A`/`ALIAS`) for the apex/root
   - `CNAME www` → host
4. Extra domains: set each to **301 redirect** to the canonical one

### Canonical domain rule
Pick **one** primary. Every other domain redirects to it (better SEO, no duplicate-content split, one place to maintain).

---

## Domains On Hand (all at Squarespace) — inventory 2026-06-23

| Domain | Theme | Expires | Note |
|--------|-------|---------|------|
| **`herronsangels.com`** | **Herron's Angels — on-brand!** | (Active) | ⭐ strong canonical candidate for the rental |
| `ngels.com` | fragment of "angels"? | 2027-09-17 | maybe related to Herron's Angels |
| `iamjeffderemer.com` | Personal | 2028-06-05 | |
| `jeffderemer.com` / `.net` / `.org` | Personal | 2028-06-05 | |
| `philanthrobot.net` / `.org` | Philanthropy + robot/AI | 2028-05-28 | could tie to future giving idea |
| `philanthrobotics.com` / `.net` | Philanthropy + robot/AI | 2028-05-28 | |
| `terranastra.com` / `.org` | "Terra Nastra" (earth/land) | **2026-06-06 — EXPIRED** | ⏰ decide: renew or release |
| `terranastralparks.org` | Land / parks | **2026-07-01 — expiring soon** | ⏰ |
| `terranastraparks.org` | Land / parks | **2026-07-01 — expiring soon** | ⏰ |
| `theseapps.net` / `.org` | Apps / dev | 2027-02-26 | |

**Finding:** `herronsangels.com` is the one on-brand, Herron-themed domain already owned. ⭐

---

## Branding Question (decide before the website)

Two names are in play:

| Name | Source | Vibe |
|------|--------|------|
| **Eagle Bluff (Retreat)** | The property / this repo | Place-based, calm, scenic |
| **Herron's Angels** | `herronsangels.com` you own | Playful, memorable, island-specific |

They can **coexist**: e.g. *Herron's Angels* as a friendly umbrella/host brand, *Eagle Bluff* as the specific home. Or pick one public face. **You decide** — this drives logo, listing title, and which domain is canonical.

---

## Canonical Domain Options

### Option A — Use `herronsangels.com` (recommended: free + on-brand + owned today)
You already own it. Forward it to Airbnb now (Phase 0), host the landing page on it later (Phase 1). Zero new cost.

### Option B — Register a dedicated `eaglebluff*` domain (~$15/yr)
If you want the public face to be "Eagle Bluff." Check availability in Squarespace → *Get a domain*:
`eaglebluffretreat.com` · `herronbluff.com` · `herronislandretreat.com`

> You can do **both**: register `eaglebluffretreat.com` *and* point `herronsangels.com` at it.

**My recommendation:** Start with **Option A today** (it's free and you own it). Decide the long-term brand separately — forwarding is reversible in minutes.

---

## Squarespace-Specific Steps

### Phase 0 — Forward a domain to Airbnb (today)
> Squarespace hides this under **Website**, not a top-level "Forwarding" menu.

1. Log in at **squarespace.com** → profile icon → **Domains**
2. Click **`herronsangels.com`**
3. Left sidebar → **Website**
4. Scroll to **Domain forwarding rules** → **Add Rule**
5. **Forward from:** type `@` (the root domain). ⚠️ Note: `@` removes existing Squarespace records — fine for a parked domain not connected to a site.
6. **Forward to:** `https://www.airbnb.com/rooms/1698780813654737500`
7. (Optional) Advanced: choose **301 permanent**
8. **Save** → it shows **Pending**; can take **24–48 hours** to go live
9. Test later in a browser

> If you also want `www.herronsangels.com` to work, add a second rule forwarding from `www`.

### Phase 1 — Point a domain at a hosted page (this week)
1. Build/landing page on **Cloudflare Pages** or **Netlify** (free)
2. In the host: *Add custom domain* → it shows DNS records
3. In Squarespace: **DNS settings** → add the records (CNAME/A) the host gives you
4. Other domains → **301 forward** to the canonical one

> Squarespace tip: you can move a domain's DNS to **Cloudflare** for free if we want Cloudflare to manage everything (hosting + redirects in one place). Optional.

---

## STILL NEED FROM JEFF

- [ ] **Brand face:** "Eagle Bluff (Retreat)" vs "Herron's Angels" vs both
- [ ] **Canonical domain:** use `herronsangels.com` (free, recommended) or register `eaglebluff*`?
- [ ] OK to forward canonical → **Airbnb** for Phase 0 today?
- [ ] OK to use **Cloudflare** (or Netlify) for the Phase 1 page?
- [ ] ⏰ **Separate decision:** renew or release the `terranastra*` domains before they lapse?

---

## Notes

- Booking stays on **Airbnb** for now (no payment/legal plumbing needed on the site)
- Branding: **"Eagle Bluff Retreat"** — calm/PNW tone, no resort-speak (see `docs/00-TODO.md` brand note)
- A direct-booking site is a *much* later Phase 3 (Stripe, rental agreement, calendar sync) — not now
