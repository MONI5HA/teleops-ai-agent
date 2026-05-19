

https://github.com/user-attachments/assets/ba946da6-dd57-4218-beab-d461410176ed

````md
# 🚀 TeleOps AI Agent

An AI-powered telecom operations assistant built using **LangGraph**, **RAG**, **FastAPI**, and **React**.

This project simulates a real-world Telecom NOC (Network Operations Center) AI system that helps telecom engineers diagnose RAN (Radio Access Network) issues using multi-agent AI orchestration, telecom KPI analysis, alarm monitoring, and knowledge-grounded AI reasoning.

---

# 📌 Project Overview

TeleOps AI Agent is a production-style multi-agent AI platform designed for telecom troubleshooting and network observability workflows.

The system can:

- Analyze telecom network KPIs
- Detect and interpret active alarms
- Retrieve telecom knowledge using RAG
- Diagnose RAN degradation issues
- Recommend corrective actions
- Provide grounded AI responses using telecom documentation

This project demonstrates:

- Agentic AI
- Tool-using agents
- Multi-agent orchestration
- Retrieval-Augmented Generation (RAG)
- FastAPI backend engineering
- Modern React frontend development
- AI observability patterns

---

# 🧠 Core AI Architecture

```text
User Query
    ↓
React Frontend
    ↓
FastAPI Backend
    ↓
LangGraph Orchestrator
    ↓
├── KPI Agent
├── Alarm Agent
├── RAG Agent
    ↓
LLM Reasoning Layer
    ↓
Structured Telecom Diagnosis
````

---

# 🧠 Multi-Agent Workflow

The system uses specialized AI agents collaborating together.

## 📡 KPI Agent

Responsible for:

* Telecom KPI retrieval
* SINR analysis
* RSRP analysis
* Throughput monitoring
* Congestion detection

### Example Metrics

* SINR
* RSRP
* Connected Users
* Throughput

---

## 🚨 Alarm Agent

Responsible for:

* Monitoring active alarms
* Detecting RF interference
* Congestion alerts
* Network degradation alerts

### Example Alarms

* High Interference
* Sector Congestion
* Weak Coverage
* Cell Down

---

## 📚 RAG Agent

Responsible for:

* Telecom document retrieval
* Knowledge-grounded reasoning
* Semantic search using embeddings
* Context injection into AI prompts

The RAG agent retrieves relevant telecom knowledge chunks from vector storage before generating final responses.

---

## 🧠 Orchestrator Agent (LangGraph)

Responsible for:

* Delegating tasks to specialist agents
* Combining outputs
* Producing grounded telecom diagnosis
* Managing workflow execution

---

# 📂 Telecom Documents Used

The system uses telecom-related technical documents for the RAG pipeline.

### Document Categories

* 5G RAN concepts
* LTE optimization
* SINR troubleshooting
* RSRP explanations
* RF interference troubleshooting
* Congestion handling
* Antenna optimization
* Telecom KPI references

---

# 📁 How Documents Are Stored

Documents are stored locally inside:

```text
app/rag/telecom_docs/
```

### Example

```text
app/rag/telecom_docs/
├── sinr_basics.txt
├── rsrp_reference.txt
├── ran_congestion.txt
├── interference_guide.txt
```

---

# 🧠 RAG Pipeline

The project implements a full Retrieval-Augmented Generation pipeline.

## 🔄 RAG Workflow

```text
Telecom Documents
        ↓
Text Chunking
        ↓
Embeddings Generation
        ↓
FAISS Vector Storage
        ↓
Semantic Retrieval
        ↓
Relevant Context Injection
        ↓
