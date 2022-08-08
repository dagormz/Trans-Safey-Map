CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE INCIDENTS
(
    ID uuid DEFAULT uuid_generate_v4 (),
    CITY VARCHAR,
    STATE CHAR(2),
    YEAR INT,
    SEVERITY VARCHAR
);

COPY INCIDENTS FROM '/run/data/summary_data.csv' WITH (FORMAT csv, HEADER TRUE);