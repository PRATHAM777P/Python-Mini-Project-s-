def get_history(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT action, result FROM history WHERE user=?", (user,))
    data = c.fetchall()
    conn.close()
    return data
