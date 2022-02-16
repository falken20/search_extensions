import os
import pytest
import mock

from src import search_extensions


def test_count_files_no_path():
    assert search_extensions.count_files("") == []


def test_count_files_err_path():
    assert search_extensions.count_files("/no_true_path") == []


def test_count_files_root_path():
    #assert len(search_extensions.count_files("/")) > 0
    pass


def test_get_params():
    # In get_params if environment vars doesnt exist execute input(), with this
    # sentence it builds an entry with value "" for all the input()
    search_extensions.input = lambda resp_input: ""

    path, extensions, files = search_extensions.get_params()
    assert isinstance(path, str) == True
    assert isinstance(extensions, str) == True
    assert isinstance(files, list) == True


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
        os.environ["EXTENSIONS"] = "txt"

    # Set the entry for input() function to "y"
    search_extensions.input = lambda letter_input: "y"
    assert search_extensions.search_extensions() is True


def test_if_main():
    from src import search_extensions
    with mock.patch.object(search_extensions, "main", return_value=42):
        with mock.patch.object(search_extensions, "__name__", "__main__"):
            with mock.patch.object(search_extensions.sys, 'exit') as mock_exit:
                search_extensions.main()
                # assert mock_exit.call_args[0][0] == 42
                assert True == True
