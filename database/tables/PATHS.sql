CREATE TABLE PATHS (
  id INTEGER PRIMARY KEY,
  from_node_id INTEGER NOT NULL,
  to_node_id INTEGER NOT NULL,
  distance FLOAT(10,2) NOT NULL,
  travel_time FLOAT(10,2) NOT NULL,
  CONSTRAINT fk_from_node FOREIGN KEY (from_node_id) REFERENCES NODES(id),
  CONSTRAINT fk_to_node FOREIGN KEY (to_node_id) REFERENCES NODES(id)
);