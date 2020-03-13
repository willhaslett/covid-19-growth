# covid-19-growth

The Johns Hopkins University Center for Systems Science and Engineering is providing
[daily COVID-19 CSV files](https://github.com/CSSEGISandData/COVID-19) containing the data that are
displayed on their
[ArcGIS dashboard for COVID-19](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6).
This repo aims to provide a sensible starting point and some useful functions for ongoing work in
Pandas/Python using the JH data.

For VSCode users, available as a self-contained, system-independent environment using Docker Remote with Jupyter Notebook integration.

![Screenshot](.screenshot.png)

## Installing
### Vanilla

Clone the repo **with --recursive**
```
git clone --recursive git@github.com:willhaslett/covid-19-growth.git
```

Set up your Python environmet. For example, with virtualenv
```
cd covid-19-growth
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Verify installation
```
$ python lib/tests.py

Main dataframe:
       province_state    country      lat      long       date  cases   day
0                 NaN   Thailand  15.0000  101.0000 2020-01-22      2   0.0
1                 NaN      Japan  36.0000  138.0000 2020-01-22      2   0.0
2                 NaN  Singapore   1.2833  103.8333 2020-01-22      0   0.0
3                 NaN      Nepal  28.1667   84.2500 2020-01-22      0   0.0
4                 NaN   Malaysia   2.5000  112.5000 2020-01-22      0   0.0
...               ...        ...      ...       ...        ...    ...   ...
20195     Socorro, NM         US  33.8837 -106.7235 2020-03-11      2  49.0
20196  Bernalillo, NM         US  35.0178 -106.6291 2020-03-11      1  49.0
20197     Oakland, MI         US  42.5922  -83.3362 2020-03-11      1  49.0
20198       Wayne, MI         US  42.2791  -83.3362 2020-03-11      1  49.0
20199  New Castle, DE         US  39.5393  -75.6674 2020-03-11      1  49.0

[20200 rows x 7 columns]

Cases for one country:
     index    province_state country      lat     long       date  cases   day
0      159            France  France  46.2276   2.2137 2020-01-22      0   0.0
1      201         St Martin  France  18.0708 -63.0501 2020-01-22      0   0.0
2      208  Saint Barthelemy  France  17.9000 -62.8333 2020-01-22      0   0.0
3      563            France  France  46.2276   2.2137 2020-01-23      0   1.0
4      605         St Martin  France  18.0708 -63.0501 2020-01-23      0   1.0
..     ...               ...     ...      ...      ...        ...    ...   ...
145  19593         St Martin  France  18.0708 -63.0501 2020-03-10      2  48.0
146  19600  Saint Barthelemy  France  17.9000 -62.8333 2020-03-10      1  48.0
147  19955            France  France  46.2276   2.2137 2020-03-11   2281  49.0
148  19997         St Martin  France  18.0708 -63.0501 2020-03-11      2  49.0
149  20004  Saint Barthelemy  France  17.9000 -62.8333 2020-03-11      1  49.0

[150 rows x 8 columns]

Cases for one province_state:
   index    province_state country      lat      long       date  cases  day
0      5  British Columbia  Canada  49.2827 -123.1207 2020-01-22      0  0.0
1    409  British Columbia  Canada  49.2827 -123.1207 2020-01-23      0  1.0
2    813  British Columbia  Canada  49.2827 -123.1207 2020-01-24      0  2.0
3   1217  British Columbia  Canada  49.2827 -123.1207 2020-01-25      0  3.0
4   1621  British Columbia  Canada  49.2827 -123.1207 2020-01-26      0  4.0

Tests passed
$
```

### VSCode/Docker

Clone the repo as above (--recursive!)

Have the [VSCode extension for Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) installed. Here 'remote' means, in a local Docker container (Debian).

In VSCode, [Open the project folder in a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container)

Verify the installation as above.

## Usage

To stay in sync with the Johns Hopkins data
```
./update_data.sh
```

`etl.py` currently provides one dataframe and four fucntions:
* `df_all` A dataframe with all global cases, long format, dates as Pandas timestamps
* `filter(column, vlaue)` Generic filter
* `for_country(country)` Filter by country
* `for_province_state(province_state)` Filter by province_state
* `sum_by_date()` Group by date and sum case counts 

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

The Johns Hopkins University Center for Systems Science and Engineering is doing a great public service by sharing these data.
