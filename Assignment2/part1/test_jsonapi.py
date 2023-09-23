import unittest
import datetime
import jsonapi  

class TestJSONAPI(unittest.TestCase):
    
    def setUp(self):
        self.data = {
            "name": "Alice",
            "age": 23,
            "date": datetime.datetime.now() 
        }

    def test_dumps(self):
        serial_data = jsonapi.dumps(self.data)
        self.assertIsInstance(serial_data, str) 

        self.assertIn(self.data['date'].isoformat(), serial_data)

    def test_loads(self):
        serial_data = jsonapi.dumps(self.data)
        deserial_data = jsonapi.loads(serial_data)
        
        self.assertIsInstance(deserial_data, dict)
        self.assertEqual(self.data['name'], deserial_data['name'])
        self.assertEqual(self.data['age'], deserial_data['age'])

        deserialized_date = datetime.datetime.fromisoformat(deserial_data['date'])
        self.assertEqual(self.data['date'], deserialized_date)

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            jsonapi.dumps(complex(2, 3))

if __name__ == '__main__':
    unittest.main()
