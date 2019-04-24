import pytest
from carta import *
from mazo import *

def test_cartas():
    m1 = Mazo()
    m2 = Mazo([])

    assert len(m1) == 48
    assert len(m2) == 0
    assert type(m1.saca(2))
    assert type(m1.saca(2)) 