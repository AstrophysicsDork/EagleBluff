# Secrets — How This Works

> **Why this folder exists:** the GitHub repo is **public**. Anything committed here is visible to the entire internet and indexed by search engines. So real WiFi passwords, door codes, gate/alarm codes, etc. must **never** be committed.

## The pattern

| File | Committed to git? | Contains |
|------|-------------------|----------|
| `README.md` (this file) | ✅ Yes | Explanation only |
| `SECRETS.template.md` | ✅ Yes | Blank structure, no real values |
| `SECRETS.local.md` | ❌ **No** (gitignored) | The **real** values |

The `.gitignore` ignores `secrets/*.local.*`, so `SECRETS.local.md` stays on your machine (and Haidee's, if shared privately) but never reaches GitHub.

## How values reach the printed welcome book

Guest-facing docs (e.g. [`docs/25-QuickStartSheet.md`](../docs/25-QuickStartSheet.md)) keep **placeholders** like `{{WIFI_PASSWORD}}` or a `<!-- TODO -->`.

At **print time** (not in the repo), you fill the real values from `SECRETS.local.md` into the printed copy. This keeps:

- The public repo clean (no secrets)
- One private source of truth for sensitive values
- Guests still get the password on the paper sheet in the house

> WiFi passwords are *meant* to be shared with guests — but on **paper in the home / in the Airbnb app message**, not in a public code repository.

## Sharing the local file safely

- Send to Haidee via text/email/password manager — **not** by committing
- If you ever paste a code into a chat with the AI, that's fine for filling docs, but the AI will keep it in `*.local.md` (ignored), never in a committed file

## If a secret ever gets committed by accident

Tell the AI. Steps: rotate the value (change the password/code), then scrub it from git history. Don't just delete the file — git remembers.
