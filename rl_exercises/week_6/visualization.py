import json

import numpy as np
import matplotlib.pyplot as plt
from rliable import library as rly
from rliable import metrics
from rliable import plot_utils

baselines = ['none','avg','value','gae']
seeds = [123, 456789, 34643]

all_returns = {}
all_steps = list()

for b in baselines:
    all_returns[b] = list()
    for s in seeds:
        with open(f"rl_exercises/week_6/results/level_1/baseline_{b}_{s}.json", 'r') as file:
            data = json.load(file)
            all_returns[b].append([data['avg_returns']])
            all_steps.append(data['steps'])
    all_returns[b] = np.asarray(all_returns[b])
    
# all_returns = {baseline: [num_runs x num_games x frames]}
# all_returns = {baseline: [       3 x         1 x 100000]}

assert all([len(s) == len(all_steps[0]) for s in all_steps])

frames = np.arange(len(all_steps[0]))

iqm = lambda scores: np.array([metrics.aggregate_iqm(scores[..., frame]) for frame in frames])

iqm_scores, iqm_cis = rly.get_interval_estimates(all_returns, iqm, reps=50000)


ax = plot_utils.plot_sample_efficiency_curve(
    all_steps[0],
    iqm_scores, 
    iqm_cis, 
    algorithms=baselines,
    xlabel='Step',
    ylabel='Average Return'
)

fig = ax.get_figure()
fig.legend()
fig.savefig("rl_exercises/week_6/plots/level1_average_returns.png", bbox_inches='tight')
