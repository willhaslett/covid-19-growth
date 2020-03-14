# covid-19-growth

The Johns Hopkins University Center for Systems Science and Engineering is providing
[daily COVID-19 CSV files](https://github.com/CSSEGISandData/COVID-19) containing the data that are
displayed on their
[ArcGIS dashboard for COVID-19](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6).
This repo aims to provide a sensible starting point and some useful functions for ongoing work in
Pandas/Python using the JH data.

The Jupyter Notebook contains a stub demonstrating the use of `lmfit` with these data

Cloning vs forking: no breaking changes to `etl.py` are anticipated, only additional features.

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

Cases (head):
  province_state    country      lat      long       date  cases  day
0            NaN   Thailand  15.0000  101.0000 2020-01-22      2  0.0
1            NaN      Japan  36.0000  138.0000 2020-01-22      2  0.0
2            NaN  Singapore   1.2833  103.8333 2020-01-22      0  0.0
3            NaN      Nepal  28.1667   84.2500 2020-01-22      0  0.0
4            NaN   Malaysia   2.5000  112.5000 2020-01-22      0  0.0

...

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

`etl.py` currently provides three dataframes and four manipulation functions:
* `df_cases` All global cases, long format, dates as Pandas timestamps
* `df_deaths` All global deaths, long format, dates as Pandas timestamps
* `df_recovered` All global recoveries, long format, dates as Pandas timestamps
* `filter(df, column, vlaue)` Generic filter
* `for_country(df, country)` Filter by country
* `for_province_state(df, province_state)` Filter by province_state
* `sum_by_date(df)` Group by date and sum case counts 

`us.py` currently provides case dataframes with states split into a new column, and a US
population dataframe
* `df_cases_us` All US cases
* `df_deaths_us` All US deaths
* `df_recovered_us` All US recoveries
* `df_population_us` United Staes population by state, sub_region, and region

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

The Johns Hopkins University Center for Systems Science and Engineering is doing a great public service by sharing these data.
