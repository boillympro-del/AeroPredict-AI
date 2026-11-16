# ✈️ AeroPredict AI

> 🚧 **Work in progress** – this project is still under development.

A Python command-line tool to monitor industrial / aeronautic machines: it records each machine's **temperature** and **rotation speed**, saves them to a CSV file, and raises **alerts** when values go outside safe limits.

## Features

- ➕ Register one or several machines (ID, temperature, speed) with input validation
- 💾 Save every machine to `registre.csv` and reload them automatically on startup
- 📋 List all registered machines
- 🔍 Search a machine by its ID
- ⚠️ Alerts when:
  - temperature is above **80 °C**
  - speed is outside **1500 ± 150 rpm**

## Run it

```bash
python AER0.py
```

Requires Python 3 – no external libraries.

## Roadmap

- [x] Load saved machines from the CSV back into the program
- [x] Search a machine by its ID
- [ ] Edit / delete a machine
- [ ] Data analysis & predictions (pandas, scikit-learn) – the "AI" part 🤖

---

Made by [@boillympro-del](https://github.com/boillympro-del) – BTS SIO SLAM student.
