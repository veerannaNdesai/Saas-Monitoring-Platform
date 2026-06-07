# System Architecture Design
## SaaS Monitoring Platform

---

## 1. Objective & Overview
Define the high-level architecture of the SaaS Monitoring Platform and describe how different system components interact to provide website monitoring, historical analytics, and alert notifications. 

The architecture is designed to be simple and lightweight for the MVP (Version 1) while establishing clear boundaries that support scalability and future horizontal expansion.

---

## 2. System Components

The platform consists of five primary components.

### 2.1 React Frontend
* 💡 **Responsibilities:**
  * User registration and authentication interface.
  * Monitor configuration and CRUD management dashboard.
  * Uptime and response time latency visualization.
  * Historical alert logs and status viewing.
* 🚫 **Constraints:**
  * Communicates exclusively via REST APIs.
  * Has no direct database connectivity.
  * Does not perform monitoring checks or trigger notification emails.

### 2.2 FastAPI Backend
* 💡 **Responsibilities:**
  * User authentication and session validation.
  * Business logic execution and input validation.
  * Database operations (via ORM or query builder).
  * API routing, authorization filters, and schema management.
* 📞 **Key REST APIs:**
  * `POST /auth/register` - Create new user accounts
  * `POST /auth/login` - Obtain authentication tokens
  * `GET /monitors` - Fetch all configured monitors
  * `POST /monitors` - Add a new monitor target
  * `GET /dashboard` - Retrieve aggregated uptime & performance analytics
  * `GET /alerts` - Retrieve historical alerts
* 📌 **Purpose:** Acts as the central application orchestration layer.

### 2.3 PostgreSQL Database
* 💡 **Responsibilities:**
  * Persistent storage for all core business data.
* 🗄️ **Stored Tables:**
  * `users` - Accounts and credentials
  * `monitors` - Websites configuration targets
  * `monitor_logs` - Historical latency and check response logs
  * `alerts` - Records of triggered downtime notifications
* 📌 **Purpose:** Provides durable, relational data integrity and historical auditing.

### 2.4 Scheduler Service
* 💡 **Responsibilities:**
  * Automatically coordinates check loops at configured frequencies.
* 🔄 **Standard Monitoring Workflow:**
  1. Fetch active monitors from PostgreSQL.
  2. Execute concurrency-optimized health checks.
  3. Record status codes, latencies, and availability results.
  4. Write outcome logs to `monitor_logs`.
  5. Check assertions and dispatch alerts if failures occur.
* 📦 **MVP Technology:** `APScheduler` (Advanced Python Scheduler) running in-process or as a lightweight background daemon.
* 🚀 **Future Growth path:** Transition to a distributed setup utilizing a task queue (e.g., Celery, BullMQ) backed by Redis/RabbitMQ and multiple worker processes.

### 2.5 Email Notification Service
* 💡 **Responsibilities:**
  * Deliver downtime/uptime alerts immediately to users when checks fail.
* ✉️ **Alert Format Example:**
  ```text
  Subject: Website Down Alert
  ------------------------------------
  Website: https://example.com
  Status:  DOWN
  Time:    12:15 PM
  ------------------------------------
  ```
* 📌 **Purpose:** Delivers proactive user alerting to guarantee minimal time-to-resolution.

---

## 3. High-Level Architecture Diagram

```mermaid
graph TD
    User([User Browser]) -->|HTTPS| ReactFrontend[React Frontend]
    ReactFrontend -->|REST API| FastAPI[FastAPI Backend]

    subgraph API_Layer [FastAPI Backend APIs]
        FastAPI --> AuthAPI[Authentication]
        FastAPI --> MonitorAPI[Monitor CRUD]
        FastAPI --> DashboardAPI[Dashboard Analytics]
    end

    AuthAPI & MonitorAPI & DashboardAPI -->|Read/Write| Postgres[(PostgreSQL)]

    Scheduler[Scheduler Service - APScheduler] -->|1. Query Targets| Postgres
    Scheduler -->|2. Run Checks| TargetWebsites[External Websites / APIs]
    Scheduler -->|3. Save Log| Postgres
    Scheduler -->|4. Trigger Alert| AlertService[Alert Service]
    AlertService -->|5. Send Notification| EmailService[Email Notification Service]
    EmailService -->|6. Deliver Email| User
```

---

