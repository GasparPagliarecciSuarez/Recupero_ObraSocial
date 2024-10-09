import unittest
from tkinter import Tk
from prueba3BD import Gestionmedico

class TestGestionmedico(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = Gestionmedico(self.root)
        self.app.tree.insert("", "end", values=("Ramiro", "Perez", "44567895"))
        self.app.tree.insert("", "end", values=("Jorge", "Barzola", "20445726"))
        self.app.tree.insert("", "end", values=("Jorge", "Sosa", "17000929"))

    def test_buscar_medico(self):
        # Test case where the search term matches a medico
        self.app.entrada_buscar.insert(0, "Ramiro")
        self.app.buscar_medico()
        items = self.app.tree.get_children()
        self.assertEqual(len(items), 1)
        self.assertEqual(self.app.tree.item(items[0], 'values'), ("Ramiro", "Perez", "44567895"))

        # Test case where the search term does not match any medico
        self.app.entrada_buscar.delete(0, 'end')
        self.app.entrada_buscar.insert(0, "NonExistent")
        self.app.buscar_medico()
        items = self.app.tree.get_children()
        self.assertEqual(len(items), 0)

        # Test case where the search term is empty
        self.app.entrada_buscar.delete(0, 'end')
        self.app.buscar_medico()
        items = self.app.tree.get_children()
        self.assertEqual(len(items), 3)

if __name__ == '__main__':
    unittest.main()