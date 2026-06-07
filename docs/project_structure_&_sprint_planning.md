# Project Structure & Sprint Planning
## SaaS Monitoring Platform

---

## 1. Core Architectural Principle

> [!NOTE]
> **Separation of Concerns:** Think of your codebase like a professional company. You do not place HR, Finance, Engineering, and Marketing into the same room. Likewise, database models, API routing, authentication mechanics, and core business logic should reside in distinct, dedicated layers—not packed into a single script.

---

## 2. Directory Layouts

### 2.1 Backend Project Directory (`backend/`)
For our **FastAPI** backend service, we utilize a modular, service-oriented architecture:

```text
backend/
└── app/
    ├── main.py                  # Service entry point and application initialization
    ├── api/                     # HTTP router controllers (endpoint paths only)
    │   ├── auth.py
    │   ├── monitors.py
    │   ├── dashboard.py
    │   └── alerts.py
    ├── core/                    # Security configurations and global dependency injectables
    │   ├── config.py
    │   ├── security.py
    │   └── dependencies.py
    ├── db/                      # Database engine connections and session managers
    │   ├── database.py
    │   └── session.py
    ├── models/                  # Database relational schema entities (SQLAlchemy models)
    │   ├── user.py
    │   ├── monitor.py
    │   ├── monitor_log.py
    │   └── alert.py
    ├── schemas/                 # Data validation and serialization envelopes (Pydantic models)
    │   ├── auth.py
    │   ├── monitor.py
    │   ├── dashboard.py
    │   └── alert.py
    ├── services/                # Business logic layer (computations, DB writing, triggers)
    │   ├── auth_service.py
    │   ├── monitor_service.py
    │   ├── dashboard_service.py
    │   ├── alert_service.py
    │   └── monitoring_service.py
    ├── scheduler/               # Concurrency check runner (monitoring engine)
    │   └── scheduler.py
    ├── utils/                   # Reusable auxiliary utilities
    │   ├── email.py
    │   └── logger.py
    └── tests/                   # Integration and unit tests
```

#### **Backend Component Roles:**
* 📂 **`api/` (Routing Layer):** Handles incoming HTTP requests and structures HTTP responses. It performs basic parameter parsing and delegates calculations directly to the service layer.
  * *Best Practice:* Routes should remain extremely thin.
  * 🔴 *Bad:* Placing 100 lines of query logic directly inside a route definition.
  * 🟢 *Good:* Route calls `monitor_service.create_monitor(db, payload)`.
* 📂 **`services/` (Business Logic Layer):** The functional engine of the app. This isolates calculation steps, state transactions, and notification triggers from the web framework itself.
* 📂 **`models/` (Relational Models):** Declares SQLAlchemy classes representing tables, indexes, and primary/foreign key mappings.
* 📂 **`schemas/` (Validation Layer):** Holds Pydantic validation types which dictate strict inputs, type validation, and serialize responses (filtering sensitive details).
* 📂 **`scheduler/` (Automation Layer):** Coordinates background operations (checks) via standard library timers or dedicated schedulers.
* 📂 **`utils/` (Helper Layer):** Reusable utilities like system logging setups and mail-dispatch clients.

---

### 2.2 Frontend Project Directory (`frontend/`)
For our **React** client application, components are organized by functional boundaries:

```text
frontend/
└── src/
    ├── App.jsx                  # Main component declaring routes & providers
    ├── components/              # Globally reusable visual UI elements
    │   ├── Navbar.jsx
    │   ├── MonitorCard.jsx
    │   └── Chart.jsx
    ├── context/                 # Global state providers
    │   └── AuthContext.jsx
    ├── hooks/                   # Custom React utility hooks
    ├── pages/                   # Complete viewport view containers
    │   ├── Login.jsx
    │   ├── Register.jsx
    │   ├── Dashboard.jsx
    │   └── Monitors.jsx
    ├── routes/                  # Protected and public routing paths definitions
    └── services/                # Backend API connectors and axios handlers
        └── api.js
```

---

## 3. Development Roadmap (Sprint Plan)

To build this systematically, we follow a modular **8-Sprint Development Plan**:

