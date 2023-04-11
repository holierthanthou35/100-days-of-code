import pandas 

data = pandas.read_csv("day11.py\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

new_data_set = {
    "fur" : [],
    "count" : [],
}

for color in data[data.Fur_Color]:
    new_data_set.fur.append(color)