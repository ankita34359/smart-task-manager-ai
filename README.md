# 🚀 Smart Task Manager (AI-Enhanced)

A full-stack, production-ready task management application built using **Flask (backend)** and **React (frontend)**.
This project focuses on **clean architecture, strict validation, and correctness**, along with a controlled **AI-based priority suggestion system**.

---

## 🌐 Live Demo

* **Frontend (Vercel):** https://smart-task-manager-ai-rho.vercel.app
* **Backend (Render):** *(Add your Render backend URL here)*

---

## 📌 Features

* ✅ Create, update, and delete tasks
* ✅ Strict workflow enforcement:

  * `TODO → IN_PROGRESS → DONE` (no skipping allowed)
* ✅ AI-based priority suggestion (LOW, MEDIUM, HIGH)
* ✅ Input validation (prevents invalid data)
* ✅ Modular backend architecture
* ✅ RESTful API integration
* ✅ Automated tests using Pytest

---

## 🧠 Key Highlights

* Prevents invalid states (empty title, incorrect transitions)
* Clean separation of concerns (routes, services, schemas, models)
* Schema-based validation using Marshmallow
* AI feature is optional, controlled, and safe
* Designed with **production deployment in mind**

---

## 🏗️ Architecture Overview

### 🔹 Backend (Flask)

* Built with **Flask**, **SQLAlchemy**, and **Marshmallow**
* Modular structure:

  * `routes/` → API layer
  * `services/` → business logic
  * `schemas/` → validation
  * `models/` → database

### 🔹 Frontend (React)

* Built using **React (Vite)**
* Clean UI with glassmorphism design
* Uses Axios for API communication

---

## ⚙️ Tech Stack

### Backend

* Python (Flask)
* SQLAlchemy
* Marshmallow
* Gunicorn
* Pytest

### Frontend

* React (Vite)
* Axios
* CSS

### Database

* SQLite (development)
* PostgreSQL (Neon for production)

---

## 📂 Project Structure

```
smart-task-manager-ai/
│
├── backend/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── utils/
│   ├── tests/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── hooks/
│
├── README.md
├── ai_guidelines.md
└── .env.example
```

---

## 🔐 Validation Rules

* Task title cannot be empty
* Invalid status transitions are not allowed
* Only allowed statuses:

  * TODO
  * IN_PROGRESS
  * DONE

---

## 🤖 AI Feature

* Suggests task priority based on description
* Implemented as a controlled AI mock (`utils/ai.py`)
* Ensures:

  * Valid outputs only (LOW, MEDIUM, HIGH)
  * Fallback handling if AI fails
  * System does not depend on AI

---

## 🧪 Testing

Automated tests are implemented using **Pytest**.

### Covered:

* Task creation
* Invalid inputs
* Status transitions
* AI behavior
* Validation errors

Run tests:

```
cd backend
pytest
```

---

## ▶️ How to Run Locally

### 🔹 Backend

```
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python app.py
```

---

### 🔹 Frontend

```
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:5173
```

---

## 🧪 How to Verify Functionality

1. Create a task
2. Use description like **"urgent work"** → priority becomes HIGH
3. Move task:

   * TODO → IN_PROGRESS → DONE
4. Try invalid inputs (empty title) → validation error

---

## ☁️ Deployment

This project is deployed using modern cloud platforms:

### 🔹 Database (Neon)

* PostgreSQL cloud database
* Persistent and production-ready
* Connection via `DATABASE_URL`

---

### 🔹 Backend (Render)

* Flask API deployed as Web Service
* Uses Gunicorn for production

Configuration:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn "app:create_app()"
```

Environment Variable:

```
DATABASE_URL=<Neon PostgreSQL URL>
```

---

### 🔹 Frontend (Vercel)

* React app deployed via Vercel

Environment Variable:

```
VITE_API_URL=<Render Backend URL>/api
```

---

## ⚖️ Design Decisions

* Used **SQLite** for local development simplicity
* Switched to **PostgreSQL (Neon)** for production reliability
* Focused on **clean architecture over complex features**
* AI implemented safely without system dependency

---

## 🚀 Future Improvements

* User authentication
* Real AI integration (OpenAI API)
* Drag-and-drop task management
* Filtering and search

---

## 🎥 Walkthrough

*(Add your video link here)*

---

## 📧 Submission

Developed as part of an engineering assessment.

---

## 👩‍💻 Author

**Ankita Gupta**
