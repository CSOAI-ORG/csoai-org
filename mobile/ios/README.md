# CSOAI iOS Capacitor Build

> **Move 30** — iOS Capacitor Wrapper for CSOAI v3.1

## Prerequisites

- macOS 12+ with Xcode 14+
- Node.js 18+ (`node -v`)
- Apple Developer account (for signing & TestFlight)
- `npm` or `pnpm` installed

## Quick Start

```bash
cd /Users/nicholas/clawd/csoai-org/mobile

# 1. Install dependencies
npm install

# 2. Add iOS platform
npx cap add ios

# 3. Sync web assets + config
npx cap sync ios

# 4. Open in Xcode
npx cap open ios
```

## Xcode Signing Setup

1. Open `ios/App/App.xcworkspace` in Xcode
2. Select the **App** target → **Signing & Capabilities**
3. Check **Automatically manage signing**
4. Select your **Team** (Apple Developer account)
5. Set **Bundle Identifier**: `org.csoai.app`
6. Ensure **Push Notifications** capability is enabled (auto-added by Capacitor)

## Build & Archive

```bash
# Build release
npx cap build ios --release

# Or via Xcode:
# Product → Archive → Distribute App → App Store Connect
```

## TestFlight Upload

1. In Xcode Organizer, select the archived build
2. Click **Distribute App** → **App Store Connect** → **Upload**
3. Select **TestFlight & App Store**
4. Upload and wait for processing (~10–30 min)
5. In [App Store Connect](https://appstoreconnect.apple.com):
   - Go to **TestFlight** tab
   - Add internal testers (up to 100)
   - Submit for external beta review if needed

## App Store Submission

1. Fill **App Information** in App Store Connect:
   - Name: **CSOAI**
   - Subtitle: *Compliance Intelligence for AI Systems*
   - Category: **Developer Tools**
   - Privacy Policy URL: `https://csoai.org/privacy`
2. Upload screenshots (6.7″, 6.5″, 5.5″ iPhone + iPad)
3. Submit for review (typical: 24–48 hours)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `capacitor.config.ts` not found | Ensure file is at `mobile/capacitor.config.ts` |
| Signing errors | Verify Apple Developer team + bundle ID match |
| Push not working | Add `APS Environment` entitlement manually if missing |
| White screen on launch | Check `webDir` points to built static export |

---
*CSOAI 33 Moves | Move 30 — iOS Capacitor Wrapper*
