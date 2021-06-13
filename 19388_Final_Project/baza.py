import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    print("Database connection is open")

    conn.execute('CREATE TABLE pracownicy (imienazwisko TEXT, nrpracownika TEXT, adres TEXT)')
    print("Table created")

    conn.close()
    print("Database connection is closed")

    conn = sqlite3.connect('database.db')
    print("Database connection is open")
    cur = conn.cursor()

    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",
                ('Adrian Lukasik', '1', 'Elblag'))
    cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?,?,?)",
                ('Python Flask', '2', 'Berlin'))
    conn.commit()

    cur.execute('SELECT * FROM pracownicy ORDER BY imienazwisko')
    print(cur.fetchall())

    conn.close()
    print("Database connection is closed")