import os
import json
import copy
import pytest

# ------------------------
# Cheese "module" code
# ------------------------

_default_prefs = {
    'slicing': ['manchego', 'sharp cheddar'],
    'spreadable': ['Saint Andre', 'camembert', 'bucheron', 'goat', 'humbolt fog', 'cambozola'],
    'salads': ['crumbled feta']
}

def read_cheese_preferences():
    """Read cheese preferences from ~/.cheese.json"""
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'r') as f:
        return json.load(f)

def write_cheese_preferences(prefs=_default_prefs):
    """Write cheese preferences to ~/.cheese.json"""
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)

def write_default_cheese_preferences():
    """Write default preferences"""
    write_cheese_preferences(_default_prefs)

# ------------------------
# Tests
# ------------------------

def test_def_prefs_full(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    write_default_cheese_preferences()
    expected = _default_prefs
    actual = read_cheese_preferences()
    assert expected == actual

def test_custom_prefs(tmp_path, monkeypatch):
    monkeypatch.setenv('HOME', str(tmp_path))
    custom_prefs = {
        'slicing': ['brie'],
        'spreadable': [],
        'salads': ['blue cheese']
    }
    write_cheese_preferences(custom_prefs)
    read_back = read_cheese_preferences()
    assert read_back == custom_prefs

def test_def_prefs_change_expanduser(tmp_path, monkeypatch):
    fake_home_dir = tmp_path / "home"
    fake_home_dir.mkdir()
    monkeypatch.setattr(os.path, "expanduser", lambda x: str(x).replace("~", str(fake_home_dir)))
    write_default_cheese_preferences()
    expected = _default_prefs
    actual = read_cheese_preferences()
    assert expected == actual

def test_def_prefs_change_defaults(tmp_path, monkeypatch):
    fake_home_dir = tmp_path / "home"
    fake_home_dir.mkdir()
    monkeypatch.setattr(os.path, "expanduser", lambda x: str(x).replace("~", str(fake_home_dir)))

    # Write defaults and save original
    write_default_cheese_preferences()
    defaults_before = copy.deepcopy(_default_prefs)

    # Modify defaults in memory
    monkeypatch.setitem(_default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(_default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(_default_prefs, 'salads', ['pepper jack'])
    defaults_modified = copy.deepcopy(_default_prefs)

    # Write modified defaults
    write_default_cheese_preferences()
    actual = read_cheese_preferences()

    # Assertions
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
