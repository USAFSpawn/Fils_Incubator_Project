-- 🐣 Incubator Project - Sensor Logging Database

CREATE TABLE incubator (
    timestamp TEXT PRIMARY KEY,
    temperature REAL,
    humidity REAL
);

CREATE INDEX idx_timestamp ON incubator(timestamp);
