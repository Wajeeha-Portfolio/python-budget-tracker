# 💰 BudgetTrack  

> **BudgetTrack** is a simple, extensible personal finance dashboard that helps you track your income and expenses, visualize your financial data, and gain insights into your spending habits.  
> Built with a **Flask** backend for file upload & data processing and a **Streamlit** frontend for interactive data visualization.  

---

## ✨ Features  

- 📂 **Upload CSV** containing your financial transactions.  
- 🔍 **Automatic parsing** of income and expense data.  
- 📊 **Interactive visualizations** using Plotly (pie charts, bar charts, and more).  
- 🔄 **Session-based state management** for seamless user experience.  
- 🎨 **Bootstrap-styled dashboard** for a modern look.  
- 🔧 **Extensible backend** for adding more analytics or data sources.  

---

## 🚀 Getting Started  

### 📋 Prerequisites  
- Python **3.8+**  
- [pip](https://pip.pypa.io/en/stable/)  

### 📥 Installation  

1. **Clone the repository:**  
    ```bash
    git clone https://github.com/Wajeeha-Portfolio/python-budget-tracker.git
    cd BudgetTrack
    ```
---

## ▶️ How to Run the Project  

1. **Start the Flask backend:**  
    ```bash
    python budgetTrack.py
    ```
    Backend runs at: [http://127.0.0.1:5000](http://127.0.0.1:5000)  

2. **Start the Streamlit dashboard:**  
    ```bash
    streamlit run dashboard.py
    ```
    Dashboard opens at: [http://localhost:8501](http://localhost:8501)  

3. **Use the App:**  
    - 📤 Upload your CSV/XLSX/TXT file.  
    - 📈 View your income and expense visualizations.  

> ⚠️ **Note:** Both the Flask server and Streamlit dashboard must run simultaneously.  

---

## 📄 File Format  

| Date       | Category   | Type    | Amount  |
|------------|-----------|---------|---------|
| 2024-01-01 | Salary    | Income  | 5000    |
| 2024-01-02 | Groceries | Expense | 200     |
| ...        | ...       | ...     | ...     |

- **Type** → `Income` or `Expense`  
- **Amount** → Numeric value  

---

## 🗂 Project Structure  

```
BudgetTrack/
│
├── budgetTrack.py         # Flask app entry point
├── upload_handler.py      # Flask blueprint for file upload and processing
├── dashboard.py           # Streamlit dashboard
├── uploads/               # Uploaded files (auto-created)
├── .gitignore
└── README.md
```

---

## 🤝 Contributing  

Contributions are welcome!  
Please **open an issue** or **submit a pull request** for improvements or bug fixes.  

---

## 🙌 Acknowledgements  

- [Flask](https://flask.palletsprojects.com/)  
- [Streamlit](https://streamlit.io/)  
- [Plotly](https://plotly.com/python/)  
- [Bootstrap](https://getbootstrap.com/)  

---

**💡 Happy Budgeting!**  
