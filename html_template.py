HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MedParser — Medical Report AI Extractor API</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0f172a;
      --card-bg: #1e293b;
      --card-border: #334155;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --accent: #a855f7;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --success: #22c55e;
      --danger: #ef4444;
      --code-bg: #090d16;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2rem 1rem;
    }
    .container {
      max-width: 900px;
      margin: 0 auto;
    }
    header {
      text-align: center;
      margin-bottom: 2.5rem;
    }
    .logo {
      font-size: 3rem;
      margin-bottom: 0.5rem;
    }
    h1 {
      font-size: 2.25rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.75rem;
    }
    .subtitle {
      color: var(--text-muted);
      font-size: 1.1rem;
      max-width: 650px;
      margin: 0 auto 1.5rem;
    }
    .badges {
      display: flex;
      justify-content: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }
    .badge {
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      color: var(--primary);
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 500;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 1.5rem;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    .card-title {
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
    }
    .step-item {
      background: rgba(15, 23, 42, 0.5);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 1rem;
    }
    .step-num {
      display: inline-block;
      width: 24px;
      height: 24px;
      background: var(--primary);
      color: #000;
      font-weight: bold;
      border-radius: 50%;
      text-align: center;
      line-height: 24px;
      font-size: 0.85rem;
      margin-bottom: 0.5rem;
    }
    .step-title {
      font-weight: 600;
      margin-bottom: 0.25rem;
    }
    .step-desc {
      font-size: 0.875rem;
      color: var(--text-muted);
    }
    pre {
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 1rem;
      overflow-x: auto;
      font-family: 'Fira Code', monospace;
      font-size: 0.875rem;
      color: #e2e8f0;
      margin-top: 0.5rem;
    }
    code {
      font-family: 'Fira Code', monospace;
      background: rgba(255, 255, 255, 0.1);
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
      font-size: 0.85em;
    }
    .btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: var(--primary);
      color: #000;
      font-weight: 600;
      padding: 0.65rem 1.25rem;
      border-radius: 8px;
      text-decoration: none;
      border: none;
      cursor: pointer;
      transition: background 0.2s ease;
      font-size: 0.95rem;
    }
    .btn:hover { background: var(--primary-hover); color: #fff; }
    .btn-secondary {
      background: transparent;
      border: 1px solid var(--card-border);
      color: var(--text);
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--text-muted);
    }
    .form-group {
      margin-bottom: 1rem;
    }
    label {
      display: block;
      font-size: 0.875rem;
      font-weight: 500;
      margin-bottom: 0.35rem;
      color: var(--text-muted);
    }
    input[type="text"], input[type="password"], select, input[type="file"] {
      width: 100%;
      padding: 0.65rem 0.85rem;
      background: var(--code-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      color: var(--text);
      font-family: inherit;
      font-size: 0.9rem;
    }
    input:focus, select:focus {
      outline: none;
      border-color: var(--primary);
    }
    .actions {
      display: flex;
      gap: 1rem;
      margin-top: 1.5rem;
    }
    footer {
      text-align: center;
      margin-top: 3rem;
      color: var(--text-muted);
      font-size: 0.85rem;
    }
    footer a { color: var(--primary); text-decoration: none; }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">🩺</div>
      <h1>MedParser API</h1>
      <p class="subtitle">Extract structured lab tests, biomarkers, and patient details from medical reports using Google Gemini AI.</p>
      <div class="badges">
        <span class="badge">FastAPI</span>
        <span class="badge">Gemini 3.6 Flash</span>
        <span class="badge">Header-based Auth</span>
        <span class="badge">PDF & Image Support</span>
      </div>
    </header>

    <div class="card">
      <h2 class="card-title">📖 API Quick Reference</h2>
      <div class="grid">
        <div class="step-item">
          <div class="step-num">1</div>
          <div class="step-title">Supply Credentials</div>
          <div class="step-desc">Pass your <code>X-Gemini-Api-Key</code> & <code>X-Gemini-Model</code> headers with every request.</div>
        </div>
        <div class="step-item">
          <div class="step-num">2</div>
          <div class="step-title">Upload File</div>
          <div class="step-desc">Send PDF, JPEG, PNG, WEBP, or HEIC files (up to 15MB) via multipart form-data.</div>
        </div>
        <div class="step-item">
          <div class="step-num">3</div>
          <div class="step-title">Structured JSON</div>
          <div class="step-desc">Receive patient details, test values, reference ranges, and flagged abnormal results.</div>
        </div>
      </div>
      <div class="actions">
        <a href="/docs" class="btn" target="_blank">🚀 Open Swagger API Docs</a>
        <a href="/health" class="btn btn-secondary" target="_blank">💓 Health Check Endpoint</a>
      </div>
    </div>

    <div class="card">
      <h2 class="card-title">💻 Example Request (cURL)</h2>
      <pre><code>curl -X POST "https://your-domain.com/extract" \\
  -H "accept: application/json" \\
  -H "X-Gemini-Api-Key: YOUR_GEMINI_API_KEY" \\
  -H "X-Gemini-Model: gemini-3.6-flash" \\
  -F "file=@/path/to/medical_report.pdf"</code></pre>
    </div>

    <div class="card">
      <h2 class="card-title">🧪 Try It Live</h2>
      <form id="extractForm">
        <div class="grid">
          <div class="form-group">
            <label for="apiKey">Gemini API Key</label>
            <input type="password" id="apiKey" placeholder="AIzaSy..." required>
          </div>
          <div class="form-group">
            <label for="model">Gemini Model</label>
            <select id="model">
              <option value="gemini-3.6-flash" selected>gemini-3.6-flash (Recommended)</option>
              <option value="gemini-1.5-flash">gemini-1.5-flash</option>
              <option value="gemini-1.5-pro">gemini-1.5-pro</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label for="file">Medical Report File (PDF or Image)</label>
          <input type="file" id="file" accept=".pdf,.png,.jpg,.jpeg,.webp,.heic,.heif" required>
        </div>
        <button type="submit" class="btn" id="submitBtn">✨ Extract Data</button>
      </form>
      <div id="outputContainer" style="display: none; margin-top: 1.5rem;">
        <label>Extraction Result:</label>
        <pre><code id="jsonOutput">Parsing document...</code></pre>
      </div>
    </div>

    <footer>
      MedParser API • Powered by FastAPI & Google Gemini • <a href="https://github.com/devded/medparser" target="_blank">GitHub Repository</a>
    </footer>
  </div>

  <script>
    document.getElementById('extractForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const apiKey = document.getElementById('apiKey').value.trim();
      const model = document.getElementById('model').value;
      const fileInput = document.getElementById('file');
      const submitBtn = document.getElementById('submitBtn');
      const outputContainer = document.getElementById('outputContainer');
      const jsonOutput = document.getElementById('jsonOutput');

      if (!apiKey || fileInput.files.length === 0) {
        alert('Please provide your Gemini API key and select a medical report file.');
        return;
      }

      const formData = new FormData();
      formData.append('file', fileInput.files[0]);

      submitBtn.disabled = true;
      submitBtn.innerText = '⏳ Extracting...';
      outputContainer.style.display = 'block';
      jsonOutput.innerText = 'Sending document to Gemini API...';

      try {
        const response = await fetch('/extract', {
          method: 'POST',
          headers: {
            'X-Gemini-Api-Key': apiKey,
            'X-Gemini-Model': model
          },
          body: formData
        });
        const data = await response.json();
        jsonOutput.innerText = JSON.stringify(data, null, 2);
      } catch (err) {
        jsonOutput.innerText = 'Error: ' + err.message;
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = '✨ Extract Data';
      }
    });
  </script>
</body>
</html>
"""
