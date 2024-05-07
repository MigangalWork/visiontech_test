import unittest
from src.process import Processes 


class TestProcesses(unittest.TestCase):

    def test_data(self):
        Processes.managers = [
            {"id": 1, "tax_number": "132254524", "name": "Miguel Torres"},
            {"id": 2, "tax_number": "143618668", "name": "Ana Martín"},
            {"id": 3, "tax_number": "78903228", "name": "Carlos Ruiz"},
        ]

        Processes.grapes = [
            {"id": 1, "name": "Tempranillo"},
            {"id": 2, "name": "Albariño"},
            {"id": 3, "name": "Garnacha"},
        ]

        Processes.vineyards_info = [
            {"id": 1, "name": "Viña Esmeralda"},
            {"id": 2, "name": "Bodegas Bilbaínas"},
        ]

        Processes.vineyards = [{'manager_id': 1, 'vineyard_id': 1, 'grape_id': 1, 'year_planted': 2019, 'area': 1500, 
                                    'grape_name': 'Tempranillo', 'manager_name': 'Miguel Torres', 'vineyard_name': 'Viña Esmeralda'}, 
                                   {'manager_id': 2, 'vineyard_id': 2, 'grape_id': 2, 'year_planted': 2021, 'area': 9000, 
                                    'grape_name': 'Albariño', 'manager_name': 'Ana Martín', 'vineyard_name': 'Bodegas Bilbaínas'}, 
                                   {'manager_id': 3, 'vineyard_id': 1, 'grape_id': 3, 'year_planted': 2020, 'area': 3000, 
                                    'grape_name': 'Garnacha', 'manager_name': 'Carlos Ruiz', 'vineyard_name': 'Viña Esmeralda'}, 
                                   {'manager_id': 1, 'vineyard_id': 2, 'grape_id': 1, 'year_planted': 2020, 'area': 2000, 
                                    'grape_name': 'Tempranillo', 'manager_name': 'Miguel Torres', 'vineyard_name': 'Bodegas Bilbaínas'}, 
                                   {'manager_id': 3, 'vineyard_id': 2, 'grape_id': 3, 'year_planted': 2021, 'area': 1000, 
                                    'grape_name': 'Garnacha', 'manager_name': 'Carlos Ruiz', 'vineyard_name': 'Bodegas Bilbaínas'}]
        

    def test_get_managers_ids(self):
        expected_ids = [1, 2, 3]
        self.assertEqual(Processes.get_managers_ids(), expected_ids, "Should match the IDs of all managers")

    def test_get_tax_number_by_name(self):
        expected_tax_numbers = ['143618668', '78903228', '132254524' ]
        self.assertEqual(Processes.get_tax_number_by_name(), expected_tax_numbers, "Should return sorted tax numbers by name")

    def test_get_group_by_field_name_valid(self):
        expected_group = {'Viña Esmeralda': [1500, 3000], 'Bodegas Bilbaínas': [9000, 2000, 1000]}
        result = Processes.get_group_by_field_name(Processes.vineyards_info, 'vineyard_name', 'area')
        self.assertEqual(result, expected_group, "Should group areas by vineyard name correctly and sort them")

    def test_get_area_for_field(self):
        expected_areas = {'Viña Esmeralda': 4500, 'Bodegas Bilbaínas': 12000}
        result = Processes.get_area_for_field(Processes.vineyards_info, 'vineyard_name')
        self.assertEqual(result, expected_areas, "Should correctly compute total areas for each vineyard")


if __name__ == '__main__':
    unittest.main()
