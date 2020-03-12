# covid-19-growth

The Johns Hopkins University Center for Systems Science and Engineering is providing
[daily COVID-19 CSV files](https://github.com/CSSEGISandData/COVID-19) containing the data that are
displayed on their
[ArcGIS dashboard for COVID-19](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6).
This repo aims to provide a sensible starting point and some useful functions for ongoing work in
Pandas/Python using the JH data.

For VSCode users, available as a self-contained, system-independent environment using Docker Remote with Jupyter Notebook integration.

Breaking changes to `etl.py` will be committed on 2020-03-12 as new features are added. The API for
this file should be stable as of 2020-03-13.

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
             city_county      lat      long       date  cases state
35           King County  47.6062 -122.3321 2020-01-22      1    WA
36           Cook County  41.7377  -87.6976 2020-01-22      0    IL
46           Los Angeles  34.0522 -118.2437 2020-01-22      0    CA
64            San Benito  36.5761 -120.9876 2020-01-22      0    CA
66               Madison  43.0731  -89.4012 2020-01-22      0    WI
...                  ...      ...       ...        ...    ...   ...
10345      Pierce County  47.0676 -122.1295 2020-03-07      1    WA
10346    Plymouth County  42.1615  -70.7928 2020-03-07      1    MA
10347  Santa Cruz County  36.9741 -122.0308 2020-03-07      1    CA
10348       Tulsa County  36.1593  -95.9410 2020-03-07      1    OK
10349  Montgomery County  30.3213  -95.4778 2020-03-07      0    TX

[3772 rows x 6 columns]
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

`etl.py` currently provides one dataframe and these fucntions:
* `df_all` A dataframe with all global cases, long format, dates as Pandas timestamps
* `filter(column, vlaue)` Generic filter
* `for_country(country)` Filter by country
* `for_province_state(province_state)` Filter by province_state
* `sum_by_date()` Group by date and sum case counts 

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

The Johns Hopkins University Center for Systems Science and Engineering is doing a great public service by sharing these data.
