# BudgetTrack

**BudgetTrack** is a simple, extensible personal finance dashboard that helps you track your income and expenses, visualize your financial data, and gain insights into your spending habits. The project uses a Flask backend for file upload and data processing, and a Streamlit frontend for interactive data visualization.

---

## Features

- **Upload CSV** containing your financial transactions.
- **Automatic parsing** of income and expense data.
- **Interactive visualizations** using Plotly (pie charts, bar charts, and more).
- **Session-based state management** for seamless user experience.
- **Bootstrap-styled dashboard** for a modern look.
- **Extensible backend** for adding more analytics or data sources.

---

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/BudgetTrack.git
    cd BudgetTrack
    ```

2. **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Run the Project

1. **Start the Flask backend:**

    Open a terminal and run:
    ```bash
    python budgetTrack.py
    ```
    This will start the backend server (by default at [http://127.0.0.1:5000](http://127.0.0.1:5000)).

2. **Start the Streamlit dashboard:**

    Open a new terminal window and run:
    ```bash
    streamlit run dashboard.py
    ```
    This will open the dashboard in your browser (usually at [http://localhost:8501](http://localhost:8501)).

3. **Use the App:**
    - Upload your CSV/XLSX/TXT file using the dashboard.
    - View your income and expense visualizations.

**Note:**  
Make sure both the Flask server and Streamlit dashboard are running at the same time.

---

## File Format

Your CSV file should have at least the following columns:

| Date       | Category      | Type    | Amount  |
|------------|--------------|---------|---------|
| 2024-01-01 | Salary       | Income  | 5000    |
| 2024-01-02 | Groceries    | Expense | 200     |
| ...        | ...          | ...     | ...     |

- **Type** should be either `Income` or `Expense`.
- **Amount** should be a numeric value.

---

## Project Structure

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

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- [Bootstrap](https://getbootstrap.com/)

---

**Happy Budgeting!**
