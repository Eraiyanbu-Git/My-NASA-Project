# 🌍 NASA NEO (Near-Earth Object) Data Pipeline 🚀

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
NasaScript.py - Python script to fetch & store asteroid data 
Dashboard.py - Streamlit app to visualize asteroid info 
--- 
## ⚙️ Setup Instructions
1. Configure MySQL Database
Create a database with Asteroid and Close_approach Tables and
Populate them with up to 10,000 records
2. Update credentials in NasaScript.py:
connection = db.connect(
	host='localhost',

	user='root',

	password='YOUR_PASSWORD',

	database='YOUR_DATABASE_NAME')


3. Run Data Fetch Script

NasaScript.py

This will: Fetch asteroid data from NASA API
   
📊 Database Schema

**Asteroids table:

**Column**                            **Type**

Id	                                   BIGINT

Name	                               VARCHAR

Absolute_magnitude_h	               FLOAT

Estimated_diameter_min_km              FLOAT

Estimated_diameter_max_km	           FLOAT

Is_potentially_hazardous_asteroid	   BOOLEAN
 
**close_approach table:

**Column**	                           **Type**

Neo_reference_id	                     BIGINT

Close_approach_date	                     DATE

Relative_velocity_kmph	                 FLOAT

AU	                                     FLOAT
 
Miss_distance_km	                     FLOAT

Miss_distance_lunar			             FLOAT

Orbiting_body				             TEXT
 
🔑 NASA API Key

You can get a free NASA API key from: https://api.nasa.gov
Replace the placeholder API_KEY in your script with your own key:
 
📌 Sample Use Cases

Astronomical research 
Hazard analysis
Educational visualization tools
Historical data insights on NEOs
 
🙋‍♂️ Author
Eraiyanbu 
GitHub: Eraiyanbu-Git
