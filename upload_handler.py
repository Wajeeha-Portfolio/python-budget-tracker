from flask import Flask, request, jsonify, Blueprint
from werkzeug.utils import secure_filename
import os
import csv
import pandas as pd

app = Flask(__name__)
upload_handler = Blueprint('upload_handler', __name__)


# Set upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_handler.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        total_income = 0
        total_expense = 0

        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row
            rows = []
            type_index = header.index('Type') if 'Type' in header else None
            if type_index is None:
                return jsonify({'error': 'Invalid file format'}), 400
            amount_index = header.index('Amount') if 'Amount' in header else None
            if amount_index is None:
                return jsonify({'error': 'Invalid file format'}), 400
            income_distribution = {}
            expense_distribution = {}
            amount_distribution_over_time = {}
            total_amount = 0

            for row in reader:
                if row[type_index].lower() == 'income':
                    income_distribution[row[1]] = float(row[amount_index])
                    total_amount += float(row[amount_index])
                elif row[type_index].lower() == 'expense':
                    expense_distribution[row[1]] = float(row[amount_index])
                    total_amount -= float(row[amount_index])
                
                amount_distribution_over_time[row[0]] = total_amount
                    

            print(f'amount_distribution_over_time: {amount_distribution_over_time}')
            print(f'Income Distribution: {income_distribution}')
            print(f'Expense Distribution: {expense_distribution}')
        # Return income_distribution in the response so Streamlit can save it in session state
        return jsonify({
            'message': 'File uploaded successfully',
            # 'filename': filename,
            'income_distribution': income_distribution,
            'expense_distribution': expense_distribution,
            'amount_distribution_over_time': amount_distribution_over_time,
            # 'preview': rows[:5]
        }), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400
