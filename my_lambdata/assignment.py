from pandas import DataFrame


#TODO: helper function from Assignment
# Name abbreviation--> Full name visa versa
# EA--> Elif Ayar, etc


def add_names_column(my_df):

    """
    Add a column of corresponding state names to a dataframe.

    params(my_df) is a dataframe with a column called "abbrev" that has name abbreviations
    
    Return a copy of the original dataframe, but wioth extra column.

    """

    #TODO:

    new_df=my_df.copy()

    name_map={"EA":"Elif Ayar","VA":"Vera Ayar","MA":"Musa Ayar","HA":"Harun Ayar","EAY":"Ekmel Ayar",
              "HAY":"Huma Ayar"}
    
    new_df['name']=new_df['abbrev'].map(name_map)

    #new_df
    return new_df
if __name__=="__main__":
  
    df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})
    print(df)


    mapped_df=add_names_column(df)
    print(mapped_df)