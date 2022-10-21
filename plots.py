from matplotlib import pyplot as plt
import numpy as np

# wykres kołowy - pie chart

def pie_chart(sums, categories):
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    ax.pie(sums, labels = categories, autopct='%1.2f%%')
    plt.savefig("categories_chart.jpg")
    #plt.show()
