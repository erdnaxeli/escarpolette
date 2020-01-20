import click
import uvicorn

from escarpolette import app


@click.command()
@click.option(
    "--config",
    "config_file",
    help="path to the config file",
    type=click.Path(resolve_path=True),
)
@click.option(
    "--host",
    default="127.0.0.1",
    help="address to bind to listen for connections",
    type=str,
)
@click.option(
    "--port", default=5000, help="port to bind to listing for connections", type=int
)
def run(config_file: click.Path, host: str, port: int) -> None:
    app.config.from_pyfile(config_file)
    uvicorn.run(app, host=host, port=port)


run()
