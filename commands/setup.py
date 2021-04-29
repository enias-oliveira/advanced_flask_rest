import flask

from flask import cli
from flask_sqlalchemy import SQLAlchemy


def group_database(app: flask.Flask) -> None:
    cli_group_database: cli.AppGroup = cli.AppGroup("database")
    database: SQLAlchemy = app.db

    @cli_group_database.command("create")
    def cli_database_create():
        database.create_all()

    @cli_group_database.command("drop")
    def cli_database_drop():
        database.drop_all()

    app.cli.add_command(cli_group_database)


def init_app(app: flask.Flask) -> None:
    group_database(app)
