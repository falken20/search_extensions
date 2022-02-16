from os import path
from src.search_extensions import count_files, get_params
import pytest


def test_count_files_no_path():
    assert count_files("") == []

def test_count_files_err_path():
    assert count_files("/no_true_path") == []

def test_count_files_root_path():
    #assert len(count_files("/")) > 0
    pass

def test_get_params():
    path, extensions, files = get_params()
    assert isinstance(path, str) == True 
    assert isinstance(extensions, str) == True 
    assert isinstance(files, list) == True 


