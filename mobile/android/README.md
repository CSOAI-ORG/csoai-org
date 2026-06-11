# CSOAI Android Capacitor Build

> **Move 31** — Android Capacitor Wrapper for CSOAI v3.1

## Prerequisites

- Android Studio Hedgehog (2023.1.1) or newer
- Node.js 18+ (`node -v`)
- JDK 17 (`java -version`)
- Google Play Console account (for upload)

## Quick Start

```bash
cd /Users/nicholas/clawd/csoai-org/mobile

# 1. Install dependencies
npm install

# 2. Add Android platform
npx cap add android

# 3. Sync web assets + config
npx cap sync android

# 4. Open in Android Studio
npx cap open android
```

## Android Studio Signing Setup

### 1. Generate Release Keystore

```bash
cd android/app
keytool -genkey -v -keystore csoai-release.keystore -alias csoai \
  -keyalg RSA -keysize 2048 -validity 10000
```

### 2. Configure `build.gradle` Signing

In `android/app/build.gradle`, ensure:

```gradle
android {
    signingConfigs {
        release {
            storeFile file("csoai-release.keystore")
            storePassword System.getenv("CSOAI_KEYSTORE_PASSWORD")
            keyAlias "csoai"
            keyPassword System.getenv("CSOAI_KEY_PASSWORD")
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

### 3. Set Environment Variables

```bash
export CSOAI_KEYSTORE_PASSWORD="your_keystore_password"
export CSOAI_KEY_PASSWORD="your_key_password"
```

## Build Release APK / AAB

```bash
# Build Android App Bundle (required for Play Console)
cd android
./gradlew bundleRelease

# Output: android/app/build/outputs/bundle/release/app-release.aab

# Or build APK for side-loading
./gradlew assembleRelease
# Output: android/app/build/outputs/apk/release/app-release.apk
```

## Play Console Upload Steps

1. Go to [Google Play Console](https://play.google.com/console)
2. Create app → **CSOAI** → Category: **Developer Tools**
3. Set up **Internal Testing** track (fastest, up to 100 testers)
4. Upload `app-release.aab` to **Internal Testing**
5. Fill store listing:
   - Short description: *Compliance intelligence for AI systems. Map 50+ frameworks across 15 domains.*
   - Full description: See `csoai.org/about`
   - Screenshots: Phone (16:9 or 9:16) + Tablet (16:9 or 4:3)
   - Feature graphic: 1024×500px
   - Privacy policy: `https://csoai.org/privacy`
6. Save → Review release → Start rollout

## Production Release

1. Complete **Content rating** questionnaire
2. Set **Pricing & distribution** → Free, all countries
3. Move from Internal → Closed → Open → Production
4. Each stage requires review (Internal is instant)

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `capacitor.config.ts` not found | Ensure file is at `mobile/capacitor.config.ts` |
| Gradle sync fails | Check Android Studio SDK + JDK versions |
| Keystore not found | Verify path in `build.gradle` matches actual file |
| White screen on launch | Check `webDir` points to built static export |
| Push notifications fail | Add `google-services.json` if using FCM |

---
*CSOAI 33 Moves | Move 31 — Android Capacitor Wrapper*
