"""
Day 05 - Talking to a real database using sqlite3
Creates a tiny local database, inserts tag readings, then queries them.
"""

import sqlite3


def setup_database(conn):
    """Create the table if it doesn't exist yet."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag_name TEXT NOT NULL,
            area TEXT NOT NULL,
            value REAL NOT NULL
        )
    """)
    conn.commit()


def insert_reading(conn, tag_name, area, value):
    """Insert one tag reading. Uses ? placeholders - never insert values directly into the SQL string."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tags (tag_name, area, value) VALUES (?, ?, ?)",
        (tag_name, area, value)
    )
    conn.commit()


def get_readings_by_area(conn, area):
    """Return all rows for a given area."""
    cursor = conn.cursor()
    cursor.execute("SELECT tag_name, area, value FROM tags WHERE area = ?", (area,))
    return cursor.fetchall()


def get_average_value(conn, area):
    """Let the database do the math - faster than pulling all rows and averaging in Python."""
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(value) FROM tags WHERE area = ?", (area,))
    result = cursor.fetchone()   # ekta row expect korchi, tai fetchone()
    return result[0]


def main():
    conn = sqlite3.connect("python-daily/week1/tags.db")
    setup_database(conn)

    # Kichu sample reading insert korlam (real life e ei data PLC/OPC theke ashto)
    readings = [
        ("WWTP_FIT_101", "WWTP", 452.7),
        ("WWTP_FIT_102", "WWTP", 398.2),
        ("CLEARWELL_LIT_201", "CLEARWELL", 78.5),
    ]
    for tag_name, area, value in readings:
        insert_reading(conn, tag_name, area, value)

    print("--- All WWTP readings ---")
    for row in get_readings_by_area(conn, "WWTP"):
        tag_name, area, value = row
        print(f"{tag_name:<20} {area:<10} {value}")

    avg = get_average_value(conn, "WWTP")
    print(f"\nAverage WWTP value: {avg:.2f}")

    conn.close()   # kaj shesh hole connection bondho korte hoy, resource free kore dey


if __name__ == "__main__":
    main()