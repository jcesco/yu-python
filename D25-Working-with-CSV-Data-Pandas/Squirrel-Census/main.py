import pandas

# data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_count = data["Primary Fur Color"].value_counts()

# data = pandas.DataFrame(color_count)
# data.to_csv("./color_count.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./color_count2.csv")

