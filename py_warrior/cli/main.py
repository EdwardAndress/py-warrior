import click


@click.group()
def cli():
    """py-warrior: a Python dungeon crawler teaching game."""


@cli.command()
@click.argument("name")
def new(name):
    """Scaffold a new warrior directory."""
    click.echo(f"Creating {name}/... (not yet implemented)")


@cli.command()
def play():
    """Play the current level."""
    click.echo("Starting game... (not yet implemented)")


@cli.command()
def replay():
    """Replay the last run in slow motion."""
    click.echo("Replaying... (not yet implemented)")
