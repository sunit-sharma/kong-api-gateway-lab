# Kong API Gateway Lab

A hands-on, end-to-end **API Gateway lab** demonstrating how to design, deploy, and evolve backend services behind **Kong Gateway (OSS)** using Docker today, with a clear path to **Kubernetes / Minikube** next.

This repository is intentionally built as a **learning + portfolio project**, focusing on **real-world gateway patterns** rather than toy examples.

---

## 🎯 Goals of This Lab

- Demonstrate **API Gateway fundamentals** using Kong OSS
- Show **consumer-transparent routing** and rollout patterns
- Keep backend services **private and decoupled**
- Build artifacts that are:
  - Easy to run locally
  - Easy to understand
  - Easy to extend to Kubernetes

---

## 🧱 Current Architecture (Docker-based)

Client
|
v
Kong Gateway (DB-less)
|
v
Upstream (weighted)
├── service-a (FastAPI)
└── service-b (FastAPI)

### Key characteristics
- Single external entry point (Kong)
- Backend services not exposed directly
- Traffic routing controlled centrally at the gateway
- No consumer-side changes required for rollouts

---

## 🚀 What’s Implemented So Far

### ✅ API Gateway
- **Kong OSS (DB-less mode)**
- Declarative configuration via `kong.yml`
- Single route (`/api`) exposed to consumers

### ✅ Backend Services
- `service-a`: Python FastAPI
- `service-b`: Python FastAPI
- Containerised with Docker
- Simple JSON responses for clarity

### ✅ Traffic Management
- **Weighted routing (canary-style rollout)** using Kong upstreams
- Example:
  - 50% → service-a
  - 50% → service-b
- Traffic can be shifted without client changes

### ✅ Gateway Plugins
- **Rate Limiting**
  - Protects backend services
  - Enforced at the gateway
- **Correlation ID**
  - Request tracing via `X-Request-ID`
  - Propagated downstream

---

## 🗂 Repository Structure (So Far)

├── backends/
│   └── python-fastapi/
│       ├── service-a/
│       └── service-b/
│
├── kong/
│   └── kong.yml
│
├── docker-compose/
│   └── docker-compose-python.yml
│
└── README.md

This structure is intentionally designed to:
- Support **multiple tech stacks** (Python now, Java later)
- Transition cleanly to **Kubernetes manifests**

---

## ▶️ Running the Lab (Docker)

### Prerequisites
- Docker Desktop
- Docker Compose (comes with Docker Desktop)

### Start the stack

docker compose -f docker-compose/docker-compose-python.yml up --build

### Test the API
curl http://localhost:8000/api/v1/hello

Note : Repeat the call multiple times to observe traffic being served by both services as Kong is routing is distrinuting traffic using round robin algorithm across both versions of APIs.

Example response-1:

{
  "service": "service-a",
  "version": "v1",
  "message": "Hello from API v1"
}
Example response-2:
{
  "service": "service-b",
  "version": "v2",
  "message": "Hello from API v2"
}

### Why This Design Matters

This lab mirrors real production gateway patterns:
	•	Consumers talk to one stable endpoint
	•	Rollouts and experiments happen at the gateway
	•	Backends can evolve independently
	•	Failures and limits are handled centrally

These are the same principles used in:
	•	API platforms
	•	Microservices architectures
	•	Cloud-native systems

### What’s Intentionally Deferred (For Now)

To keep the foundation clean, the following are planned but not yet committed:
	•	Prometheus & Grafana (observability)
	•	Kubernetes / Minikube manifests
	•	Java Spring Boot backend
	•	Ingress controller mode
	•	CI/CD pipelines

Each of these will be added incrementally, without refactoring existing work.

### Roadmap

Planned next steps:
	1.	Migrate services to Kubernetes (Minikube)
	2.	Deploy Kong in Kubernetes (DB-less)
	3.	Re-implement weighted routing in K8s
	4.	Add observability in a Kubernetes-native way
	5.	Introduce a Java Spring Boot service

⸻

### 📌 Notes
	•	This project uses Kong OSS, not Enterprise.
	•	Gateway-level patterns are the focus.
	•	The repository prioritises clarity and correctness over feature overload.

⸻

### 👤 Author

Built as a hands-on learning and portfolio project to explore:
	•	API Gateway design
	•	Traffic management patterns
	•	Containerised backends
	•	Cloud-native foundation