## 4. System Data Flows

### 4.1 User Registration Flow
```mermaid
sequenceDiagram
    actor User
    participant Frontend as React Frontend
    participant Backend as FastAPI Backend
    participant DB as PostgreSQL
    
    User->>Frontend: Fill Registration Form
    Frontend->>Backend: POST /auth/register
    Backend->>DB: Save user credentials
    DB-->>Backend: Confirmed
    Backend-->>Frontend: Success Response (JWT/Session)
    Frontend-->>User: Load authenticated dashboard
```

### 4.2 Create Monitor Target Flow
```mermaid
sequenceDiagram
    actor User
    participant Frontend as React Frontend
    participant Backend as FastAPI Backend
    participant DB as PostgreSQL
    
    User->>Frontend: Configure Target (e.g., https://example.com, 60s check)
    Frontend->>Backend: POST /monitors
    Backend->>DB: Store monitor settings
    DB-->>Backend: Confirmed
    Backend-->>Frontend: Return created monitor record
    Frontend-->>User: Display monitor status cards
```

### 4.3 Automated Uptime Check Flow
```mermaid
sequenceDiagram
    participant Scheduler as Scheduler Service
    participant Target as External Target Website
    participant DB as PostgreSQL
    
    Scheduler->>DB: Retrieve active monitors
    DB-->>Scheduler: Return monitor targets list
    loop For each active monitor
        Scheduler->>Target: Execute HTTP GET request
        Note over Scheduler: Measure Response Time & Status
        Target-->>Scheduler: Response status code (e.g., 200 OK)
        Scheduler->>DB: Insert record into monitor_logs (status, response_time)
    end
```

### 4.4 Downtime Detection & Alerting Flow
```mermaid
sequenceDiagram
    participant Scheduler as Scheduler Service
    participant Alert as Alert Service
    participant DB as PostgreSQL
    participant Email as Email Service
    
    Note over Scheduler: Uptime check fails (e.g., 500 Server Error)
    Scheduler->>DB: Insert log record (is_up = false)
    Scheduler->>Alert: Trigger Alert Event
    Alert->>DB: Save record to alerts audit log
    Alert->>Email: Request email delivery
    Email-->>Email: Dispatch downtime alert email to user
```

### 4.5 Dashboard Visualization Flow
```mermaid
sequenceDiagram
    actor User
    participant Frontend as React Frontend
    participant Backend as FastAPI Backend
    participant DB as PostgreSQL
    
    User->>Frontend: Load Dashboard Page
    Frontend->>Backend: GET /dashboard
    Backend->>DB: Query monitor states, uptime percent, & average latencies
    DB-->>Backend: Return aggregated analytics
    Backend-->>Frontend: Return dashboard payload
    Frontend-->>User: Render charts & status indicators
```

---

## 5. Scalability Considerations

| Aspect | MVP Architecture (V1) | Production/Scalable Architecture |
| :--- | :--- | :--- |
| **Engine** | FastAPI + SQLite/PostgreSQL + APScheduler | FastAPI + PostgreSQL + Task Queue |
| **Concurrency** | In-process Threading / Async loops | Distributed workers (Celery/BullMQ) with Redis broker |
| **Performance** | Ideal for 100s of monitored targets | Scales horizontally to 10,000s of parallel targets |
| **Fault Tolerance** | Single process failure stops scheduling | Workers can fail independently without halting scheduling |

---

## 6. Architectural Principles

* 📐 **Separation of Concerns:** Each component is decoupled. The frontend handles view presentation; the backend processes business logic; the scheduler runs checks independently; and the database manages state.
* ⚙️ **Horizontal Scalability:** Components can be scaled separately. If check counts grow, additional workers can be added. If browser traffic spikes, frontend/API instances can be replicated.
* 🛠️ **Maintainability:** Clear boundaries and interface contracts make debugging, updating dependencies, and building integrations trivial.

---

## 7. Summary
The SaaS Monitoring Platform uses a layered architecture consisting of a React frontend, FastAPI backend, PostgreSQL database, scheduler service, and email notification system. 

By separating API logic from scheduled task runners, the system maintains high responsive performance on user dashboard requests while executing continuous, reliable background health checks. This template serves as a strong foundation for future features including API monitoring assertions, distributed worker nodes, Slack hook notifications, and multi-tenant billing models.
