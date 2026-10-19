"""Local SQLite storage for the kiosk; no separate database server is required."""
import re
import sqlite3

from .config import DB_PATH, DATA_DIR

IntegrityError = sqlite3.IntegrityError


class _Cursor:
    def __init__(self, cursor):
        self._cursor = cursor

    @property
    def lastrowid(self):
        return self._cursor.lastrowid

    @property
    def rowcount(self):
        return self._cursor.rowcount

    def execute(self, sql, params=()):
        sql = sql.replace("%s", "?").replace(" FOR UPDATE", "")
        sql = re.sub(
            r"ON DUPLICATE KEY UPDATE name=VALUES\(name\)",
            "ON CONFLICT(email) DO UPDATE SET name=excluded.name",
            sql,
            flags=re.IGNORECASE,
        )
        self._cursor.execute(sql, params)
        return self

    def fetchone(self):
        row = self._cursor.fetchone()
        return dict(row) if row is not None else None

    def fetchall(self):
        return [dict(row) for row in self._cursor.fetchall()]


class _Connection:
    def __init__(self, connection):
        self._connection = connection

    def cursor(self, dictionary=False):
        return _Cursor(self._connection.cursor())

    def start_transaction(self):
        self._connection.execute("BEGIN")

    def commit(self):
        self._connection.commit()

    def rollback(self):
        self._connection.rollback()

    def close(self):
        self._connection.close()


def connect():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return _Connection(connection)


def initialize():
    """Create the local kiosk tables. Existing SQLite orders are preserved."""
    db = connect()
    try:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
            id TEXT NOT NULL PRIMARY KEY,
            idempotency_key TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL,
            status TEXT NOT NULL,
            total NUMERIC NOT NULL,
            payload TEXT NOT NULL
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS customer_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS customer_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL DEFAULT '',
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def database_health():
    db = connect()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT sqlite_version() AS version")
        row = cursor.fetchone()
        return {"database": "SQLite", "databaseVersion": row["version"], "connection": "connected"}
    finally:
        db.close()
