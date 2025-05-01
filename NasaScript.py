import streamlit as st
import pandas as pd
from datetime import datetime
import mysql.connector as db
 
# Connect to MySQL Database
connection = db.connect(
    host='localhost',
    user='root',
    password='Anbu_0820',
    database='ds'
)
cursor = connection.cursor()
 
# Streamlit App Configuration
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🚀 NASA Asteroid Tracker 🌠</h1>", unsafe_allow_html=True)
st.divider()
 
# Sidebar Menu
with st.sidebar:
    selected = st.radio("Choose an Option:", ["Filter Criteria", "Queries"])
 
# ------------------------ FILTER SECTION ------------------------
if selected == "Filter Criteria":
    st.sidebar.title("Filters")
 
    # Filter Inputs
    start_date = st.sidebar.date_input("Close Approach Start Date", datetime(2024, 1, 1))
    end_date = st.sidebar.date_input("Close Approach End Date", datetime(2025, 1, 1))
 
    au_min, au_max = st.sidebar.slider("Astronomical Units (AU)", 0.0, 1.0, (0.0, 0.5))
    lunar_min, lunar_max = st.sidebar.slider("Lunar Distances (LD)", 0.0, 100.0, (0.0, 50.0))
    velocity_min, velocity_max = st.sidebar.slider("Relative Velocity (km/h)", 0.0, 100000.0, (0.0, 50000.0))
    diameter_min, diameter_max = st.sidebar.slider("Estimated Diameter (km)", 0.0, 20.0, (0.0, 10.0))
    hazardous_state = st.sidebar.selectbox("Hazardous State", options=["All", "Hazardous", "Non-Hazardous"])
 
    # Filter Button
    if st.sidebar.button("Filter Data"):
        # SQL Query with 12 placeholders
        query = """
        SELECT
            asteroids.name,
            close_approach.close_approach_date,
            close_approach.AU,
            close_approach.miss_distance_km,
            close_approach.miss_distance_lunar,
            close_approach.relative_velocity_kmph,
            asteroids.estimated_diameter_min_km,
            asteroids.estimated_diameter_max_km,
            asteroids.is_potentially_hazardous_asteroid
        FROM close_approach
        JOIN asteroids ON close_approach.neo_reference_id = asteroids.id
        WHERE close_approach.close_approach_date BETWEEN %s AND %s
        AND close_approach.AU BETWEEN %s AND %s
        AND close_approach.miss_distance_lunar BETWEEN %s AND %s
        AND close_approach.relative_velocity_kmph BETWEEN %s AND %s
        AND asteroids.estimated_diameter_min_km BETWEEN %s AND %s
        AND asteroids.estimated_diameter_max_km BETWEEN %s AND %s
        """
 
        # Add Hazardous State Filter
        if hazardous_state == "Hazardous":
            query += " AND asteroids.is_potentially_hazardous_asteroid = 1"
        elif hazardous_state == "Non-Hazardous":
            query += " AND asteroids.is_potentially_hazardous_asteroid = 0"
 
        # Parameters (matching 12 %s placeholders)
        params = (
            start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"),
            float(au_min), float(au_max),
            float(lunar_min), float(lunar_max),
            float(velocity_min), float(velocity_max),
            float(diameter_min), float(diameter_max),
            float(diameter_min), float(diameter_max)
        )
 
        # Execute Query
        cursor.execute(query, params)
        rows = cursor.fetchall()
 
        # Display Results
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        st.subheader("Filtered Results")
        st.dataframe(df)
 
