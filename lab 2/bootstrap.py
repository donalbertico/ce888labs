import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
	means = []
	for i in range(0,iterations):
		arr = np.random.choice(sample,sample_size,replace = True)
		means.append(np.mean(arr))
	data_mean = np.mean(means)
	lower = np.percentile(means, 97.5)
	upper = np.percentile(means, 2.5)
	return data_mean, lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')

	data = df.values.T[1]
	boots = []
	for i in range(100, 100000, 1000):
		boot = boostrap(data, data.shape[0], i)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')

	veh = pd.read_csv('vehicles.csv')
	proposed = veh.values.T[1]
	proposed = proposed[~np.isnan(proposed)]
	boostCu = boostrap(veh.values.T[0],len(veh.values.T[0]),1000);
	boostNe = boostrap(proposed,len(proposed),1000);
	print((("current upper : %s")%(boostCu[2])))
	print((("current lower : %s")%(boostCu[1])))
	print((("new upper : %s")%(boostNe[2])))
	print((("new lower : %s")%(boostNe[1])))

	#the bounds does not really variate meaning the new fleets are not better than the current ones
