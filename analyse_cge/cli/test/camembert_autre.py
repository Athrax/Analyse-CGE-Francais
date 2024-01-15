import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch
# Mettre dans gestionnaire_commandes
# from cli.test.camembert_autre  import pie_autre
# pie_autre(valeurs, labels, titre)


#faire le total
#faire 5% du total si données < 5% alors dans liste autre
#faire somme % autre
#total % autre puis divise pour avoir % chaque autre   #C? labels alors dict?


def pie_autre(valeurs,labels,titre):
    liste_autre=[]
    labels_autre=[]

    valeurs_1=[]
    labels_1=[]
    total = 0
    total_autre= 0

    total = sum(valeurs)

    for i in range(len(valeurs)-1):
        if valeurs[i] <= total * 0.05 :
            total_autre += valeurs[i]
            liste_autre.append(valeurs[i] / total)
            labels_autre.append(labels[i])
        else:
            valeurs_1.append(valeurs[i] / total)
            labels_1.append(labels[i])

    valeurs_1.append(total_autre / total)
    labels_1.append("Autre")
    affichage_autre(liste_autre,labels_autre,valeurs_1,labels_1,titre)

def affichage_autre(liste_autre,labels_autre,valeurs_1,labels_1,titre):
    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
    fig.subplots_adjust(wspace=0)

    #pie chart parameters
    explode = [0.1, 0, 0]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * valeurs_1[-1]
    wedges, *_ = ax1.pie(valeurs_1, autopct='%1.1f%%', startangle=angle,
                         labels=labels_1, explode=explode)
    #
    # bar chart parameters
    bottom = 1
    width = .2
    #
    # # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(liste_autre, labels_autre)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                     alpha=0.1 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

    ax2.set_title(titre)
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(liste_autre)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(4)
    ax2.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                          xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(4)

    plt.show()


