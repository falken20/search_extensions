# by Richi Rod AKA @richionline / falken20

import logging
import os
import sys

from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

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
    # os.walk it yields a 3-tuple (dirpath, dirnames, filenames) for each folder and root
    total_files = []

    for root, dirs, files in os.walk(path):
        for name in files:
            total_files.append(os.path.join(root, name))
        # If only I want to see files names
        # total_files += files

    return total_files


def get_params():
    console.print("Executing [bold]get_params[/bold]", style="green")

    path = os.getenv("PATH_DIR") if os.getenv("PATH_DIR") else input("Insert path: ")
    extensions = os.getenv("EXTENSIONS") if os.getenv("EXTENSIONS") else input("Insert extensions (separated by comma): ")
    files = count_files(path)

    return path, extensions, files


def print_table(path="", extensions="", files=[""]):
    console.print("Executing [bold]print_table[/bold]", style="green")

    table = Table(show_header=True, header_style="bold")
    table.add_column("Variable")
    table.add_column("Value")
    table.add_row("PATH", path)
    table.add_row("EXTENSIONS", extensions)
    table.add_row("TOTAL FILES", str(len(files)))

    console.print(table)


def search_extensions() -> bool:
    """ Main function

    Returns:
        bool: Return True if everything ok, False in other case
    """
    console.print("Executing [bold]search_extensions[/bold]", style="green")

    try:
        file_list = []
        path, extensions, files = get_params()

        print_table(path, extensions, files)

        console.print("Starting to review [bold]files[/bold]", style="green")

        # Preparing progress task bar
        with Progress() as progress:
            task = progress.add_task("[green]Searching for [bold]extensions[/bold]...", total=len(files))

            count_files_affected = 0
            for file in files:
                if file[file.rfind(".") + 1:len(file)] in extensions:
                    count_files_affected += 1
                    file_list.append(file)

                progress.update(task, advance=1)

        print(f"\n[blue bold]Found: {count_files_affected} files with some of these extensions: {extensions}")

        if count_files_affected > 0 and input("Could you review name files (y/n)? ") in ["Y", "y"]:
            console.print(file_list)

        return True
    except Exception as err:
        console.print(f"[red bold]EXECUTION ERROR: {format(err)}")
        return False


def main():
    console.print("\n***** search_extensions started *****\n", style="bold green")
    # console.print(globals(), "\n")

    # Go to the parent directory
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    # Main proccess
    if search_extensions():
        console.print("search_extensions finished OK", style="green bold")
    else:
        console.print("search_extensions finished KO", style="red bold")

    console.print("\n[bold green]***** search_extensions finished :smile: *****[/bold green]\n")


if __name__ == "__main__":
    main()
