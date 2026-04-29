import pytest
from pathlib import Path
from click.testing import CliRunner
from py_warrior.cli.main import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_new_creates_directory(runner):
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["new", "my-tower"])
        assert result.exit_code == 0
        assert Path("my-tower").is_dir()


def test_new_creates_warrior_py(runner):
    with runner.isolated_filesystem():
        runner.invoke(cli, ["new", "my-tower"])
        content = Path("my-tower/warrior.py").read_text()
        assert "def turn(warrior):" in content


def test_new_creates_readme(runner):
    with runner.isolated_filesystem():
        runner.invoke(cli, ["new", "my-tower"])
        content = Path("my-tower/README.md").read_text()
        assert "walk" in content.lower()


def test_new_warns_if_directory_exists(runner):
    with runner.isolated_filesystem():
        runner.invoke(cli, ["new", "my-tower"])
        result = runner.invoke(cli, ["new", "my-tower"])
        assert result.exit_code != 0
        assert "already exists" in result.output
