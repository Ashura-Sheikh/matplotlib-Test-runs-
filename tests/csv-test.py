import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


plt.style.use("ggplot")

with open('data.csv') as csvfile:
    csv_reader= csv.DictReader(csvfile)

    language_counter= Counter()

    for row in csv_reader:
        language_counter.update(row['clientid'].split(';'))

clientid = []
gains = []



plt.bar(clientid, gains)

plt.bar(clientid, gains)
plt.title("Demo")
plt.xlabel("test_run_x")
plt.ylabel("test_run_y")

plt.show()



    #row= next(csv_reader)
    #print(row)
