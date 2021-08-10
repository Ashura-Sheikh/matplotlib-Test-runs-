from matplotlib import pyplot   as plt

plt.style.use('ggplot')

slices = [15, 50, 35]
labels = ['Fifteen', 'Fifty', 'Thirtyfive']
## can break as much as you want
explode = [0, 0.1, 0.1]
colors = ['#008fd5', '#fc4f30', '#6d904f']

#autopct stands for percentage value given
plt.pie(slices, labels=labels, colors=colors, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Pie Chart display")
plt.tight_layout()
plt.show()
