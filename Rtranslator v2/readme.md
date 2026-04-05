# 🌐 RTranslator

<div align="center">

![RTranslator Banner](https://img.shields.io/badge/RTranslator-v2.0-00e5b0?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTUgOGw2IDYiLz48cGF0aCBkPSJNNCAxNGw2LTYgMi0zIi8+PHBhdGggZD0iTTIgNWgxMiIvPjxwYXRoIGQ9Ik03IDJoMSIvPjxwYXRoIGQ9Ik0yMiAyMmwtNS0xMC01IDEwIi8+PHBhdGggZD0iTTE0IDE4aDYiLz48L3N2Zz4=)
![License](https://img.shields.io/badge/License-MIT-3d8bff?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-16%2B-00e5b0?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Claude%20Sonnet-purple?style=for-the-badge)

**Real-time voice & text translation across 16+ languages — powered by Claude AI**  
Works offline in Demo Mode · No server required · Privacy-first

[Try the App](#-quick-start) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 **Text Translation** | Type or paste text → instant AI translation with copy, share & TTS |
| 🎙️ **Voice Input (STT)** | Speak in your language via Web Speech API (Chrome/Edge) |
| 🔊 **Text-to-Speech** | Hear translations spoken aloud via browser TTS |
| 💬 **Conversation Mode** | Bidirectional chat with per-message translation bubbles |
| 📻 **Walkie-Talkie Mode** | Turn-based voice translation — tap to speak, auto-translates for the other person |
| 📋 **History** | All translations saved locally; tap to reload any item |
| 🌙 **Dark Theme** | Fully dark, mobile-first UI |
| 🔒 **Privacy-First** | No backend, no logging, API key stays in your browser |

---

## 🌍 Supported Languages

🇬🇧 English · 🇪🇸 Spanish · 🇫🇷 French · 🇩🇪 German · 🇮🇹 Italian · 🇵🇹 Portuguese  
🇨🇳 Chinese · 🇯🇵 Japanese · 🇰🇷 Korean · 🇸🇦 Arabic · 🇷🇺 Russian · 🇮🇳 Hindi  
🇹🇷 Turkish · 🇳🇱 Dutch · 🇵🇱 Polish · 🇺🇦 Ukrainian

---

## 🚀 Quick Start

### Option A — Open directly (no install needed)

1. Download `RTranslator.html`
2. Open it in **Chrome** or **Edge** (for full STT/TTS support)
3. On first launch, enter your [Anthropic API key](https://console.anthropic.com) — or use **Demo Mode** to try it without a key

### Option B — Serve locally

```bash
git clone https://github.com/YOUR_USERNAME/RTranslator.git
cd RTranslator
# Serve with any static server, e.g.:
python3 -m http.server 8080
# Then open http://localhost:8080/RTranslator.html
```

### Option C — Deploy to GitHub Pages

1. Push the repo to GitHub
2. Go to **Settings → Pages → Source → main branch**
3. Your app will be live at `https://YOUR_USERNAME.github.io/RTranslator/RTranslator.html`

---

## 🔑 API Key Setup

RTranslator uses the [Anthropic Claude API](https://console.anthropic.com) for AI translation.

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Create an API key (free tier available)
3. Open RTranslator, tap the 🔑 icon, and paste your key
4. Your key is stored **only in your browser's localStorage** — never sent to any server other than `api.anthropic.com`

> ⚠️ **Security warning:** Do NOT share the HTML file after entering your API key.  
> The key is stored in localStorage on *your device only*, but clear it before sharing the file.  
> See [SECURITY.md](SECURITY.md) for full details.

---

## 🏗️ Architecture

```
RTranslator (Single HTML file — no build step)
│
├── 📝 Text Mode        → textarea → Claude API → output + TTS
├── 💬 Conversation     → chat UI → per-message Claude translation
├── 📻 Walkie-Talkie    → Web Speech API → Claude → SpeechSynthesis
├── 📋 History          → localStorage (browser-only)
└── ⚙️  Settings        → prefs in localStorage, key in localStorage
```

**Stack:**
- Pure HTML + CSS + Vanilla JS (zero dependencies, zero npm)
- [Claude Sonnet](https://anthropic.com) for translation
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) for STT
- [SpeechSynthesis API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis) for TTS
- localStorage for persistence

---

## 🔒 Privacy & Security

- ✅ **No backend server** — the app is a single static HTML file
- ✅ **No analytics or tracking** — zero third-party scripts at runtime
- ✅ **API key masked** in UI — only the last 4 characters are ever displayed
- ✅ **Input sanitization** — all user-generated content is escaped before rendering
- ✅ **Content Security Policy** — meta CSP tag restricts connections to Anthropic only
- ✅ **API key format validated** before saving (`sk-ant-...` pattern)
- ✅ **Rate limit errors** handled gracefully — no key exposed in error messages
- ✅ **History stays local** — localStorage only, never transmitted

See [SECURITY.md](SECURITY.md) for the full security model and responsible disclosure policy.

---

## 📂 Repository Structure

```
RTranslator/
├── RTranslator.html      # Main app (self-contained)
├── README.md             # This file
├── SECURITY.md           # Security policy
├── LICENSE               # MIT License
└── .gitignore            # Ignores secrets and temp files
```

---

## 🗺️ Roadmap

- [ ] OCR — translate text in images
- [ ] Custom phrase dictionary
- [ ] Conversation recording & export
- [ ] Auto language detection
- [ ] PWA / installable app (manifest + service worker)
- [ ] Offline model via WebAssembly (Whisper.cpp)
- [ ] Multi-participant Bluetooth (Nearby Connections API)
- [ ] Android APK via Capacitor/WebView wrapper

---

## 🤝 Contributing

Contributions welcome! Please read the guidelines before submitting a PR.

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit: `git commit -m 'feat: add my feature'`
4. Push: `git push origin feat/my-feature`
5. Open a Pull Request

---


## 🙏 Credits

- Translation powered by [Anthropic Claude](https://anthropic.com)
- Speech recognition via [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- Inspired by the [RTranslator Android app](https://github.com/niedev/RTranslator)
- UI fonts: [Syne](https://fonts.google.com/specimen/Syne) + [Inter](https://fonts.google.com/specimen/Inter)

---

<div align="center">
Made with ❤️ · <a href="https://console.anthropic.com">Get your API key</a>
</div>
