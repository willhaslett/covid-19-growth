# covid-19-growth

The Johns Hopkins University Center for Systems Science and Engineering is providing
[daily COVID-19 CSV files](https://github.com/CSSEGISandData/COVID-19) containing the data that are
displayed on their
[ArcGIS dashboard for COVID-19](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6).
This repo aims to provide a sensible starting point and some useful functions for ongoing work in
Pandas/Python using the JH data.

`modeling_stub.ipynb` contains a template demonstrating the use of [lmfit](https://lmfit.github.io/lmfit-py/) with these data.

For VSCode users, available as a self-contained, system-independent environment using Docker Remote with Jupyter Notebook integration.

![](.screenshot.png)

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

Global cases (head):
        date  day  cases province_state    country      lat      long
0 2020-01-22    0      2            NaN   Thailand  15.0000  101.0000
1 2020-01-22    0      2            NaN      Japan  36.0000  138.0000
2 2020-01-22    0      0            NaN  Singapore   1.2833  103.8333
3 2020-01-22    0      0            NaN      Nepal  28.1667   84.2500
4 2020-01-22    0      0            NaN   Malaysia   2.5000  112.5000

...

Tests passed
$
```

### VSCode/Docker

Clone the repo as above (--recursive!)

Have the [VSCode extension for Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) installed. Here 'remote' means in a local Docker container (Debian).

In VSCode, [Open the project folder in a container](https://code.visualstudio.com/docs/remote/containers#_quick-start-open-an-existing-folder-in-a-container)

Verify the installation as above.

## Usage

The JH submodule is pulled nightly, updating the source data. To force a pull locally:
```
./update_data.sh
```

### `c19all.py`
* `df_all` A dictionary containing dataframes with all global data for cases, deaths, and recoveries. `province_state` has mixed types, as it does upstream.
  ```
  print(df_all['cases'])

              date  day  cases  province_state              country      lat      long
  0     2020-01-22    0      2             NaN             Thailand  15.0000  101.0000
  1     2020-01-22    0      2             NaN                Japan  36.0000  138.0000
  2     2020-01-22    0      0             NaN            Singapore   1.2833  103.8333
  3     2020-01-22    0      0             NaN                Nepal  28.1667   84.2500
  4     2020-01-22    0      0             NaN             Malaysia   2.5000  112.5000
  ...          ...  ...    ...             ...                  ...      ...       ...
  21887 2020-03-13   51      2             NaN                Aruba  12.5211  -69.9683
  21888 2020-03-13   51      2  Grand Princess               Canada  37.6489 -122.6655
  21889 2020-03-13   51      1             NaN                Kenya  -0.0236   37.9062
  21890 2020-03-13   51      1             NaN  Antigua and Barbuda  17.0608  -61.7964
  21891 2020-03-13   51      5         Alabama                   US  32.3182  -86.9023
  
  [21892 rows x 7 columns] 
  ```

* Functions
  - `filter(df, column, vlaue)` Generic filter
  - `for_country(df, country)` Filter by country
  - `for_province_state(df, province_state)` Filter by province_state
  - `sum_by_date(df)` Group by date and sum case counts 

### `c19us.py`
####Deprecation warning: A dataframe is under construction that facilitates analyis at the national level as well as at the state, county and territory level, rather than breaking thinigs up as they are now. There will be boolean columns indicating the type of each record. This is needed because, e.g., county and state reords both have a state associated with them.  v0.2.0.

* `df_us` A dictionary of US case, death, and recovery dataframes for the US.
  ```
  print(df_us['cases'])

         index       date  day  cases          state_county      lat      long
  0        100 2020-01-22    0      0            Washington  47.4009 -121.4905
  1        101 2020-01-22    0      0              New York  42.1657  -74.9481
  2        102 2020-01-22    0      0            California  36.1162 -119.6816
  3        103 2020-01-22    0      0         Massachusetts  42.2302  -71.5301
  6        106 2020-01-22    0      0               Georgia  33.0406  -83.6431
  ...      ...        ...  ...    ...                   ...      ...       ...
  13033  23385 2020-03-14   52      0             Wayne, MI  42.2791  -83.3362
  13034  23386 2020-03-14   52      0        New Castle, DE  39.5393  -75.6674
  13035  23404 2020-03-14   52      6               Alabama  32.3182  -86.9023
  13036  23408 2020-03-14   52      3           Puerto Rico  18.2208  -66.5901
  13037  23424 2020-03-14   52      1  Virgin Islands, U.S.  18.3358  -64.8963

  [12932 rows x 7 columns]
  ```
* `df_us_state` A dictionary of state-level case, death, and recovery dataframes for the US.

  ```
  print(df_us_state['cases'])
  
               date  day  cases                 state  population          sub_region     region
  0     2020-01-22    0      0            Washington     7614893             pacific       west
  1     2020-01-22    0      0              New York    19453561        mid_atlantic  northeast
  2     2020-01-22    0      0            California    39512223             pacific       west
  3     2020-01-22    0      0         Massachusetts     6892503         new_england  northeast
  6     2020-01-22    0      0               Georgia    10617423      south_atlantic      south
  ...          ...  ...    ...                   ...         ...                 ...        ...
  12841 2020-03-14   52      9          South Dakota      884659  west_north_central    midwest
  12842 2020-03-14   52      0         West Virginia     1792147      south_atlantic      south
  12843 2020-03-14   52      2               Wyoming      578759            mountain       west
  12914 2020-03-14   52      0  District of Columbia      705749      south_atlantic      south
  13035 2020-03-14   52      6               Alabama     4903185  east_south_central      south

  [2703 rows x 7 columns]
  ```
  [Population and region data source](https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population#Summary_of_population_by_region)
  
* `df_us_county` A dictionary of county-level case, death, and recovery dataframes for the US. US territory data are mixed in with county data at present.
  ```
  print(df_us_county['cases'])

              date  day                county  cases
  18    2020-01-22    0             Tennessee      0
  52    2020-01-22    0            Kitsap, WA      0
  53    2020-01-22    0            Solano, CA      0
  54    2020-01-22    0        Santa Cruz, CA      0
  55    2020-01-22    0              Napa, CA      0
  ...          ...  ...                   ...    ...
  13032 2020-03-14   52           Oakland, MI      0
  13033 2020-03-14   52             Wayne, MI      0
  13034 2020-03-14   52        New Castle, DE      0
  13036 2020-03-14   52           Puerto Rico      3
  13037 2020-03-14   52  Virgin Islands, U.S.      1
  ```

* A caution about using the US data below the national level. Reporting regions have been evolving over time. As shown in the figure below, the makeup of overall US data beetween
counties and states has been shifting toward the state level. It's unclear on 2020-03-15 how this will play out.
  ![](.us_cases.png)
  
**Deprecation warning:** A dataframe is under construction that facilitates analyis of the US data at the national level as well as at the state, county and territory level, rather than breaking things up as they are now. There will separate columns for each type of record. This will be the only US dataframe in the next release.


## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

The Johns Hopkins University Center for Systems Science and Engineering is doing a great public service by sharing these data.
