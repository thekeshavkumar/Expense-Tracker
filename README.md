# 💰 Expense Tracker (CLI-Based) in Python

A simple command-line based **Expense Tracker** built using Python. It helps you track your daily spending, categorize expenses, and view summaries — all stored locally using CSV and managed with `pandas`.

---

## 🛠️ Features

- ➕ Add new expenses (with amount, category, date, and description)
- 📋 View all expenses in a readable tabular format
- 🔍 Filter expenses by category
- 📊 Show summary of total spending by category
- 🧾 Data stored in CSV for easy access and portability

---

## 📂 Project Structure

```

expense\_tracker/
├── tracker.py            # Main Python script
├── expenses.csv          # Automatically created data file
└── requirements.txt      # List of dependencies

````

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8+
- pip package manager

### 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/thekeshavkumar/expense-tracker.git
   cd expense-tracker
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**

   ```bash
   python tracker.py
   ```

---

## 🖥️ Example Usage

```
💰 Expense Tracker Menu
1. Add Expense
2. View All Expenses
3. View Expenses by Category
4. Show Summary
5. Exit
Choose an option (1-5): 1
```

---

## 📦 Dependencies

* [pandas](https://pandas.pydata.org/)
* [tabulate](https://pypi.org/project/tabulate/)

---

## 🧠 Concepts Used

* File I/O with CSV
* Command-line input/output
* Python functions and flow control
* Data handling with pandas
* Terminal UI with tabulate

---

## 📌 Future Improvements (Suggestions)

* Add a delete or edit expense option
* GUI version using `tkinter` or `streamlit`
* Monthly budget tracker
* Export to PDF or Excel

---

## 🧑‍💻 Author

**Keshav** — *Python Enthusiast & Student*

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
