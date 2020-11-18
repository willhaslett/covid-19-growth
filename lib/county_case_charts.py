import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import matplotlib.ticker as ticker
import datetime
import pickle
import copy
import snake_case

# TODO: This should all be object-oriented rather than a bunch of functions

YMAX = 30

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
def county_plot(county, state, metric='cases', source='nyt', population=None):
    df = copy.deepcopy(df_start)
    start_date = pd.to_datetime('2020-03-01')
    location = {
        'type': 'county',
        'value': [county, state]
    }
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
    ax.set_ylim(ymin=0)
    # ax.set_ylim(ymax=YMAX)
    ax.xaxis.set_major_locator(dt.MonthLocator())
    ax.xaxis.set_major_formatter(dt.DateFormatter('%b'))
    ax.tick_params(axis='y', colors=color)
    ax.tick_params(axis='x', colors=color)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis='x')
    plt.style.use('seaborn-whitegrid')
    plt.text(df.date.iloc[-1] + datetime.timedelta(days=3), df.count_of_diff_7_day_mean.iloc[-1],
             "7-day\navg.", color=color, style='italic')
    filename = snake_case.convert(f'{county} {state}.svg')
    plt.savefig(f'output/charts/{filename}')


county_dicts = [
    {'county': 'Orange', 'state': 'Vermont', 'population': 28892},
    {'county': 'Orange', 'state': 'Vermont', 'population': 28892},
    {'county': 'Windsor', 'state': 'Vermont', 'population': 55062},
    {'county': 'Grafton', 'state': 'New Hampshire', 'population': 89886},
    {'county': 'Sullivan', 'state': 'New Hampshire', 'population': 43146},
]

for county_dict in county_dicts:
    county_plot(**county_dict)
