# write some code using unittest to test our assigment function

import unittest
from my_lambdata.assignment import add_names_column
from pandas import DataFrame

df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})
class TestMyAssignment(unittest.TestCase):
  
    def test_assignment(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(add_names_column(df).iloc[[0],[1]], "Elif Ayar") 

if __name__ == '__main__':
    unittest.main()

#df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})
#mapped_df=add_names_column(df)