# ------------------------ QUERIES SECTION ------------------------
elif selected == "Queries":
    st.sidebar.title("Choose Query")
 
    # Query Options
    query_options = [
        "Count how many times each asteroid has approached Earth",
        "Average velocity of each asteroid over multiple approaches",
        "List top 10 fastest asteroids",
        "Find potentially hazardous asteroids that have approached Earth more than 3 times",
        "Find the month with the most asteroid approaches",
        "Get the asteroid with the fastest ever approach speed",
        "Sort asteroids by maximum estimated diameter (descending)",
        "Asteroids whose closest approach is getting nearer over time",
        "Display the name of each asteroid along with the date and miss distance of its closest approach to Earth",
        "List names of asteroids that approached Earth with velocity > 50,000 km/h",
        "Count how many approaches happened per month",
        "Find asteroid with the highest brightness (lowest magnitude value)",
        "Get number of hazardous vs non-hazardous asteroids",
        "Find asteroids that passed closer than the Moon (lesser than 1 LD)",
        "Find asteroids that came within 0.05 AU (astronomical distance)",
        "Find the asteroid with the highest absolute magnitude (brightest asteroid)",
        "List the top 5 asteroids with the largest estimated diameter",
        "Count the number of asteroids that have approached Earth more than 5 times",
        "Find the asteroid with the longest time between two consecutive close approaches",
        "List asteroids that have approached Earth within 0.05 AU and have a diameter greater than 1 km"
    ]
 
    # Select Query
    query_choice = st.sidebar.selectbox("Select Query", query_options)
 
    # SQL Queries
    queries = {
        "Count how many times each asteroid has approached Earth": """
            SELECT asteroids.name, COUNT(*) AS approach_count
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            GROUP BY asteroids.name
            ORDER BY approach_count DESC
        """,
        "Average velocity of each asteroid over multiple approaches": """
            SELECT asteroids.name, AVG(close_approach.relative_velocity_kmph) AS avg_velocity
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            GROUP BY asteroids.name
            ORDER BY avg_velocity DESC
        """,
        "List top 10 fastest asteroids": """
            SELECT asteroids.name, close_approach.relative_velocity_kmph
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            ORDER BY close_approach.relative_velocity_kmph DESC
            LIMIT 10
        """,
        "Find potentially hazardous asteroids that have approached Earth more than 3 times": """
            SELECT asteroids.name, COUNT(*) AS approach_count
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            WHERE asteroids.is_potentially_hazardous_asteroid = 1
            GROUP BY asteroids.name
            HAVING approach_count > 3
        """,
        "Find the month with the most asteroid approaches": """
            SELECT MONTH(close_approach.close_approach_date) AS month, COUNT(*) AS total_approaches
            FROM close_approach
            GROUP BY month
            ORDER BY total_approaches DESC
            LIMIT 1
        """,
        "Get the asteroid with the fastest ever approach speed": """
            SELECT asteroids.name, close_approach.relative_velocity_kmph
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            ORDER BY close_approach.relative_velocity_kmph DESC
            LIMIT 1
        """,
        "Sort asteroids by maximum estimated diameter (descending)": """
            SELECT asteroids.name, asteroids.estimated_diameter_max_km
            FROM asteroids
            ORDER BY asteroids.estimated_diameter_max_km DESC
        """,
        "Asteroids whose closest approach is getting nearer over time": """
            SELECT asteroids.name, close_approach.close_approach_date, close_approach.miss_distance_km
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            ORDER BY close_approach.close_approach_date, close_approach.miss_distance_km ASC
        """,
        "Display the name of each asteroid along with the date and miss distance of its closest approach to Earth": """
            SELECT asteroids.name, close_approach.close_approach_date, close_approach.miss_distance_km
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            ORDER BY close_approach.miss_distance_km ASC
        """,
        "List names of asteroids that approached Earth with velocity > 50,000 km/h": """
            SELECT asteroids.name, close_approach.relative_velocity_kmph
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            WHERE close_approach.relative_velocity_kmph > 50000
            ORDER BY close_approach.relative_velocity_kmph DESC
        """,
        "Count how many approaches happened per month": """
            SELECT MONTH(close_approach.close_approach_date) AS month, COUNT(*) AS num_approaches
            FROM close_approach
            GROUP BY month
            ORDER BY num_approaches DESC
        """,
        "Find asteroid with the highest brightness (lowest magnitude value)": """
            SELECT asteroids.name, asteroids.absolute_magnitude_h
            FROM asteroids
            ORDER BY asteroids.absolute_magnitude_h ASC
            LIMIT 1
        """,
        "Get number of hazardous vs non-hazardous asteroids": """
            SELECT asteroids.is_potentially_hazardous_asteroid, COUNT(*) AS count
            FROM asteroids
            GROUP BY asteroids.is_potentially_hazardous_asteroid
        """,
        "Find asteroids that passed closer than the Moon (lesser than 1 LD)": """
            SELECT asteroids.name, close_approach.close_approach_date, close_approach.miss_distance_lunar
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            WHERE close_approach.miss_distance_lunar < 1
            ORDER BY close_approach.miss_distance_lunar ASC
        """,
        "Find asteroids that came within 0.05 AU (astronomical distance)": """
            SELECT asteroids.name, close_approach.close_approach_date, close_approach.AU
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            WHERE close_approach.AU < 0.05
            ORDER BY close_approach.AU ASC
        """,
        # New queries added:
        "Find the asteroid with the highest absolute magnitude (brightest asteroid)": """
            SELECT asteroids.name, asteroids.absolute_magnitude_h
            FROM asteroids
            ORDER BY asteroids.absolute_magnitude_h ASC
            LIMIT 1;
        """,
        "List the top 5 asteroids with the largest estimated diameter": """
            SELECT asteroids.name, asteroids.estimated_diameter_max_km
            FROM asteroids
            ORDER BY asteroids.estimated_diameter_max_km DESC
            LIMIT 5;
        """,
        "Count the number of asteroids that have approached Earth more than 5 times": """
            SELECT asteroids.name, COUNT(*) AS approach_count
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            GROUP BY asteroids.name
            HAVING approach_count > 5;
        """,
        "Find the asteroid with the longest time between two consecutive close approaches": """
            SELECT asteroids.name, MAX(DATEDIFF(close_approach.close_approach_date, prev_approach.close_approach_date)) AS max_time_gap
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            JOIN close_approach AS prev_approach ON asteroids.id = prev_approach.neo_reference_id
            WHERE close_approach.close_approach_date > prev_approach.close_approach_date
            GROUP BY asteroids.name
            ORDER BY max_time_gap DESC
            LIMIT 1;
        """,
        "List asteroids that have approached Earth within 0.05 AU and have a diameter greater than 1 km": """
            SELECT asteroids.name, close_approach.AU, asteroids.estimated_diameter_max_km
            FROM close_approach
            JOIN asteroids ON asteroids.id = close_approach.neo_reference_id
            WHERE close_approach.AU < 0.05
            AND asteroids.estimated_diameter_max_km > 1;
        """
    }
 
    # Execute and Display Query
    if query_choice:
        query = queries[query_choice]
        cursor.execute(query)
        rows = cursor.fetchall()
 
        # Display Results
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)
        st.subheader(query_choice)
        st.dataframe(df)
 
# Cleanup
cursor.close()
connection.close()
 