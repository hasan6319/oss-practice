
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

console = Console()

console.print(
    Panel(f"Welcome to my Python tool, {args.name}!", title="OSS Practice")
)

table = Table(title="My Favorite Tools")
table.add_column("Tool")
table.add_column("Purpose")

table.add_row("Python", "Writing programs")
table.add_row("Git", "Tracking code changes")
table.add_row("VS Code", "Editing my projects")

console.print(table)