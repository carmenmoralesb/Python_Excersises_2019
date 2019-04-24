#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from sobrecarga import *

class Probando_suma(unittest.TestCase):
    """
    Prueba de sumar fracciones
    """
 
    def test_suma_fracciones(self):
        """
        Test que prueba la suma de fracciones del fichero de sobrecarga.py
        """
        f1 = (1/3)
        f2 = (2/3)
        self.assertEqual(f1+f2,3/3)
 
if __name__ == '__main__':
    unittest.main()