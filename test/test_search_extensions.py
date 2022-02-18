import os

from src import search_extensions


def test_count_files_no_path():
    assert search_extensions.count_files("") == []


def test_count_files_err_path():
    assert search_extensions.count_files("/no_true_path") == []


def test_count_files_true_path():
    assert len(search_extensions.count_files("/Users")) > 0


def test_get_params():
    # In get_params if environment vars doesnt exist execute input(), with this
    # sentence it builds an entry with value "" for all the input()
    search_extensions.input = lambda resp_input: ""

    path, extensions, files = search_extensions.get_params()
    assert isinstance(path, str) is True
    assert isinstance(extensions, str) is True
    assert isinstance(files, list) is True


def test_print_table():
    table = search_extensions.print_table("/un_path", "extensions", ["files"])
    assert table != ""


def test_print_table_no_params():
    table = search_extensions.print_table()
    assert table != ""


def test_search_extensions():
    search_extensions.input = lambda letter_input: "n"
    assert search_extensions.search_extensions() is True


def test_search_extensions_show_files():
    if not os.getenv("PATH_DIR"):
        os.environ["PATH_DIR"] = "/Users/u102105/workspace/java"
    if not os.getenv("EXTENSIONS"):
        os.environ["EXTENSIONS"] = "java"

    # Set the entry for input() function to "y"
    search_extensions.input = lambda letter_input: "y"
    assert search_extensions.search_extensions() is True


def test_main():
    search_extensions.main()
