# teste unitario para o modulo hendle.py

import unittest
import src.handle as handle

class TestHandle(unittest.TestCase):

    def setUp(self):
        self.new_file = 'new_file.csv'
        self.old_file = 'TabeladeAreasdoConhecimento.csv'

    def test_get_list(self):
        self.assertEqual(handle.get_list('0 Lógica Matemática 1.01.01.03-9'), ['1.00.00.00-3', 'Ciências Exatas e da Terra'])

    def test_read_csv(self):
        self.assertEqual(handle.read_csv(self.old_file).shape, (1290, 1))

    def test_save_csv(self):
        self.assertEqual(handle.save_csv(self.new_file, handle.read_csv(self.old_file)).shape, (1290, 1))

    def test_line_by_line(self):
        self.assertEqual(handle.line_by_line(self.new_file, self.old_file).shape, (1291, 2))
