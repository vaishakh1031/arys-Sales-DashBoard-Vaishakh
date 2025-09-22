**Sales Data Dashboard Project**

# 1. Project Scope & Overview
This project is a full-stack web application designed to analyze and visualize sales data. The primary goal is to transform a raw sales dataset into an interactive and insightful dashboard. The scope covers the entire data pipeline, from cleaning and processing the data to serving it via a REST API and rendering it on a dynamic frontend.

The project is broken down into three main components:

  ● Data Preprocessing: A Python script cleans, transforms, and prepares the raw sales data for analysis.

  ● Backend API: A Flask-based web server that loads the processed data and exposes it through several endpoints.

  ● Frontend Dashboard: A single-page web application that fetches data from the API and visualizes it using various charts and key performance indicators (KPIs).

# 2. Features
-> KPI Cards: Quick overview of Total Sales, Total Orders, and Average Order Value.

-> Sales Trend Analysis: A line chart visualizing sales performance over time.

-> Product Performance: A bar chart showing sales distribution across different product lines.

-> Geographical Sales Data: A pie chart illustrating which countries contribute the most to sales.

-> Order Status Summary: A donut chart breaking down the status of all orders (e.g., Shipped, In Process).

-> Top Customer Identification: A list displaying the top 5 customers by total sales.

# 3. Tech Stack

  ● Component
  ● Technology
  ● Data Processing
  ● Python, Pandas, Jupyter Notebook
  ● Backend
  ● Flask, Flask-CORS
  ● Frontend
  ● HTML, JavaScript, Tailwind CSS, Chart.js

# 4. Project Structure

    sales-dashboard/
    ├── .gitignore

    ├── backend/

    │   ├── app.py

    │   └── sales_data_processed.csv  (Generated)

    ├── data_preprocessing/

    │   ├── Sales_Data_Preprocessing.ipynb

    │   └── sales_data.csv            (Raw data)

    ├── frontend/

    │   └── index.html

    └── README.md

# 5. Setup and Run Instructions
Step 1: Data Preprocessing
Place your raw sales_data.csv file inside the data_preprocessing/ directory.

Install the required Python libraries:

pip install pandas jupyter

Run the Sales_Data_Preprocessing.ipynb notebook to clean the data and generate backend/sales_data_processed.csv.

Step 2: Start the Backend Server
Navigate to the backend/ directory.

Install the required libraries:
            
            pip install Flask Flask-Cors pandas

Run the Flask server:

            python app.py

The server will be running at http://127.0.0.1:5001. Keep this terminal open.

Step 3: Launch the Frontend.
Navigate to the frontend/ directory.

Open the index.html file in your web browser. The dashboard should load and display the data.