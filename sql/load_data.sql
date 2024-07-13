COPY users_a(user_id, signup_date, signup_method)
FROM '/data/users_a.csv' DELIMITER ',' CSV HEADER;

COPY users_b(user_id, signup_date, signup_method)
FROM '/data/users_b.csv' DELIMITER ',' CSV HEADER;
