<div align="center">

# 🔍 VisionVault

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=Semantic+image+search+for+your+machine;Powered+by+Gemini+%2B+ChromaDB;Search+your+photos+with+plain+English" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gemini](https://img.shields.io/badge/Gemini-Embeddings-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6B6B?style=for-the-badge)](https://www.trychroma.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Privacy](https://img.shields.io/badge/Privacy-First-8B5CF6?style=for-the-badge&logo=shield&logoColor=white)]()

<br/>

> **Search your local image library with plain English.**
> Powered by Gemini multimodal embeddings & ChromaDB — delivered as a single Jupyter notebook.

<br/>

<!-- 🎬 DEMO GIF INSTRUCTIONS:
     1. Record your screen with ScreenToGif (Windows): https://www.screentogif.com/
        OR Kap (macOS): https://getkap.co/
        OR peek (Linux): https://github.com/phw/peek
     2. Record: run index_dir() → then search_images("your query") → show results
     3. Save as demo.gif and drop it in this repo
     4. Replace the line below with: <img src="demo.gif" .../>
-->

</div>

---

## 💡 What Can You Search?

```
"sunset over mountains"        →   finds your best landscape shots
"birthday cake with candles"   →   finds that party photo from 2022
"whiteboard diagram"           →   finds your meeting notes photo
"dog at the beach"             →   finds every beach trip with your dog
"receipt or invoice"           →   finds scanned documents instantly
```

> No more guessing filenames. Just describe what you remember.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🧠 Multimodal AI Search
Uses Google's Gemini embedding model to **understand the actual content** of your images — not just filenames or tags.

</td>
<td width="50%">

### 🔒 Maximum Privacy
No absolute paths ever stored. Your images are identified by **SHA-256 content hashes** only — nothing traceable back to your folder structure.

</td>
</tr>
<tr>
<td width="50%">

### 💾 Persistent Global Index
Database lives at `~/.visionvault` on your machine. Index once, search forever — **survives reboots**.

</td>
<td width="50%">

### ⚡ Fast & Efficient
Large images are **auto-resized to 1024px** before embedding, keeping API calls fast and payloads small.

</td>
</tr>
<tr>
<td width="50%">

### 🌐 Wide Format Support
Supports `.png` `.jpg` `.jpeg` `.webp` `.gif` `.bmp` out of the box.

</td>
<td width="50%">

### 🔁 Incremental Indexing
Already-indexed images are **automatically skipped** — only new files are processed on re-runs.

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Step 1 — Get a Gemini API Key

Get your **free** key at [Google AI Studio](https://aistudio.google.com/) then set it as an environment variable:

```bash
# macOS / Linux
export GEMINI_API_KEY="your-gemini-api-key"
```

```powershell
# Windows (PowerShell)
$env:GEMINI_API_KEY="your-gemini-api-key"
```

> ⚠️ **Never paste your real API key into the notebook or README.**

<br/>

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

<br/>

### Step 3 — Launch the Notebook

```bash
jupyter notebook visionvault.ipynb
```

---

## 🗂️ Usage

### 📁 Index a Folder

```python
# macOS / Linux
index_dir("/Users/yourname/Pictures")

# Windows
index_dir(r"D:\Pictures")
```

Call `index_dir()` on as many folders as you want — all results go into the **same global database** and duplicates are skipped automatically.

<br/>

### 🔍 Search Your Images

```python
results = search_images("sunglasses on a beach", k=5)

for i, r in enumerate(results, 1):
    label = r.get("name") or r["id"]
    print(f"{i}. [{r['score']:.3f}] {label}")
```

Results include a **relevance score** (0–1) and the **filename** — no absolute paths, ever.

---

## 🔐 Privacy & Security

<div align="center">

| What | How VisionVault Handles It |
|---|---|
| 📂 File paths | **Never stored** — SHA-256 hash used as ID instead |
| ☁️ Cloud sync | **None** — database stays 100% on your machine |
| 🔑 API key | **Environment variable only** — never in code or files |
| 📓 Notebook output | **Clear before pushing** — `Kernel → Restart & Clear Output` |
| 🗄️ Database location | `~/.visionvault` — outside your repo, never committed |

</div>

---

## 📦 Dependencies

```
chromadb    — local vector database
requests    — API communication
numpy       — vector math
pillow      — image resizing
certifi     — SSL certificates
```

---

## 📁 Project Structure

```
visionvault/
├── 📓 visionvault.ipynb   ← the entire app — one notebook
├── 📋 requirements.txt    ← Python dependencies
├── 🚫 .gitignore          ← keeps secrets & caches out of Git
└── 📖 README.md           ← you are here

~/.visionvault/            ← your private image index (NOT in this repo)
```

---

## 💡 Tips & Tricks

- 🗂️ **Index multiple folders** — call `index_dir()` multiple times, everything lands in one global DB
- 🔄 **Re-index anytime** — only new images are processed, existing ones are skipped
- 🗣️ **Use broad natural language** — `"dog running outside"` works better than `"IMG_4821.jpg"`
- 📊 **Minimum score is 0.15** — results below this threshold are filtered out automatically
- 🧹 **Always clear outputs** before committing — run `Kernel → Restart & Clear Output`

---

<div align="center">

**Built with**

[![Gemini](https://img.shields.io/badge/Gemini-AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square)](https://www.trychroma.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

*If you find this useful, give it a ⭐ on GitHub!*

</div>
