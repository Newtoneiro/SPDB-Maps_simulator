CREATE TABLE STOPS (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  coordinates POINT NOT NULL
);