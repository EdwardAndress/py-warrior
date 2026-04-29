import click
from pathlib import Path


_TEMPLATES = Path(__file__).parent / "templates"


@click.group()
def cli():
    """py-warrior: a Python dungeon crawler teaching game."""


@cli.command()
@click.argument("name")
def new(name):
    """Scaffold a new warrior directory."""
    target = Path(name)
    if target.exists():
        raise click.ClickException(f"'{name}' already exists.")
    target.mkdir()
    (target / "warrior.py").write_text((_TEMPLATES / "warrior.py.txt").read_text())
    (target / "README.md").write_text((_TEMPLATES / "README.md.txt").read_text())
    click.echo(f"Created {name}/. Edit warrior.py then run: py-warrior play")


@cli.command()
def play():
    """Play the current level."""
    click.echo("Starting game... (not yet implemented)")


@cli.command()
def replay():
    """Replay the last run in slow motion."""
    click.echo("Replaying... (not yet implemented)")
