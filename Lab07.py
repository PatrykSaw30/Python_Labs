Lab01
import numpy as np
import matplotlib.pyplot as plt

x = [1, 3, 5, 7]
y = np.array ([27, 30, 21, 29])

plt.plot(x, y, color = 'green')
plt.title('Temperature plot')
plt.xlabel('day')
plt.ylabel('temperature')
plt.grid(True)
plt.show()
------------------------------------
Lab02
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 5, 0.5)
y = np.arange(0, 25, 2.5)

plt.plot(x,y, marker = 's', color =  'red')
plt.text(float(x[0]), float(y[0]), f'({x[0]}, {y[0]})', fontsize = 12)
plt.text(float(x[-1]), float(y[-1]), '(5, 25)', fontsize = 12)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
---------------------------------------------------------------------------
Lab03
import matplotlib.pyplot as plt

labels = ['Film1', 'Film2', 'Film3']
sizes = [45, 40, 15]
explode1 = (0, 0., 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=45)
ax1.axis('equal')
plt.show()
----------------------------------------------------------------------------------------------
Lab04
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=10000)
bins = 10
fig, axes = plt.subplots(1, 2, figsize=(12, 5))


axes[0].hist(data, bins=bins)
axes[0].set_title("Histogram (10 bins)")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

counts, bin_edges = np.histogram(data, bins=bins)

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

axes[1].bar(bin_centers, counts, width=(bin_edges[1] - bin_edges[0]))
axes[1].set_title("Bar Plot (10 bins)")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()

plt.show()