```mermaid
gantt
    title SaaS Monitor Development Timeline
    dateFormat  X
    axisFormat %d
    
    section Foundation
    Sprint 1: Base Setup           :active, s1, 0, 10
    Sprint 2: Authentication       :s2, after s1, 10d
    section Core Backend
    Sprint 3: Monitor CRUD         :s3, after s2, 10d
    Sprint 4: Monitoring Scheduler :s4, after s3, 10d
    Sprint 5: Dashboard Analytics  :s5, after s4, 10d
    section Frontend & Integration
    Sprint 6: React UI Client      :s6, after s5, 10d
    Sprint 7: Alerts & Notifications:s7, after s6, 10d
    section Deployment
    Sprint 8: Production Release   :s8, after s7, 10d
```

---

### **Sprint 1: Repository & Base Infrastructure Setup**
* **Goal:** Initialize workspace and database connectors.
* 📋 **Tasks:**
  - [ ] Initialize git repository.
  - [ ] Bootstrap FastAPI project scaffolding.
  - [ ] Setup PostgreSQL database container.
  - [ ] Initialize Alembic for database migrations.
  - [ ] Standardize environment configurations (`.env`).
* 📦 **Deliverable:** FastAPI running and successfully executing test connections to PostgreSQL.

---

### **Sprint 2: Authentication & User Management**
* **Goal:** Implement secure user registration and login routines.
* 📋 **Tasks:**
  - [ ] Define the database `User` schema model.
  - [ ] Implement password hashing logic.
  - [ ] Code the registration API endpoint (`POST /auth/register`).
  - [ ] Code the session login API endpoint (`POST /auth/login`).
  - [ ] Setup JWT authentication middleware check.
* 📦 **Deliverable:** Secure registration and login flow returning standard JWT access tokens.

---

### **Sprint 3: Monitor Configuration Management (CRUD)**
* **Goal:** Allow users to define target websites to monitor.
* 📋 **Tasks:**
  - [ ] Define the `Monitor` model and table relationships.
  - [ ] Create Pydantic input schemas for monitor targets.
  - [ ] Write creation endpoints (`POST /monitors`).
  - [ ] Write reading and list retrieval endpoints (`GET /monitors`).
  - [ ] Write deletion endpoints (`DELETE /monitors/{id}`).
* 📦 **Deliverable:** Users can successfully create, list, and delete site monitor targets.

---

### **Sprint 4: Synthetic Monitoring Engine**
* **Goal:** Launch background health monitoring checkers.
* 📋 **Tasks:**
  - [ ] Install and configure `APScheduler` in backend.
  - [ ] Implement async HTTP website health checker utility.
  - [ ] Log response time and HTTP status code metrics into the database.
* 📦 **Deliverable:** Periodic background checks trigger and store website performance results.

---

### **Sprint 5: Dashboard & Analytics APIs**
* **Goal:** Deliver aggregation APIs for dashboard rendering.
* 📋 **Tasks:**
  - [ ] Implement Uptime calculations logic.
  - [ ] Write aggregated dashboard metrics endpoint (`GET /dashboard/summary`).
  - [ ] Write latency history timeline endpoint (`GET /dashboard/history/{id}`).
* 📦 **Deliverable:** Clean API endpoints providing calculated stats for frontend charts.

---

### **Sprint 6: React Dashboard Client**
* **Goal:** Build the visual web client application.
* 📋 **Tasks:**
  - [ ] Create Login & Register forms.
  - [ ] Design the layout grid structure.
  - [ ] Implement Monitor Cards with current status details.
  - [ ] Bind latency charts to database metrics using Recharts.
* 📦 **Deliverable:** Fully interactive React SPA showing live status indicators and charts.

---

### **Sprint 7: Event Alerts & Notification Service**
* **Goal:** Inform owners when downtime events are triggered.
* 📋 **Tasks:**
  - [ ] Define database `Alert` audit schema.
  - [ ] Setup email dispatch agent (SMTP/SES).
  - [ ] Implement failure-threshold check trigger (e.g. 3 consecutive failures).
* 📦 **Deliverable:** Automated emails sent instantly when a monitored site goes down.

---

### **Sprint 8: Production Hardening & Documentation**
* **Goal:** Optimize deployment scripts and document usage.
* 📋 **Tasks:**
  - [ ] Dockerize backend and frontend services.
  - [ ] Configure standard system log rotation.
  - [ ] Create deployment documentation and comprehensive `README.md`.
* 📦 **Deliverable:** Production-ready Docker Compose environment with full configuration guide.
