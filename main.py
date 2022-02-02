# by Richi Rod AKA @richionline / falken20

import logging
import os
import sys

from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track

from dotenv import load_dotenv, find_dotenv

# Set the format of logging messages
logging.basicConfig(format=f'{os.getenv("ID_LOG", "")} %(levelname)s:%(asctime)s: '
                           f'File: %(filename)s: Function: %(funcName)s\n'
                           '%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=os.getenv("LOG_LEVEL", "INFO"))

# Load .env file
load_dotenv(find_dotenv())


def count_files(path):
    # os.walk it yields a 3-tuple (dirpath, dirnames, filenames)
    return next(os.walk(path))[2]


def get_params():
    path = os.getenv("PATH_DIR", "")
    extensions = os.getenv("EXTENSIONS", "")
    files = count_files(path)

    table = Table(show_header=True, header_style="bold red")
    table.add_column("Variable")
    table.add_column("Value")
    table.add_row("PATH", path)
    table.add_row("EXTENSIONS", extensions)
    table.add_row("NUM FILES", str(len(files)))

    return table


def main():
    console = Console()
    console.print("Starting search_extensions cron", style="bold magenta")
    # Go to the parent directory
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # Get the environment vars
    console.print(get_params())

    a = 0
    for step in track(range(10000000), description="Processing..."):
        a += 1

    print("[bold green]Init config finished[/bold green]", ":vampire:")


if __name__ == "__main__":
    main()
