# with open("./weather_data.csv") as datafile:
#     weather_data = datafile.readlines()
#
# weather_information = []
# for weather in weather_data:
#     weather_information.append(weather.rstrip())
#
#
# print(weather_data)
# print(weather_information)

# import csv
#
# with open("./weather_data.csv") as datafile:
#     data = csv.reader(datafile)
#     print(data)
#     # for row in data:
#     #     print(row)
#
#     temperatures = []
#     for weather in data:
#         if weather[1] != "temp":
#             temperatures.append(int(weather[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = sum(temp_list)/ len(temp_list)
# print(avg_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# Get data in row (part 2)
# monday = data[data.day == "Monday"]
# temp_cel = int(monday.temp)
# print(temp_cel)
# temp_faren = temp_cel*9/5 +32
# print(temp_faren)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./new_data.csv")
