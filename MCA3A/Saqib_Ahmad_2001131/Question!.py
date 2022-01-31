#bar chart
import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]

height = [10, 24, 36, 40, 5]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label,
		width = 0.8, color = ['red', 'green'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My bar chart!')

plt.show()

#histogram
ages = [2,5,70,40,30,45,50,45,43,40,44,
		60,7,13,57,18,90,77,32,21,20,40]

range = (0, 100)
bins = 10

plt.hist(ages, bins, range, color = 'green',
		histtype = 'bar', rwidth = 0.8)

plt.xlabel('age')
plt.ylabel('No. of people')
plt.title('My histogram')

plt.show()

#pie chart

activities = ['eat', 'sleep', 'work', 'play']

slices = [3, 7, 8, 6]

colors = ['r', 'y', 'g', 'b']

plt.pie(slices, labels = activities, colors=colors,
		startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
		radius = 1.2, autopct = '%1.1f%%')

plt.legend()

plt.show()



