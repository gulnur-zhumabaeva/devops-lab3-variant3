import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

GREETING = os.getenv("GREETING", "Hello")
STUDENT = os.getenv("STUDENT", "student")
VARIANT = os.getenv("VARIANT", "0")


def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "appdb_3"),
        user=os.getenv("DB_USER", "user_3"),
        password=os.getenv("DB_PASSWORD", "pass_3")
    )


@app.route("/")
def home():
    return f"{GREETING}, {STUDENT}! Variant {VARIANT} v2\n"

@app.route("/health")
def health():
    return jsonify(status="ok", variant=VARIANT)


@app.route("/visits")
def visits():
    if not os.getenv("DB_HOST"):
        return jsonify(error="DB_HOST is not configured"), 503

    conn = get_conn()

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS visits (
                        id SERIAL PRIMARY KEY,
                        visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                cur.execute("INSERT INTO visits DEFAULT VALUES")
                cur.execute("SELECT COUNT(*) FROM visits")
                count = cur.fetchone()[0]

        return jsonify(visits=count)
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000"))
    )
