# Kong API Gateway Lab

A hands-on, end-to-end **API Gateway lab** demonstrating how to design, deploy, and evolve backend services behind **Kong Gateway OSS(Open Source)** using **Docker**.

This repository is intentionally built as a **learning + portfolio project**, focusing on **real-world gateway patterns** rather than toy examples.  
Kubernetes is treated as a **future, optional extension**, not a prerequisite.

---

## 📌 Scope & Learning Focus

This lab is designed to provide a **clear and lightweight entry point into Kong API Gateway fundamentals**.

While Kubernetes is a common runtime for Kong in production, it is **not required to understand gateway concepts** such as routing, traffic control, and plugins.  
To avoid unnecessary complexity, Kubernetes support is positioned as a **future roadmap item**, allowing learners to focus on Kong first.

---

## 🎯 Goals of This Lab

- Demonstrate **API Gateway fundamentals** using Kong OSS
- Show **consumer-transparent routing** and rollout patterns
- Keep backend services **private and decoupled**
- Build artifacts that are:
  - Easy to run locally
  - Easy to understand
  - Easy to extend in the future (e.g. Kubernetes)

---

## 🧱 Current Architecture (Docker-based)

```text
Client
  |
  v
Kong Gateway (DB-less)
  |
  v
Upstream (weighted)
  ├── service-a (FastAPI)
  └── service-b (FastAPI)
``` 
### Key characteristics
	•	Single external entry point (Kong)
	•	Backend services are not exposed directly
	•	Traffic routing is controlled centrally at the gateway
	•	No consumer-side changes required during rollouts

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

## 🗂 Repository Structure (Current State)
```
.
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
	-	Support **multiple tech stacks** (Python now, Java later)
	-	Allow an optional transition to **Kubernetes manifests** in the future
```
---

## ▶️ Running the Lab (Docker)

### Prerequisites
	•	Docker Desktop
	•	Docker Compose (comes with Docker Desktop)

### Start the stack

docker compose -f docker-compose/docker-compose-python.yml up --build

---

## Test the API
curl http://localhost:8000/api/v1/hello

Repeat the call multiple times to observe traffic being served by both services, as Kong distributes traffic across upstream targets.

### Example response (service-a):
```json
{
  "service": "service-a",
  "version": "v1",
  "message": "Hello from API v1"
}
```
### Example response (service-b):

```json

{
  "service": "service-b",
  "version": "v2",
  "message": "Hello from API v2"
}
```
---

## 🤔 Why This Design Matters

This lab mirrors real production gateway patterns:
	-	Consumers talk to one stable endpoint
	-	Rollouts and experiments happen at the gateway
	-	Backends evolve independently
	-	Failures and limits are handled centrally

These principles are widely used in:
	-	API platforms
	-	Microservices architectures
	-	Cloud-native systems

---

## ⏳ What’s Intentionally Deferred (For Now)

To keep the learning experience focused, the following are planned but not yet implemented:
	-	Kubernetes / Minikube deployment
	-	Prometheus & Grafana (observability)
	-	Java Spring Boot backend service
	-	Ingress controller mode
	-	CI/CD pipelines

These enhancements will be added incrementally, without refactoring the existing Docker-based setup.

---

## 🗺 Roadmap

Planned future enhancements include:
	-	Optional Kubernetes (Minikube) deployment
	-	Running Kong Gateway in Kubernetes (DB-less mode)
	-	Re-applying weighted traffic routing in Kubernetes
	-	Adding observability in a Kubernetes-native way
	-	Introducing a Java Spring Boot backend service

Kubernetes is intentionally treated as an advanced, optional extension, not a prerequisite for understanding Kong.

---

## 📌 Notes
	-	This project uses Kong OSS (Open Source), not Enterprise.
	-	Gateway-level patterns are the primary focus.
	-	The repository prioritises clarity and correctness over feature overload.

---

## 👤 Author

Built as a hands-on learning project to explore:
	-	API Gateway design
	-	Traffic management patterns
	-	Containerised backends
	-	Cloud-native foundations