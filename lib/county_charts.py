import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.ticker as ticker
import datetime
import pickle
import copy
import snake_case

YAXPARAMS = {
    'cases': {
        'total': {
            'ymax': 40,
            'yinterval': 5
        },
        'adj': {
            'ymax': 80,
            'yinterval': 10
        }
    },
    'deaths': {
        'total': {
            'ymax': 5,
            'yinterval': 1
        },
        'adj': {
            'ymax': 5,
            'yinterval': 1
        }
    },
}

YINTERVAL_TOTAL = 5
YINTERVAL_ADJ = 10

SOURCE_LABELS = {
    'nyt': 'New York Times',
    'jhu': 'Johns Hopkins University'
}

STATE_COLORS = {
    'Vermont': '#1f77b4',
    'New Hampshire': '#871f78',
}

df_start = pickle.load(
    open('output/pickles/df_us_combined.p', 'rb')).reset_index()

# If you pass in a population, the output will be per 1,000 people
# If you pass in an output filename, the plots will be written to ./images and not rendered to the screen
def county_plot(county, state, metrics=['cases', 'deaths'], source='nyt', total_population=None):
    df = copy.deepcopy(df_start)
    start_date = pd.to_datetime('2020-03-01')
    location = {
        'type': 'county',
        'value': [county, state]
    }
    for metric in metrics:
        for population in [False, total_population]:
            count_of = f'{metric}_{source}'
            county = location['value'][0]
            state = location['value'][1]
            color = STATE_COLORS[state]
            df = df[df.county == county]
            df = df[df.state == state]
            df = df[df.date >= start_date]
            if population:
                df[count_of] = df[count_of].apply(lambda x: (x / population) * 100000)
            df['count_of_diff'] = df[count_of].diff()
            df['count_of_diff_7_day_mean'] = df.count_of_diff.rolling(7).mean()
            df = df.iloc[1:]
            fig = plt.figure(figsize=(7, 3))
            ax = fig.add_subplot(111)
            ax.bar('date', 'count_of_diff', data=df, color=color, alpha=0.35)
            ax.plot('date', 'count_of_diff_7_day_mean', color=color, data=df)
            ax.xaxis.set_major_locator(dt.MonthLocator())
            ax.xaxis.set_major_formatter(dt.DateFormatter('%b'))
            ax.set_ylim(ymin=0)
            yaxparams = YAXPARAMS[metric]['adj' if population else 'total']
            ymax = yaxparams['ymax']
            yinterval = yaxparams['yinterval']
            # ax.set_ylim(ymax=yaxparams['ymax'])
            ax.yaxis.set_ticks(np.arange(0, ymax + yinterval, yinterval))
            ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
            ax.tick_params(axis='y', colors=color)
            ax.tick_params(axis='x', colors=color)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.grid(axis='x')
            plt.style.use('seaborn-whitegrid')
            plt.text(df.date.iloc[-1] + datetime.timedelta(days=3), df.count_of_diff_7_day_mean.iloc[-1],
                    "7-day\navg.", color=color, style='italic')
            filename = snake_case.convert(f'{county} {state} {metric}{" adjusted" if population else ""}.svg')
            plt.savefig(f'output/charts/{filename}')


county_dicts = [
    {'county': 'Orange', 'state': 'Vermont', 'total_population': 28892},
    {'county': 'Orange', 'state': 'Vermont', 'total_population': 28892},
    {'county': 'Windsor', 'state': 'Vermont', 'total_population': 55062},
    {'county': 'Grafton', 'state': 'New Hampshire', 'total_population': 89886},
    {'county': 'Sullivan', 'state': 'New Hampshire', 'total_population': 43146},
]

for county_dict in county_dicts:
    county_plot(**county_dict)
