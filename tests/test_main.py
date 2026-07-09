import importlib


def test_main_import():
    importlib.import_module("main")
    assert True