# 🌍 NASA NEO (Near-Earth Object) 🚀

This project fetches data from NASA's Near-Earth Object Web Service (NeoWs) API, stores it in a MySQL database, and can be visualized using a Streamlit-based web dashboard.

---

## 📌 Features

- ✅ Fetches asteroid data using NASA's NEO Feed API  
- ✅ Parses and filters essential details like size, velocity, and proximity  
- ✅ Stores asteroid and approach data into structured MySQL tables  
- ✅ Streamlit dashboard (optional) for viewing and analyzing asteroid threats  

---

## 🛠 Technologies Used

- **Python 3.11+**  
- **Requests** – For API calls  
- **MySQL** – Backend database  
- **mysql-connector-python** – Python MySQL driver  
- **Streamlit** – For building the UI dashboard  
- **NASA Open API** – Data source  

---

## 📁 Project Structure

 NASA_NEO_Project
1.  NasaScript.py - Python script to fetch & store asteroid data 
2. Dashboard.py - Streamlit app to visualize asteroid info 
---

## ⚙️ Setup Instructions

### 1. Configure MySQL Database

Create a database named (e.g., `ds`) and ensure the following tables are created:

- `asteroids`
- `close_approach`

These will store up to 10,000 asteroid records fetched via the NASA API.

### 2. Update Database Credentials

Edit the `NasaScript.py` with your MySQL configuration:

python
connection = db.connect(
    host='localhost',
    user='root',
    password='YOUR_PASSWORD',
    database='YOUR_DATABASE_NAME'
)

### 3. Run the Data Fetch Script

python NasaScript.py

This will:

Fetch asteroid data from NASA's API

Parse and transform the data

Populate the MySQL tables with structured entries

### 📊 Database Schema

Asteroids Table

| Column                        | Type      |
|------------------------------|-----------|
| id                           | BIGINT    |
| name                         | VARCHAR   |
| absolute_magnitude_h         | FLOAT     |
| estimated_diameter_min_km    | FLOAT     |
| estimated_diameter_max_km    | FLOAT     |
| is_potentially_hazardous_asteroid | BOOLEAN |

close_approach_date

| Column              | Type   |
|---------------------|--------|
| neo_reference_id    | INT    |
| close_approach_date | DATE   |
| relative_velocity_kmph | FLOAT |
| AU                  | FLOAT  |
| miss_distance_km    | FLOAT  |
| miss_distance_lunar | FLOAT  |
| orbiting_body       | TEXT   |

### 🔑 NASA API Key
You can obtain a free API key from https://api.nasa.gov.
Replace the API_KEY placeholder in your script with your actual key:

API_KEY = "your_actual_nasa_api_key"

## 📌 Sample Use Cases

1.  Astronomical research

2. Hazardous NEO threat analysis

3. Educational visualizations

4. Historical data insights

## 🙋‍♂️ Author
### Eraiyanbu 
GitHub: Eraiyanbu-Git
