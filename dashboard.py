import streamlit as st
import requests 
import pandas as pd
import plotly.express as px
from matplotlib.backends.backend_pdf import PdfPages

# Set the title of the Streamlit app

st.markdown("""
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
""", unsafe_allow_html=True)

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'txt'])

# Create a button to submit the file
if st.button("Submit"):
    if uploaded_file is not None:
        # Send the file to the Flask API
        response = requests.post(
            "http://127.0.0.1:5000/upload",
            files={"file": uploaded_file}
        )
        if response.status_code == 200:
            st.success("File uploaded successfully")
            # Save the income distribution for visualization
            result = response.json()
            st.session_state['income_distribution'] = result.get('income_distribution', {})
            st.session_state['expense_distribution'] = result.get('expense_distribution', {})
            st.session_state['amount_distribution_over_time'] = result.get('amount_distribution_over_time', {})

            print("Income Distribution:", st.session_state['income_distribution'])
        else:
            st.error("File upload failed: {}".format(response.text))

# Show visualization using income_distribution from API
if 'income_distribution' in st.session_state:
    income_distribution = st.session_state.get('income_distribution', {})
    print("Income Distribution:", income_distribution)  
    if income_distribution:
        df = pd.DataFrame({
            'Category': list(income_distribution.keys()),
            'Value': list(income_distribution.values())
        })
        fig = px.pie(df, values='Value', names='Category', title='Income Distribution ', 
                     subtitle='Total Income: {}'.format(sum(income_distribution.values())))
        st.plotly_chart(fig)
    else:
        st.warning("No income distribution data available. Please upload a file first.")

# Show expense distribution if available
if 'expense_distribution' in st.session_state:
    expense_distribution = st.session_state.get('expense_distribution', {})
    if expense_distribution:
        df_expense = pd.DataFrame({
            'Category': list(expense_distribution.keys()),
            'Value': list(expense_distribution.values())
        })
        fig_expense = px.pie(df_expense, values='Value', names='Category', title='Expense Distribution',
                             subtitle='Total Expense: {}'.format(sum(expense_distribution.values())))
        st.plotly_chart(fig_expense)
    else:
        st.warning("No expense distribution data available. Please upload a file first.")

# Show amount distribution over time if available
if 'amount_distribution_over_time' in st.session_state:
    amount_distribution_over_time = st.session_state.get('amount_distribution_over_time', {})
    if amount_distribution_over_time:
        df_time = pd.DataFrame({
            'Date': list(amount_distribution_over_time.keys()),
            'Amount': list(amount_distribution_over_time.values())
        })
        fig_time = px.line(df_time, x='Date', y='Amount', title='Amount Distribution Over Time')
        st.plotly_chart(fig_time)
    else:
        st.warning("No amount distribution over time data available. Please upload a file first.")

total_income = sum(st.session_state.get('income_distribution', {}).values())
total_expense = sum(st.session_state.get('expense_distribution', {}).values())
total_savings = total_income - total_expense

st.markdown(f"""
    <div class="container mt-4">
        <div class="row">
            <div class="col-md-4">
                <div class="card text-white bg-primary mb-3">
                    <div class="card-header">Total Income</div>
                    <div class="card-body">
                        <h5 class="card-title">${total_income:,.2f}</h5>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white bg-danger mb-3">
                    <div class="card-header">Total Expense</div>
                    <div class="card-body">
                        <h5 class="card-title">${total_expense:,.2f}</h5>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white bg-success mb-3">
                    <div class="card-header">Total Savings</div>
                    <div class="card-body">
                        <h5 class="card-title">${total_savings:,.2f}</h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)