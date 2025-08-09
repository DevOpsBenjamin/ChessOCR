import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from service.main import process_move


def test_process_move():
    assert process_move('dummy.png') == 'e2e4'
