from class_model.die import Die
import pygal

die = Die()
result = []
for num in range(1,1001):
    result.append(die.roll())

# Analysis Result
frequencies = []
frequencies_dic = {}
for num in range(1, die.num_sides + 1):
    frequency = result.count(num)
    frequencies.append(frequency)
    frequencies_dic[num] = frequency

hist = pygal.Bar()
hist.x_labels = list(range(1,die.num_sides+1))
hist.title = "title"

# x axis title
hist.x_title = "中文 chinese title"
# y axis title
hist.y_title = "y axis title"

hist.add("D6" , frequencies_dic)
hist.render_to_file("01.svg")