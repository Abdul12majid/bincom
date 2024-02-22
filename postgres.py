import pandas as pd
import psycopg2  # For connecting to your database

# Replace these with your database credentials
HOST = "dpg-cnbdh7ud3nmc73cv46l0-a"
DBNAME = "bincom_data"
USER = "majid"
PASSWORD = "4B9hXIJpIHg4pjuGZZOWPFxdq5CpTFir"

# 1. Open and parse the HTML file
with open("dataFile.html", "r") as file:
    html_content = file.read()

df = pd.read_html(html_content)[0]  # Assuming the first table is needed

# 2. Extract color data and count frequencies
colors = df['COLOURS'].str.split(', ')
color_freqs = {}
for day_colors in colors:
    for color in day_colors:
        color = color.lower()  # lowercase for case-insensitive counting
        color_freqs[color] = color_freqs.get(color, 0) + 1

# 3. Connect to your database
conn = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)

# 4. Create table (adjust column names if needed)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS color_frequencies (
    color VARCHAR(255) PRIMARY KEY,
    frequency INTEGER NOT NULL
);
""")
conn.commit()

# 5. Insert data into the table
for color, frequency in color_freqs.items():
    cur.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))
conn.commit()

# 6. Close the connection
cur.close()
conn.close()

# 7. Optional: Print color frequencies for verification
print("Saved color frequencies to your database:")
print(color_freqs)
