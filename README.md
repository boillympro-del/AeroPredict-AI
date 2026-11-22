# ✈️ AeroPredict AI

> 🚧 **Work in progress** – this project is still under development.

A Python command-line tool to monitor industrial / aeronautic machines: it records each machine's **temperature** and **rotation speed**, saves them to a CSV file, and raises **alerts** when values go outside safe limits.

## Features

- ➕ Register one or several machines (ID, temperature, speed) with input validation
- 🗄️ Store every machine in a **SQLite** database (`database.db`, table `machines`) and reload them automatically on startup – see `data.py`
- 📋 List all registered machines
- 🔍 Search a machine by its ID
- ✏️ Modify a machine (new temperature / speed, updated in the database)
- 🗑️ Delete a machine (removed from the database)
- 🆔 Unique machine IDs (SQL `PRIMARY KEY`): a duplicate ID is refused
- 📊 Statistics: total machines, average / highest / lowest temperature and speed (SQL `COUNT`, `AVG`, `MAX`, `MIN`)
- ⚠️ Alerts when:
  - temperature is above **80 °C**
  - speed is outside **1500 ± 150 rpm**

## Run it

```bash
python AER0.py
```

Requires Python 3 – no external libraries (`sqlite3` is built into Python).

## REST API (FastAPI)

The machines stored in the database are also available through a small web API.

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

| Method | Route | What it does |
|---|---|---|
| GET | `/machines` | Returns all machines as JSON (`identifiant`, `temperature`, `vitesse`) |
| GET | `/machines/{identifiant}` | Returns one machine (404 if it doesn't exist) |
| POST | `/machines` | Adds a machine (body: `identifiant`, `temperature`, `speed`) – 201 if created, 409 if the ID already exists |
| PUT | `/machines/{identifiant}` | Modifies a machine's temperature and speed (404 if it doesn't exist) |
| DELETE | `/machines/{identifiant}` | Deletes a machine (404 if it doesn't exist) |
| GET | `/alertes?seuil=100` | Machines whose temperature is above the threshold (default 100 °C) |
| GET | `/stats/` | Statistics: total machines, average / highest / lowest temperature and speed |

Input is validated with Pydantic: temperature must be between **0 and 150 °C** and speed between **0 and 3600 rpm**, otherwise the API answers with an error (422).

Interactive docs (Swagger): http://127.0.0.1:8000/docs

## Files

- `AER0.py` – the main program (menu, machines, alerts)
- `data.py` – SQL part: create the table, add / show / modify / delete machines, statistics
- `api.py` – REST API with FastAPI (reads the machines from `data.py`)
- `requirements.txt` – libraries needed for the API

## Roadmap

- [x] Load saved machines from the CSV back into the program
- [x] Search a machine by its ID
- [x] Save machines in a SQLite database
- [x] Read machines back from the database instead of the CSV
- [x] Edit / delete a machine
- [x] Statistics on all machines
- [x] REST API with FastAPI (add / list / modify / delete machines + statistics)
- [ ] Data analysis & predictions (pandas, scikit-learn) – the "AI" part 🤖

## Versions

| Version | What changed |
|---|---|
| V0 | First version: add machines, alerts, CSV file |
| V1 Py | Reload machines from the CSV + search by ID |
| V2 Py + V1 SQL | SQLite database: create the table and add machines |
| V3 Py + V2 SQL | Show / modify / delete machines from the database, new menu options |
| V4 Py + V3 SQL | Statistics menu (count, average, max, min) + unique machine IDs |
| V5 Py + V1 API | First FastAPI route `GET /machines` (`api.py`) + removed test prints |
| V2 API | Full CRUD API: `POST`, `PUT`, `DELETE /machines` + `GET /stats/`, input validation with Pydantic |
| V4 SQL + V3 API | Robust API: `PUT`/`DELETE` return 404 when the machine doesn't exist (`rowcount`), 409 on duplicate ID, new `GET /machines/{identifiant}` and `GET /alertes` |

---

Made by [@boillympro-del](https://github.com/boillympro-del) – BTS SIO SLAM student.
