import numpy as np
from matplotlib import pyplot   as plt

plt.style.use('ggplot')

dev_x = [25,27,29,32,35,40]

x_indexes = np.arange(len(dev_x))
width = 0.25

dev_y = [28000, 32000, 31000, 45000, 35000, 39000]

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label="All Age Group")

py_dev_y = [29000, 31000, 33000, 47000, 44000, 50000]

plt.bar(x_indexes + width, py_dev_y, width=width, color='#008fd5', label="Salary Distribution")

#Can add more lines using the same format as above and plotting more data

plt.xlabel("Employee Age")
plt.ylabel("Median Salary (EUR)")
plt.title("Median Salary (EUR) by Age")

plt.legend()

plt.xticks(ticks=x_indexes, labels=dev_x)

#grid the layout
plt.grid(True)

#Padding for cleaner layout
plt.tight_layout()

plt.show()
