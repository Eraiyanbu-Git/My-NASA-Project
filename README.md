# 🌍 NASA NEO (Near-Earth Object)  🚀

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

NASA_NEO_Project/ │ ├── NasaScript.py # Python script to fetch & store asteroid data ├── dashboard.py # Streamlit app to visualize asteroid info ├── requirements.txt # Python dependencies └── README.md # You're reading it now!

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/NASA-NEO-Streamlit-MySQL.git
cd NASA-NEO-Streamlit-MySQL
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Ensure MySQL is installed and running on your system.

3. Configure MySQL Database
Create a database (e.g., ds)

Update credentials in NasaScript.py:

python
Copy
Edit
connection = db.connect(
    host='localhost',
    user='root',
    password='YOUR_PASSWORD',
    database='ds'
)
4. Run Data Fetch Script
bash
Copy
Edit
python NasaScript.py
This will:

Fetch asteroid data from NASA API

Create two tables: asteroids and close_approach

Populate them with up to 10,000 records

5. Launch the Dashboard (Optional)
bash
Copy
Edit
streamlit run dashboard.py
📊 Database Schema
asteroids table:
Column	Type
id	BIGINT
name	VARCHAR
absolute_magnitude_h	FLOAT
estimated_diameter_min_km	FLOAT
estimated_diameter_max_km	FLOAT
is_potentially_hazardous_asteroid	BOOLEAN

close_approach table:
Column	Type
neo_reference_id	BIGINT
close_approach_date	DATE
relative_velocity_kmph	FLOAT
AU	FLOAT
miss_distance_km	FLOAT
miss_distance_lunar	FLOAT
orbiting_body	TEXT

🔑 NASA API Key
You can get a free NASA API key from: https://api.nasa.gov

Replace the placeholder API_KEY in your script with your own key:

python
Copy
Edit
API_KEY = "your_api_key_here"
📌 Sample Use Cases
Astronomical research

Hazard analysis

Educational visualization tools

Historical data insights on NEOs


🙋‍♂️ Author
Your Name

GitHub: Eraiyanbu-Git
