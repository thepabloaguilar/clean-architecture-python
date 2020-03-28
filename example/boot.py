from example.configuration.database import init_db
from example.application import create_app

application = create_app()


@application.cli.command("initdb")
def _init_db():
    init_db()


if __name__ == "__main__":
    application.run()
