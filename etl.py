import pandas as pd
import psycopg2

# Load data from CSV files
users_a_df = pd.read_csv('data/users_a.csv')
users_b_df = pd.read_csv('data/users_b.csv')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="abtestdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Load data into SQL tables
for index, row in users_a_df.iterrows():
    cur.execute(
        "INSERT INTO users_a (user_id, signup_date, signup_method) VALUES (%s, %s, %s)",
        (row['user_id'], row['signup_date'], row['signup_method'])
    )

for index, row in users_b_df.iterrows():
    cur.execute(
        "INSERT INTO users_b (user_id, signup_date, signup_method) VALUES (%s, %s, %s)",
        (row['user_id'], row['signup_date'], row['signup_method'])
    )

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
