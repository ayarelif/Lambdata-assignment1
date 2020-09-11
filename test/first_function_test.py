import unittest
from my_lambdata.first_function import my_int

int_rate="14.74%"
class TestMyAssignment(unittest.TestCase):
    
    def test_function(self):
        self.assertEqual(my_int(int_rate), 14.74) 

if __name__ == '__main__':
    unittest.main()