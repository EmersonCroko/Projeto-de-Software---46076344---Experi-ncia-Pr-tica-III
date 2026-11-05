import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import calcular_soma

def test_calcular_soma():
    assert calcular_soma(2, 3) == 5
    assert calcular_soma(-1, 1) == 0 

from main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "O resultado da soma é: 5" in captured.out