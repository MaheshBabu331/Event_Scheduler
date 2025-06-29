# 📅 Event Scheduler System

Biz Digital IT Services Pvt. Ltd. - **Code Assessment Solution**

This is a simple Python backend application built using **Flask** that allows users to:

✅ Create,  
✅ View (sorted list),  
✅ Update,  
✅ Delete events  
with **persistence** to a file (`events.json`).

---

## ⚙️ Features
- Add events (title, description, start time, end time)
- List all events (sorted by start time)
- Update event details
- Delete events
- Save events between sessions using a JSON file

---

## 🚀 Setup & Run

### 1️⃣ Clone the repo (or download code)
```bash
git clone <https://github.com/MaheshBabu331/Event_Scheduler.git>
cd event_scheduler
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```
Activate it:
- Windows:
  ``` bash
  venv\Scripts\activate
  ```
- Linux / Mac:
  ``` bash
  source venv/bin/activate
  ```
### 3️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```
### 4️⃣ Run the application
``` bash
python app.py
```
👉 By default, the app runs at:
http://127.0.0.1:5000/
## 🛠 API Endpoints
### ➕ Create Event
``` bash
POST /events
Content-Type: application/json
```
``` bash
{
  "title": "Meeting",
  "description": "Discuss project roadmap",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00"
}
```
✅ Response: 201 Created
### 📋 List Events
``` bash
GET /events
```
✅ Response: 200 OK
Returns JSON list sorted by start_time.
### ✏️ Update Event
```   bash
PUT /events/<event_id>
Content-Type: application/json
```
Partial update example:
``` bash
{
  "title": "Updated Meeting",
  "end_time": "2025-07-01T12:00:00"
}
```
✅ Response: 200 OK
### ❌ Delete Event
``` bash
DELETE /events/<event_id>
```
✅ Response: 200 OK
``` bash
{ "message": "Event deleted" }
```
🔑 Data Persistence
Events are stored in events.json

Data survives between restarts

## pip install pytest
``` bash
pip install pytest
pytest
```
## 📂 POSTMAN
Import the provided POSTMAN Collection JSON
Try the APIs: POST, GET, PUT, DELETE

## 📌 Notes
- ✅ All datetimes must be in ISO 8601 format, e.g. 2025-07-01T10:00:00
- ✅ App runs locally; no external database needed.


