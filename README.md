# ABTestAnalyzer: A/B Testing and Data Analytics with Python and SQL

ABTestAnalyzer is a project for performing A/B testing and data analytics using Python and SQL. It utilizes Docker to set up and manage SQL instances, making it easy to handle database operations. The project includes an ETL pipeline to extract data from CSV files, transform it, and load it into a PostgreSQL database. Python scripts are then used to perform A/B testing and generate insights.

## Project Structure

```
ABTestAnalyzer/
├── data/
│   ├── users_a.csv
│   ├── users_b.csv
├── sql/
│   ├── create_tables.sql
│   ├── load_data.sql
├── etl.py
├── ab_testing.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
```

### Prerequisites

- Docker
- Python 3.x
- `pandas`, `psycopg2`, and `scipy` libraries

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ABTestAnalyzer.git
   cd ABTestAnalyzer
   ```

2. **Set up the Docker container:**
   ```bash
   docker-compose up -d
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the ETL script to load data into the database:**
   ```bash
   python etl.py
   ```

2. **Run the A/B testing script to perform analysis:**
   ```bash
   python ab_testing.py
   ```

### Output

The `ab_testing.py` script will print the signup methods for both groups and the result of the Chi-Square test:

```
Signup Methods for Group A:
email     2
social    1
Name: signup_method, dtype: int64

Signup Methods for Group B:
email     2
social    1
Name: signup_method, dtype: int64

Chi-Square Test Result:
Chi2: 0.0, p-value: 1.0
```

### License

This project is licensed under the MIT License.

### Contributing

Contributions are welcome! Please feel free to submit a pull request.

### Contact

For any questions or suggestions, please open an issue or contact the project maintainer.
