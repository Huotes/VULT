# tests/test_config.py
import pytest
from vult.config import Config

def test_config_initialization():
    config = Config(target='192.168.1.1', ports='80,443', output='report.json')
    assert config.target == '192.168.1.1'
    assert config.ports == '80,443'
    assert config.output == 'report.json'
