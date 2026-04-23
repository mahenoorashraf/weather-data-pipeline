🌤️ Weather Data Pipeline & Dashboard System
📌 Project Overview

This project is an end-to-end Weather Data Pipeline that fetches real-time weather data using an API, processes it using an ETL pipeline, stores it in a SQLite database, and visualizes it using a Streamlit dashboard.

It demonstrates concepts of Data Engineering, ETL processes, logging, scheduling, and data visualization.

🚀 Features
🔄 Automated ETL pipeline for weather data ingestion
🌐 Fetches real-time weather data using API
🗄️ Stores structured data in SQLite database
📊 Streamlit dashboard for visualization
📈 Interactive charts (temperature & humidity trends)
🔍 City-wise filtering and analysis
⏱️ Scheduler for automatic data updates
🧾 Logging system for monitoring and debugging
🛠️ Tech Stack
Python 🐍
SQLite 🗄️
Streamlit 📊
Pandas 📈
Requests 🌐
Logging module 🧾
Schedule ⏰
📂 Project Structure

Weather Project/
│── src/
│   ├── api\_client.py
│   ├── database.py
│   ├── etl\_pipeline.py
│   ├── dashboard.py
│   ├── logger.py
│   ├── monitor.py
│   ├── reporter.py
│   ├── validators.py
│   ├── scheduler.py
│   ├── main.py
│── weather.db
│── logs/
│── README.md

⚙️ How It Works
ETL Pipeline
Extracts weather data from API
Transforms and validates data
Loads data into SQLite database
Scheduler
Runs ETL automatically at fixed intervals
Dashboard
Reads data from database
Displays charts and KPIs
Provides interactive filters
▶️ How to Run the Project
1. Clone Repository
git clone https://github.com/your-username/weather-project.git
2. Install Dependencies
pip install -r requirements.txt
3. Run ETL Pipeline
python etl_pipeline.py
4. Run Streamlit Dashboard
streamlit run dashboard.py
📊 Dashboard Preview
🌡️ Temperature Trends
💧 Humidity Trends
📍 City-wise analysis
📈 Interactive charts
🔍 Filters for cities & time
📌 Key Learnings
ETL pipeline design
API integration
Database management (SQLite)
Data validation techniques
Streamlit dashboard creation
Logging and monitoring system
👨‍💻 Author

Mahenoor Ashraf
MCA Student | Data Science Intern | Developers Arena

⭐ Future Improvements
Real-time live dashboard updates
Deployment on Streamlit Cloud
Use PostgreSQL instead of SQLite
Add machine learning weather prediction
📌 Note

This project is developed for learning and academic purposes to demonstrate Data Engineering concepts.
