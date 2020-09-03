import pandas as pd 


#Create a function to convert list to dataframe
def my_function(name):
    x=pd.Series(name)
    y=x.to_frame()
    print(y)

name = ["Elif", "Vera", "Musa","Harun","Ekmel","Huma"]

my_function(name)


#Create a function to convert string with % to as an integer

int_rate="14.74%"

def my_int(my_input):
    return float(my_input.strip("%"))

print(my_int(int_rate))
