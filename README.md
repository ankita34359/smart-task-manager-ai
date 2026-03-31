# Smart Task Manager

A production-quality full-stack web application designed to demonstrate clean architecture, robust data validation, and AI-driven workflow features.

## Project Overview

Smart Task Manager allows users to organize their tasks on a Kanban-style board with strict workflow transitions (`TODO` ➔ `IN_PROGRESS` ➔ `DONE`). It features a Python Flask backend ensuring rigid data validation, and a modern React frontend utilizing glassmorphism and smooth animations.

### Key Features
- **Strict Status Transitions:** Tasks cannot skip workflow stages, and cannot go backwards.
- **Robust Validation:** Implemented using Marshmallow against empty strings, invalid statuses, and past due dates.
- **Duplicate Prevention:** The backend checks for tasks with duplicating titles to keep the board clean.
- **AI Priority Suggestion:** Automatically suggests a priority (`LOW`, `MEDIUM`, `HIGH`) based on task descriptions. Includes a safe fallback so the main system never throws errors during ingestion.

---

## Architecture & Technology Stack

### Backend
- **Framework:** Python (Flask)
- **Database:** SQLite (development safe, via SQLAlchemy)
- **Validation:** Marshmallow Schema validation
- **Testing:** Pytest & pytest-flask
- **Design Pattern:** Clean Architecture with separate layers:
  - `routes/`: Handles HTTP requests and responses.
  - `services/`: Contains core business logic and state transition rules.
  - `schemas/`: Exclusively handles validation of DTOs.
  - `models/`: SQLAlchemy database definitions.

### Frontend
- **Framework:** React + Vite
- **Styling:** Vanilla CSS with variables and modern glassmorphism (no Tailwind required).
- **Icons:** `lucide-react`
- **Network:** Axios for clean API queries.

---

## AI Integration Explanation

(Ref: `ai_guidelines.md` for extended details)

The AI suggestion utility is located at `backend/utils/ai.py`. It serves to parse incoming Task descriptions to suggest a valid priority tier. The feature is built to be **resilient**:
1. It validates output ensuring it matches strictly `LOW`, `MEDIUM`, or `HIGH`.
2. It catches internal exceptions perfectly so core HTTP response flow is never blocked.
3. It has a fallback implementation using heuristic keywords (`urgent`, `soon`) allowing the project to run safely strictly offline without external LLM provider costs.

---

## Setup Steps

### 1. Backend Setup

```bash
cd backend
python -m venv venv

# On Windows:
.\venv\Scripts\Activate.ps1
# On Mac/Linux:
# source venv/bin/activate

pip install -r requirements.txt
```

Run backend tests:
```bash
pytest
```

Run the API Server:
```bash
python app.py
```
*The API will start on `http://localhost:5000`.*

### 2. Frontend Setup

In a new terminal:
```bash
cd frontend
npm install
npm run dev
```
*The app will launch, typically accessible at `http://localhost:5173`.*

---

## API Documentation

### `POST /api/tasks`
Create a new task.
- **Body:** `{ "title": "...", "description": "..." }`
- **Returns:** HTTP 201 with Task object.

### `GET /api/tasks`
Fetch all tasks.
- **Returns:** HTTP 200 with list of Task objects.

### `PUT /api/tasks/<id>`
Update status or details of a task. Validation enforces `TODO` ➔ `IN_PROGRESS` ➔ `DONE` transitions.
- **Body:** `{ "status": "IN_PROGRESS" }`
- **Returns:** HTTP 200 with Updated Task object.

### `DELETE /api/tasks/<id>`
Remove a task entirely.
- **Returns:** HTTP 200 `{ "message": "Success" }`

---

## Tradeoffs and Design Decisions
- **Vanilla CSS:** I chose pure CSS Variables and modular naming to achieve a beautiful frosted-glass layout without importing Tailwind. This keeps the frontend incredibly lightweight.
- **SQLite Database:** Used for zero-friction local development, but wrapped cleanly behind SQLAlchemy so swapping to `PostgreSQL` in production is a 1-line change to `DATABASE_URL`.
- **Mock AI Implementation:** Instead of embedding an expensive `openai` or `gemini` call that could break during assessment if API keys run empty, I provided a robust heuristic mock. The Service architecture natively supports swapping this exact function out with a real API call whenever necessary, demonstrating architectural safety over brittle integrations.
