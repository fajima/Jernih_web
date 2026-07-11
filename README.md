# 🧠 JERNIH — AI Civic Operating System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red.svg">
  <img src="https://img.shields.io/badge/AI-RAG%20System-purple.svg">
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
</p>

<h3 align="center">
"Informasi yang Terang, Bukan yang Bising"
</h3>

<p align="center">
JERNIH adalah platform <b>AI Civic Assistant</b> yang dirancang untuk membantu masyarakat Indonesia mengakses layanan publik, memverifikasi informasi, memahami kebijakan, dan mengambil keputusan berbasis data melalui teknologi <b>Artificial Intelligence</b> dan <b>Retrieval-Augmented Generation (RAG)</b>.
</p>

---

# 📌 Tentang Proyek

Di era banjir informasi, masyarakat sering mengalami kesulitan dalam:

- Menemukan informasi layanan publik yang valid.
- Memastikan kebenaran berita yang beredar.
- Memahami dampak kebijakan pemerintah.
- Menentukan langkah yang harus dilakukan.
- Mengakses dokumen resmi dengan cepat.

**JERNIH hadir sebagai solusi berbasis AI** yang mampu memberikan informasi yang transparan, akurat, dan mudah dipahami.

---

# ✨ Fitur Utama

| Fitur | Deskripsi |
|--------|--------|
| 🤖 AI Civic Copilot | Asisten AI untuk konsultasi layanan publik |
| 🔍 Hoax Checker | Verifikasi berita dan deteksi hoaks |
| 📋 Action Plan Generator | Rekomendasi langkah berdasarkan kondisi pengguna |
| 📊 Policy Simulator | Simulasi dampak suatu kebijakan |
| 🧠 Knowledge Graph | Visualisasi hubungan antar kebijakan dan program |
| 📸 Smart Scanner | Analisis dokumen dan gambar |
| 🗺️ Predictive Map | Prediksi dan pemetaan data |
| 🌐 Multi-language | Mendukung Bahasa Indonesia dan Inggris |

---

# 🏗️ Arsitektur Sistem

```text
                    ┌──────────────────────┐
                    │      Pengguna        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Streamlit UI     │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼

      ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
      │ Civic Agent    │ │ Hoax Agent     │ │ Policy Agent   │
      └────────────────┘ └────────────────┘ └────────────────┘

                               │
                               ▼

                 ┌──────────────────────────┐
                 │      RAG Engine           │
                 │ (ChromaDB + Embedding)   │
                 └──────────┬───────────────┘
                            │
                            ▼

              ┌───────────────────────────────┐
              │ Dokumen & Basis Pengetahuan   │
              └───────────────────────────────┘
```

---

# 🛠️ Teknologi yang Digunakan

## Frontend

- Streamlit
- HTML & CSS
- Custom UI Components

## Backend

- Python
- ChromaDB
- Retrieval-Augmented Generation (RAG)

## Artificial Intelligence

- OpenAI API
- OpenRouter
- Groq API
- Embedding Model

## Data Source

- Program Indonesia Pintar
- Kartu Indonesia Sehat
- Bantuan Sosial PKH
- Dukcapil
- DTKS

---

# 📂 Struktur Proyek

```text
JERNIH/

├── streamlit_app/
│
├── app.py
├── requirements.txt
├── packages.txt
│
├── src/
│   ├── agents.py
│   ├── ai_service.py
│   ├── config.py
│   ├── fallback.py
│   ├── knowledge_base.py
│   ├── models.py
│   ├── pages.py
│   ├── rag_engine.py
│   ├── ui_components.py
│   └── utils.py
│
├── pages/
│   ├── 06_Smart_Scanner.py
│   ├── 07_Predictive_Map.py
│   └── 08_About.py
│
├── data/
│   ├── documents/
│   └── chroma_db/
│
└── README.md
```

---

# 🚀 Cara Menjalankan

## 1. Clone Repository

```bash
git clone https://github.com/username/jernih.git
cd jernih/streamlit_app
```

---

## 2. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 3. Konfigurasi API

Buat file:

```text
.streamlit/secrets.toml
```

Isi:

```toml
OPENAI_API_KEY = "your_api_key"
GROQ_API_KEY = "your_groq_key"
```

---

## 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```text
http://localhost:8501
```

---

# 🧠 Keunggulan JERNIH

✅ Transparansi sumber informasi.

✅ Sistem berbasis RAG untuk mengurangi halusinasi AI.

✅ Confidence score pada setiap jawaban.

✅ Desain modern dan responsif.

✅ Mendukung multi-bahasa.

✅ Mudah dikembangkan.

✅ Fokus pada kebutuhan masyarakat Indonesia.

---

# 🎯 Implementasi SDGs

JERNIH mendukung beberapa tujuan Sustainable Development Goals (SDGs):

- SDG 4 — Pendidikan Berkualitas.
- SDG 10 — Mengurangi Kesenjangan.
- SDG 11 — Kota dan Komunitas Berkelanjutan.
- SDG 16 — Perdamaian, Keadilan, dan Kelembagaan yang Tangguh.

---

# 🏆 Potensi Pengembangan

- Integrasi data pemerintah secara real-time.
- Chatbot berbasis suara.
- Aplikasi mobile Android/iOS.
- Dashboard analitik nasional.
- Integrasi dengan layanan Dukcapil dan BPJS.

---

# 👥 Tim Pengembang

**JERNIH Team**

AI Civic Operating System for Indonesia 🇮🇩

> "Informasi yang Terang, Bukan yang Bising."

---

# 📄 Lisensi

Proyek ini menggunakan lisensi **MIT License**.

---

<p align="center">
Made with ❤️ for LKS 2026
</p>
