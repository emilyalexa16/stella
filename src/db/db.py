import os
import psycopg2
import click
from flask import current_app
from flask.cli import with_appcontext
from dotenv import load_dotenv

load_dotenv()

def get_db():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    return conn

def init_db():
    conn = get_db()
    with conn.cursor() as cur:
        with current_app.open_resource("schema.sql") as f:
            cur.execute(f.read())
        conn.commit()
    conn.close()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Database initialized from schema.sql.")

def init_app(app):
    app.cli.add_command(init_db_command)