LLM Grounded Answer
```

---

# 📦 RAG Components

| Component             | Purpose             |
| --------------------- | ------------------- |
| Sentence Transformers | Generate embeddings |
| FAISS                 | Vector database     |
| Retriever             | Semantic search     |
| Ollama                | Local LLM inference |
| LangGraph             | Agent orchestration |

---

# ⚙️ Tech Stack

## 🖥️ Frontend

* React
* TailwindCSS
* Framer Motion
* Lucide React

---

## ⚙️ Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## 🧠 AI / ML

* LangGraph
* Ollama
* Sentence Transformers
* FAISS
* RAG Pipeline

---

## 🧪 Testing & Observability

* Pytest
* Python Logging
* Structured API responses

---

# 📂 Project Structure

```text
teleops-ai-agent/
│
├── app/
│   │
│   ├── agents/
│   │   ├── kpi_agent.py
│   │   ├── alarm_agent.py
│   │   └── rag_agent.py
│   │
│   ├── graph/
│   │   └── teleops_graph.py
│   │
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   ├── vector_store/
│   │   └── telecom_docs/
│   │
│   ├── api/
│   │   └── server.py
│   │
│   └── ui/
│       └── React Frontend
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

# 🚀 How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd teleops-ai-agent
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\\Scripts\\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download Ollama from:

https://ollama.com/

### Pull LLM Model

```bash
ollama pull llama3
```

### Start Ollama

```bash
ollama serve
```

---

## 5️⃣ Add Telecom Documents

Place telecom documents inside:

```text
app/rag/telecom_docs/
```

---

## 6️⃣ Generate Vector Database

```bash
python app/rag/ingest.py
```

This performs:

* text chunking
* embeddings generation
* FAISS indexing

---

## 7️⃣ Start Backend

```bash
python main.py
```

or

```bash
uvicorn app.api.server:app --reload
```

### Backend URL

```text
http://127.0.0.1:8000
```

### Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## 8️⃣ Start Frontend

```bash
cd frontend
npm install
npm run dev
```

### Frontend URL

```text
http://localhost:5173
```

---

# 🧪 Example Query

## Cell ID

```text
NR-4402
```

## Query

```text
Cell NR-4402 is showing degraded SINR and low throughput.
Analyze the issue and recommend corrective actions.
```

---

# 📊 Example API Response

```json
{
  "status": "success",
  "diagnosis": "The cell is experiencing interference and congestion issues.",

  "root_causes": [
    "RF interference",
    "High traffic congestion"
  ],

  "recommendations": [
    "Check antenna tilt",
    "Perform load balancing"
  ],

  "observability": {
    "kpi": {
      "sinr": "5 dB",
      "throughput": "18 Mbps"
    },

    "alarms": [
      {
        "alarm": "High Interference",
        "severity": "critical"
      }
    ]
  }
}
```

---

# 📈 Observability Features

The project includes:

* Agent execution logs
* KPI traces
* Alarm traces
* API request logging
* Structured responses
* Error handling

This simulates enterprise AI observability workflows.

---

# ☁️ AWS Cloud Compatibility

The architecture is designed to support AWS deployment patterns.

| AWS Service | Purpose                     |
| ----------- | --------------------------- |
| AWS Lambda  | Serverless AI agents        |
| API Gateway | REST API exposure           |
| Amazon S3   | Telecom knowledge storage   |
| CloudWatch  | Logging & monitoring        |
| IAM         | Secure permissions          |
| EC2         | Dedicated inference hosting |
| OpenSearch  | Scalable vector search      |

The system is cloud-portable and deployment-ready.

---

# 🔒 Engineering Practices

This project follows:

* Modular architecture
* Clean code principles
* Typed Python code
* Structured APIs
* Multi-agent separation
* Logging & observability
* Frontend/backend separation

---

# 🎯 Future Improvements

Planned enhancements:

* Docker deployment
* CI/CD pipelines
* AWS deployment
* OpenTelemetry tracing
* Real-time KPI streaming
* Autonomous remediation workflows
* Grafana dashboards
* Multi-LLM routing

---

# 👨‍💻 Author

Built as a hands-on project exploring:

* Agentic AI
* Telecom AI operations
* Multi-agent orchestration
* RAG systems
* AI backend engineering
* Cloud-compatible AI architectures

```
```
