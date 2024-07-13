FROM postgres:latest
COPY sql/create_tables.sql /docker-entrypoint-initdb.d/
COPY data /data
