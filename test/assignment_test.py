# write some code using unittest to test our assigment function

import unittest
from my_lambdata.assignment import add_names_column
from pandas import DataFrame

df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})
class TestMyAssignment(unittest.TestCase):
  
    def test_assignment(self):
        df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})

        # make sure our test is setup properly

        self.assertEqual(len(df.columns), 1) 
        self.assertEqual(list(df.columns),['abbrev']) 
        self.assertEqual(df.iloc[0]["abbrev"],'EA') 

        # what code can we write, referencing df to know if our function
        # did what it was supposed to do
        mapped_df=add_names_column(df)

        self.assertEqual(len(mapped_df.columns), 2) 
        self.assertEqual(list(mapped_df.columns),['abbrev','name']) 
        self.assertEqual(mapped_df.iloc[0]["abbrev"],'EA') 
        self.assertEqual(mapped_df.iloc[0]["name"],'Elif Ayar') 

if __name__ == '__main__':
    unittest.main()

