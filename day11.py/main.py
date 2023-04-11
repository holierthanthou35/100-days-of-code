import pandas

data = pandas.read_csv("C:\\Users\\avish\\Downloads\\weather_data.csv")

monday = data[data.day == "Monday"]
temp_in_c = monday.temp
temp_in_f = (temp_in_c * 9/5)+32
print(temp_in_f)