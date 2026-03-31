# 🚀 Smart Task Manager (AI-Enhanced)

A full-stack task management application built with **Flask (backend)** and **React (frontend)**.
This project focuses on **clean architecture, validation, and correctness**, along with a simple **AI-based priority suggestion system**.

---

## 📌 Features

* ✅ Create, update, and delete tasks
* ✅ Task status workflow:
  **TODO → IN_PROGRESS → DONE** (no skipping allowed)
* ✅ AI-based priority suggestion (LOW, MEDIUM, HIGH)
* ✅ Input validation (prevents invalid data)
* ✅ Clean modular backend architecture
* ✅ RESTful API integration
* ✅ Automated tests using Pytest

---

## 🧠 Key Highlights

* Prevents invalid states (e.g., empty title, incorrect transitions)
* Business logic separated from routes (service layer)
* Schema-based validation using Marshmallow
* AI feature is optional and safe (fallback supported)
* Designed for maintainability and scalability

---

## 🏗️ Tech Stack

### Backend

* Python (Flask)
* SQLAlchemy
* Marshmallow
* Pytest

### Frontend

* React (Vite)
* Axios
* CSS

### Database

* SQLite (for development)
* PostgreSQL (can be used in production)

---

## 📂 Project Structure

```
smart-task-manager/
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
└── ai_guidelines.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/smart-task-manager-ai.git
cd smart-task-manager-ai
```

---

### 🔹 2. Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate   # For Windows

pip install -r requirements.txt
```

Run backend:

```
python app.py
```

---

### 🔹 3. Frontend Setup

```
cd frontend
npm install
npm run dev
```

Open in browser:

```
http://localhost:5173
```

---

## 🧪 Running Tests

```
cd backend
pytest
```

---

## 🤖 AI Feature

* Suggests task priority based on description
* Controlled and validated before saving
* Includes fallback logic if AI fails
* Does not affect core system functionality

---

## 🔐 Validation Rules

* Task title cannot be empty
* Invalid status transitions are not allowed
* Only allowed statuses:

  * TODO
  * IN_PROGRESS
  * DONE

---

## ⚖️ Design Decisions

* Used **SQLite** for simplicity during development
* Structured backend for easy migration to PostgreSQL
* Prioritized **clean code and correctness over complexity**
* AI feature implemented safely without dependency

---

## 🚀 Future Improvements

* User authentication
* Real AI integration (OpenAI/LLM APIs)
* Drag-and-drop UI
* Task filtering and search

---

## 🎥 Walkthrough

(Add your video link here)

---

## 📧 Submission

Developed as part of an engineering assessment.

---

## 👩‍💻 Author

Ankita Gupta
