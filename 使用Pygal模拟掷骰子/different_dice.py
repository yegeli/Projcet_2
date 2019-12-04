import pygal
from die import Die

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)
# 掷几次次骰子，并把结果存储在一个列表中
results = []
for rull_name in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rulling a D6 and D10 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                 '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
