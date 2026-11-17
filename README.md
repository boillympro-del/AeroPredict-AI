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
- ⚠️ Alerts when:
  - temperature is above **80 °C**
  - speed is outside **1500 ± 150 rpm**

## Run it

```bash
python AER0.py
```

Requires Python 3 – no external libraries (`sqlite3` is built into Python).

## Files

- `AER0.py` – the main program (menu, machines, alerts)
- `data.py` – SQL part: create the table, add / show / modify / delete machines

## Roadmap

- [x] Load saved machines from the CSV back into the program
- [x] Search a machine by its ID
- [x] Save machines in a SQLite database
- [x] Read machines back from the database instead of the CSV
- [x] Edit / delete a machine
- [ ] Data analysis & predictions (pandas, scikit-learn) – the "AI" part 🤖

## Versions

| Version | What changed |
|---|---|
| V0 | First version: add machines, alerts, CSV file |
| V1 Py | Reload machines from the CSV + search by ID |
| V2 Py + V1 SQL | SQLite database: create the table and add machines |
| V3 Py + V2 SQL | Show / modify / delete machines from the database, new menu options |

---

Made by [@boillympro-del](https://github.com/boillympro-del) – BTS SIO SLAM student.
