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

### 3. Configure Environment Variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.6-flash
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

---

## 📡 API Endpoints

### `GET /health`

Returns service status, the configured Gemini model, and whether an API key is set.

**Example response:**

```json
{
  "status": "online",
  "model": "gemini-3.6-flash",
  "api_key_configured": true
}
```

### `POST /extract`

Upload a medical report (PDF or image — JPEG, PNG, WEBP, or HEIC) to extract structured JSON data.

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (PDF or image binary, up to 15MB)

**Example with cURL:**

```bash
curl -X POST "http://127.0.0.1:8000/extract" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/medical_report.pdf"
```

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
