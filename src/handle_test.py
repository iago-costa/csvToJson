# teste unitario para o modulo hendle.py

import unittest

import src.handle as handle


class TestHandle(unittest.TestCase):
    def setUp(self):
        self.new_file = "src/data/colleges.csv"
        self.old_file = "src/data/TabeladeAreasdoConhecimento.csv"

    def test_get_list(self):
        self.assertEqual(
            handle.get_list("0 Lógica Matemática 1.01.01.03-9"),
            ["1.01.01.03-9", " Lógica Matemática"],
        )

    def test_read_csv(self):
        self.assertEqual(len(handle.read_csv(self.old_file)), 1292)

    def test_save_csv(self):
        self.assertEqual(
            handle.save_csv(
                self.new_file, handle.new_data_for_csv(handle.read_csv(self.old_file))
            ).shape,
            (1291, 2),
        )

    def test_line_by_line(self):
        self.assertEqual(
            handle.line_by_line(self.new_file, self.old_file).shape, (1291, 2)
        )


# write for pytest functions
# def test_get_list():
#     assert handle.get_list('0 Lógica Matemática 1.01.01.03-9') == ['Lógica Matemática', '1.01.01.03-9']


# def test_read_csv():
#     assert handle.read_csv('TabeladeAreasdoConhecimento.csv').shape == (1290, 1)


# def test_save_csv():
#     assert handle.save_csv('new_file.csv', handle.read_csv('TabeladeAreasdoConhecimento.csv')).shape == (1290, 1)


# def test_line_by_line():
#     assert handle.line_by_line('new_file.csv', 'TabeladeAreasdoConhecimento.csv').shape == (1291, 2)
