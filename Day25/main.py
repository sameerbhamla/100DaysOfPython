'''
with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)


with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)


data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
print(data_dict)
temp_list = data['temp'].to_list()
print(sum(temp_list)/len(temp_list))
print(data['temp'].mean())
print(data['temp'].max())
print(data['condition'])
print(data.condition)


data = pandas.read_csv('weather_data.csv')
monday = data[data.day == 'Monday']
print(monday)
monday_temp = monday.temp[0]
monday_temp_F = monday.temp * 9 / 5 + 32
print(monday_temp_F)


data_dict = {
    'students': ['sameer', 'maxwell', 'mickey'],
    'scores': [100, 70, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
'''

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrel,red_squirrel,black_squirrel)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrel,red_squirrel,black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')