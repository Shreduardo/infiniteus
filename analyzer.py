import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import sys
sys.path.append("/home/Documents/Dev/Work/infinteus")


recipeData = pd.read_csv("recipes.csv", header=0)



#*** Yield Time Plot ***#
yields = np.array(recipeData[["Name", "Yield"]])

line_styles = ["b-", "g-", "r-", "c-", "m-", "y-", "k-", "m--", "b--", "g--", "r--", "c--"]

plt.figure(1)
plt.ylabel("Yield")
plt.title("Juice Yields August-November 2016")
plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')


i = 0
for y in yields:
    if(i == 10):
        break
    plt.plot(y[1].split(), line_styles[i], label=y[0])
    i += 1

plt.legend(loc=9, bbox_to_anchor=(0.5, -0.05), ncol=5, prop={'size':10})
plt.tight_layout(pad=5)



#*** Average Yield Plot ***#
avg_yields = np.array(recipeData[["Name", "Yield_Avg"]])

N = 12
x_loc = np.arange(N)
width = 0.5

fig, ax = plt.subplots()

plt.figure(2)
plt.title("Average Juice Yields")
plt.ylabel("Average Yield")
plt.xlabel("Juice")

ax.bar(x_loc, avg_yields[:12, 1], width, align="center")
ax.set_xticks(x_loc)
ax.set_xticklabels(avg_yields[:12, 0])

plt.xticks(rotation='vertical')
plt.tick_params('x', labelsize='10')



plt.tight_layout(pad=5)
plt.show()



#*** Price - Ingredient Correlation ***#
costData=pd.read_csv("costs.csv", header=0)
