import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

veh = pd.read_csv('vehicles.csv')
print((veh.columns))
sns_plot = sns.lmplot(veh.columns[0],veh.columns[1], data = veh, fit_reg = False)
sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)

sns_plot.savefig("scaterplot.png",bbox_inches='tight')

current = veh.values.T[0]
proposed = veh.values.T[1]
proposed = proposed[~np.isnan(proposed)]

plt.clf()
sns_plot2 = sns.distplot(current, bins=20, kde=False, rug = True).get_figure()
sns_plot3 = sns.distplot(proposed, bins=20, kde=False, rug = True).get_figure()
axes = plt.gca()
axes.set_xlabel('fleet')
axes.set_ylabel('feet count')

sns_plot3.savefig("histogram.png",bbox_inches='tight')
