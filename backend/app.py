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
    # Endpoint 2: Sales Over Time (Monthly)
@app.route('/api/sales_over_time', methods=['GET'])
def sales_over_time():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500

    df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M').astype(str)
    sales_by_month = df.groupby('YEAR_MONTH')['SALES'].sum().reset_index()
    sales_by_month = sales_by_month.sort_values('YEAR_MONTH')
    
    # Format for charting library
    chart_data = {
        'labels': sales_by_month['YEAR_MONTH'].tolist(),
        'values': sales_by_month['SALES'].tolist()
    }
    return jsonify(chart_data)

# Endpoint 3: Sales by Product Line
@app.route('/api/sales_by_productline', methods=['GET'])
def sales_by_productline():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500
        
    sales_by_cat = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
    
    chart_data = {
        'labels': sales_by_cat.index.tolist(),
        'values': sales_by_cat.values.tolist()
    }
    return jsonify(chart_data)
    
# Endpoint 4: Sales by Country
@app.route('/api/sales_by_country', methods=['GET'])
def sales_by_country():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500

    sales_by_country = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(10) # Top 10
    
    chart_data = {
        'labels': sales_by_country.index.tolist(),
        'values': sales_by_country.values.tolist()
    }
    return jsonify(chart_data)
    
# Endpoint 5: Order Status Distribution
@app.route('/api/order_status', methods=['GET'])
def order_status():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500
        
    status_counts = df['STATUS'].value_counts()
    
    chart_data = {
        'labels': status_counts.index.tolist(),
        'values': status_counts.values.tolist()
    }
    return jsonify(chart_data)

# Endpoint 6: Top 5 Customers by Sales
@app.route('/api/top_customers', methods=['GET'])
def top_customers():
    if df.empty:
        return jsonify({"error": "Data not available"}), 500
        
    top_cust = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(5)
    
    customer_data = {
        'labels': top_cust.index.tolist(),
        'values': top_cust.values.tolist()
    }
    return jsonify(customer_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
