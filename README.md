# MedParser 🩺

A high-performance FastAPI service that automatically extracts structured medical report data, lab test results, biomarkers, and clinical metadata from medical documents (PDFs & images) using Google Gemini AI.

---

## ✨ Features

- 📑 **Multi-Format Parsing**: Supports PDFs, JPEG, PNG, WebP, and HEIC images.
- 🧬 **Structured JSON Extraction**: Extracts patient metadata, lab name, doctor info, test names, values, units, reference ranges, and test categories.
- ⚠️ **Abnormal Value Detection**: Automatically flags out-of-range test values.
- 📝 **Clinical Summarization**: Generates brief summaries of key medical findings.
- ⚡ **Fast & Asynchronous**: Powered by FastAPI and asynchronous Gemini client API.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) + Uvicorn
- **AI Model**: Google Gemini API (`google-genai`)
- **Data Validation**: Pydantic v2
- **Runtime**: Python 3.10+

---

## 🚀 Quick Start

### 1. Clone & Setup Virtual Environment

```bash
git clone https://github.com/devded/medparser.git
cd medparser

python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

The server holds no configuration of its own — no `.env` file needed. Every caller supplies their
own Gemini API key and model per request via the `X-Gemini-Api-Key` and `X-Gemini-Model` headers
(see below), and CORS is open to any origin.

### 3. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

---

## 📡 API Endpoints

### `GET /health`

Returns service status and the headers required to call `/extract`.

**Example response:**

```json
{
  "status": "online",
  "required_headers": ["X-Gemini-Api-Key", "X-Gemini-Model"]
}
```

### `POST /extract`

Upload a medical report (PDF or image — JPEG, PNG, WEBP, or HEIC) to extract structured JSON data.

**Request:**
- Content-Type: `multipart/form-data`
- Headers:
  - `X-Gemini-Api-Key` (**required**) — your own Gemini API key
  - `X-Gemini-Model` (**required**) — the Gemini model to use, e.g. `gemini-3.6-flash`
- Body: `file` (PDF or image binary, up to 15MB)

**Example with cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/extract" \
  -H "accept: application/json" \
  -H "X-Gemini-Api-Key: YOUR_GEMINI_API_KEY" \
  -H "X-Gemini-Model: gemini-3.6-flash" \
  -F "file=@/path/to/medical_report.pdf"
```

Omitting `X-Gemini-Api-Key` returns `401 Unauthorized`; omitting `X-Gemini-Model` returns `400 Bad Request`.

**Example response:**

```json
{
  "success": true,
  "model_used": "gemini-3.6-flash",
  "data": {
    "patient_name": "Jane Doe",
    "patient_id": null,
    "date": "2026-07-18",
    "lab_name": "Apex Health Diagnostics",
    "doctor_name": "Dr. Emily Taylor",
    "clinical_summary": "...",
    "tests": [
      {
        "name": "Hemoglobin",
        "value": "11.2",
        "unit": "g/dL",
        "reference_range": "13.5 - 17.5",
        "is_abnormal": true,
        "category": "Hematology"
      }
    ]
  }
}
```

---

## 📄 License

MIT License
