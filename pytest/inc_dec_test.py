import sys

import project_root

sys.path.append(project_root.path)
import inc_dec  # The code to test


def test_increment():
    """_summary_"""
    assert inc_dec.increment(3) == 4


def test_decrement():
    """_summary_"""
    assert inc_dec.decrement(3) == 2
