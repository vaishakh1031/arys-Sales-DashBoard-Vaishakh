from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

# Initialize Flask App
app = Flask(__name__)
# Enable CORS for frontend requests
CORS(app)

# Load the processed data
try:
    df = pd.read_csv('sales_data_processed.csv')
    # Ensure ORDERDATE is in datetime format for time-based operations
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
except FileNotFoundError:
    print("Error: 'sales_data_processed.csv' not found. Make sure you have run the preprocessing notebook.")
    df = pd.DataFrame() # Create an empty dataframe to avoid crashing the app

# --- API Endpoints ---

@app.route('/')
def home():
    return "Sales Data API is running!"

# Endpoint 1: Key Performance Indicators (KPIs)
@app.route('/api/kpis', methods=['GET'])
def get_kpis():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500
        
    total_sales = df['SALES'].sum()
    total_orders = df['ORDERNUMBER'].nunique()
    total_customers = df['CUSTOMERNAME'].nunique()
    avg_order_value = total_sales / total_orders if total_orders > 0 else 0
    
    kpis = {
        'total_sales': f"${total_sales:,.2f}",
        'total_orders': f"{total_orders:,}",
        'total_customers': f"{total_customers:,}",
        'average_order_value': f"${avg_order_value:,.2f}"
    }
    return jsonify(kpis)