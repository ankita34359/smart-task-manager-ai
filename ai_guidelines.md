#  AI Guidelines – Smart Task Manager

##  How I Used AI

I used AI tools like Claude and Antigravity to help in building this project.

AI helped me in:

* Creating project structure (backend and frontend)
* Generating initial code for APIs and components
* Suggesting improvements and fixes

I did not use AI blindly. I reviewed all the code, tested it, and made changes where needed.

---

##  How I Controlled AI

* I ensured all validation rules are properly implemented
* I kept business logic separate from routes
* I avoided complex or unclear code
* I verified all outputs manually

---

##  AI Feature in This Project

This project includes a simple AI-based priority suggestion.

* If description contains "urgent" → HIGH
* If description contains "important" → MEDIUM
* Otherwise → LOW

### Safety:

* Output is limited to LOW, MEDIUM, HIGH only
* Fallback is implemented if AI fails
* The system works even without AI

---

##  Key Point

AI was used only as a helper.
All final decisions and validations were handled by me.

---
