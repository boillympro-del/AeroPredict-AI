# ✈️ AeroPredict AI

> 🚧 **Work in progress** – this project is still under development.

A Python command-line tool to monitor industrial / aeronautic machines: it records each machine's **temperature** and **rotation speed**, saves them to a CSV file, and raises **alerts** when values go outside safe limits.

## Features

- ➕ Register one or several machines (ID, temperature, speed) with input validation
- 💾 Save every machine to `registre.csv` and reload them automatically on startup
- 🗄️ Also store every new machine in a **SQLite** database (`database.db`, table `machines`) – see `data.py`
- 📋 List all registered machines
- 🔍 Search a machine by its ID
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
- `data.py` – SQL part: creates the `machines` table and inserts machines

## Roadmap

- [x] Load saved machines from the CSV back into the program
- [x] Search a machine by its ID
- [x] Save machines in a SQLite database
- [ ] Read machines back from the database instead of the CSV
- [ ] Edit / delete a machine
- [ ] Data analysis & predictions (pandas, scikit-learn) – the "AI" part 🤖

---

Made by [@boillympro-del](https://github.com/boillympro-del) – BTS SIO SLAM student.
