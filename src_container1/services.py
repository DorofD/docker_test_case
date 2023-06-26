import sqlite3 as sq


def create_db():
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS "text_notes" (
        "id"	INTEGER,
        "value"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
        );
    """
    cursor.execute(query)
    conn.commit()
    conn.close()


create_db()


def save_text(text):
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    query = f"""
        INSERT INTO text_notes ('value') VALUES('{text}');
    """
    cursor.execute(query)
    conn.commit()
    conn.close()


def get_notes():
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    query = f"""
        SELECT * FROM text_notes;
    """
    cursor.execute(query)
    result = [i[1] for i in cursor.fetchall()]
    return result


print(get_notes())
