DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account TEXT,
    business TEXT,
    amount REAL,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);