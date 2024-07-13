import psycopg2
import pandas as pd
from scipy import stats

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="abtestdb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Extract data for A/B testing
cur.execute("SELECT * FROM users_a")
users_a = cur.fetchall()
cur.execute("SELECT * FROM users_b")
users_b = cur.fetchall()

# Close connection
cur.close()
conn.close()

# Convert data to DataFrame
columns = ['user_id', 'signup_date', 'signup_method']
users_a_df = pd.DataFrame(users_a, columns=columns)
users_b_df = pd.DataFrame(users_b, columns=columns)

# Perform A/B testing
signup_methods_a = users_a_df['signup_method'].value_counts()
signup_methods_b = users_b_df['signup_method'].value_counts()

# Print results
print("Signup Methods for Group A:")
print(signup_methods_a)
print("\nSignup Methods for Group B:")
print(signup_methods_b)

# Perform Chi-Square Test
contingency_table = pd.DataFrame([signup_methods_a, signup_methods_b]).fillna(0)
chi2, p, _, _ = stats.chi2_contingency(contingency_table)

print("\nChi-Square Test Result:")
print(f"Chi2: {chi2}, p-value: {p}")
