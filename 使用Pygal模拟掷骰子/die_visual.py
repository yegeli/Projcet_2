import pygal
from die import Die

# 创建一个D6,6面
die = Die()
# 掷几次次骰子，并把结果存储在一个列表中
results = []
for rull_name in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rulling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
