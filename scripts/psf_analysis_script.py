import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

params = {
        "axes.titlesize": 24,
        "axes.labelsize": 20,
        "lines.linewidth": 3,
        "lines.markersize": 10,
        "xtick.labelsize": 20,
        "ytick.labelsize": 20,
        "font.size": 24,
        # "font.weight": "bold",
}
mpl.rcParams.update(params)


df = pd.read_csv("../data/python_psf_external_18.csv")
python_usage = df[
    [x for x in df.columns if "What do you use Python for?" in x and not
     'Other' in x]
]
f, ax = plt.subplots(figsize=(11, 4.5))
ax.set_xlim(11000, 0)
ax.yaxis.set_ticks_position('right')

python_usage[~python_usage.isnull()] = 1
python_usage.columns = [x.split(':')[0] for x in python_usage.columns]
sum_python_usage = python_usage.sum()
top_5_python_usage = sum_python_usage.sort_values().iloc[-5:]
top_5_python_usage.plot.barh(ax=ax, width=0.5)

f.subplots_adjust(right=0.3)
ax.xaxis.set_visible(False)
for loc in ['right', 'left', 'top', 'bottom']:
    ax.spines[loc].set_visible(False)

i = 0
for idx, row in top_5_python_usage.iteritems():
    ax.text(row + 6100, i-0.1, '{0:.1%}'.format(row/len(python_usage)))
    i += 1
f.savefig('../media/psf_usage_survey.png', dpi=f.dpi, transparent=True)
