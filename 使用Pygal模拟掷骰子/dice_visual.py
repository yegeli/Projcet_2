import pygal
from die import Die

# 创建一个D6,6面
die_1 = Die()
die_2 = Die()
# 掷骰子多次，并把结果存储在一个列表中
results = []
for rull_name in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rulling one D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visualtwo.svg')
