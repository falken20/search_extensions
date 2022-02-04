# by Richi Rod AKA @richionline / falken20

import logging
import os
import sys

from rich import print
from rich import console
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

# Create global object to manage terminal logs
console = Console()


def count_files(path):
    console.print("Executing [bold]count_files[/bold]", style="green")
    # os.walk it yields a 3-tuple (dirpath, dirnames, filenames)
    return next(os.walk(path))[2]


def get_params():
    
    console.print("Executing [bold]get_params[/bold]", style="green")

    path = os.getenv("PATH_DIR", "")
    extensions = os.getenv("EXTENSIONS", "")
    files = [count_files(path)]

    table = Table(show_header=True, header_style="bold red")
    table.add_column("Variable")
    table.add_column("Value")
    table.add_row("PATH", path)
    table.add_row("EXTENSIONS", extensions)
    table.add_row("NUM FILES", str(len(files)))

    console.print(table)

    return files, extensions


def search_extensions() -> bool:
    """ Main function

    Returns:
        bool: Return true if everything is ok or false in another case
    """
    console.print("Executing [bold]search_extensions[/bold]", style="green")

    files, extensions = get_params()
    
    a = 0
    for step in track(range(10000000), description="Processing..."):
        a += 1

def main():
    console.print("\nStarting search_extensions cron\n", style="bold blue")
    console.print(globals(), "\n")
    # Go to the parent directory
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # Main proccess
    search_extensions()

    console.print("\n[bold blue]Init config finished[/bold blue]\n", ":smile:")


if __name__ == "__main__":
    main()
