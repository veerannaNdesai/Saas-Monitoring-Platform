# 🟢 SaaS Uptime Monitoring Platform

A production-ready, full-stack uptime monitoring platform that tracks **availability, response status, and response time** across 50+ endpoints. Built with **FastAPI**, **PostgreSQL**, **React.js**, **JWT authentication**, and a **Docker** development environment — architected to handle thousands of health-check executions per day.

---

## 🚀 Live Demo

> _Coming soon / Add your deployed link here_

---

## 🖼️ Screenshots

> _Add screenshots of your dashboard, monitor list, and status views here_

---

## ✨ Features

- 🔁 **Continuous Health Checks** — Configurable check intervals from 1 to 30 minutes per endpoint
- 📊 **Real-Time Dashboard** — React.js UI showing live UP / DOWN / PENDING status for all monitored endpoints
- 📈 **Historical Records** — PostgreSQL-backed check history for availability trends and response time analysis
- 🔐 **JWT Authentication** — Secure multi-user access with token-based auth; each user owns and manages their own monitors
- 🐳 **Dockerized Dev Environment** — Full Docker setup for consistent local development and easy onboarding
- ⚡ **Fast API Layer** — FastAPI backend built for high-throughput, capable of thousands of health-check executions per day
- 👥 **Multi-User Ownership** — Secure monitor isolation; users can only view and manage their own endpoints

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| Frontend | React.js |
| Database | PostgreSQL |
| Auth | JWT (JSON Web Tokens) |
| DevOps | Docker, Docker Compose |
| API | RESTful (JSON) |

---

## 📁 Project Structure

```
saas-monitoring-platform/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entrypoint
│   │   ├── routers/
│   │   │   ├── auth.py          # JWT login & registration routes
│   │   │   ├── monitors.py      # CRUD routes for endpoints
│   │   │   └── checks.py        # Health check history routes
│   │   ├── models/              # SQLAlchemy ORM models
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   ├── services/
│   │   │   └── checker.py       # Health check scheduler & executor
│   │   └── database.py          # PostgreSQL connection setup
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/          # StatusBadge, MonitorCard, Dashboard
│   │   ├── pages/               # Login, Register, Dashboard, Monitor Detail
│   │   ├── api/                 # Axios interceptors & API calls
│   │   └── App.js
│   └── package.json
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- Node.js 16+
- Docker & Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/veerannaNdesai/Saas-Monitoring-Platform.git
cd Saas-Monitoring-Platform
```

### 2. Run with Docker (Recommended)

```bash
docker-compose up --build
```

This spins up the FastAPI backend, PostgreSQL database, and React frontend together.

- Frontend: `http://localhost:3000`
- API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

### 3. Manual Setup (Without Docker)

**Backend:**
```bash
cd backend
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL=postgresql://user:password@localhost/monitoring_db
export SECRET_KEY=your_jwt_secret_key

# Run migrations & start server
alembic upgrade head
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

---

## 📡 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Create a new user account |
| `POST` | `/auth/login` | Login and receive JWT tokens |

### Monitors
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/monitors/` | List all monitors for the authenticated user |
| `POST` | `/monitors/` | Create a new endpoint monitor |
| `GET` | `/monitors/{id}` | Get monitor details |
| `PUT` | `/monitors/{id}` | Update monitor settings |
| `DELETE` | `/monitors/{id}` | Delete a monitor |

### Health Checks
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/monitors/{id}/checks` | Get historical check records for a monitor |
| `POST` | `/monitors/{id}/check` | Trigger an immediate health check |

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=postgresql://user:password@localhost/monitoring_db
SECRET_KEY=your_super_secret_jwt_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
CHECK_INTERVAL_DEFAULT=5
```

---

## 📦 Key Dependencies

```txt
# Backend
fastapi
uvicorn
sqlalchemy
alembic
psycopg2-binary
python-jose[cryptography]   # JWT
passlib[bcrypt]             # Password hashing
httpx                       # Async HTTP health checks
apscheduler                 # Health check scheduler

# Frontend
react
axios
react-router-dom
```

---

## 🏗️ Architecture Overview

```
React Frontend  ──►  FastAPI Backend  ──►  PostgreSQL
                          │
                     APScheduler
                     (Background Jobs)
                          │
                    Health Check Worker
                    (HTTP requests to monitored endpoints)
```

- The **APScheduler** background job runs health checks at each monitor's configured interval
- Results (status code, latency, UP/DOWN) are stored in PostgreSQL
- The React dashboard polls the API to display real-time status

---

## 🔮 Future Improvements

- [ ] Email / Slack alert notifications on downtime
- [ ] SSL certificate expiry monitoring
- [ ] Response body assertions (keyword matching)
- [ ] Incident log and downtime history reports
- [ ] Public status page per user

---

## 👨‍💻 Author

**Veeranna N Desai**  
Python Full Stack Developer | Bangalore, Karnataka  
📧 iveerannadesai@gmail.com  
🔗 [GitHub](https://github.com/veerannaNdesai) · [LinkedIn](https://linkedin.com/in/veeranna-desai)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
