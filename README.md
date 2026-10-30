# CS506-Final-Project

Project Members: Caleb Lee, Emir Kavukcu, Travis Meyer, Toriana Mullins, Ziad Alharbi

We are following the Spark! project "Boston Bus Equity." Boston's public transport, particularly the MBTA, is a core piece of the Massachusetts bay area. It serves over 1 million people a day and has an estimated economic value of 11.4 billion per year, meaning the quality of service directly impacts people's quality of life (A Better City). The goal of this project is to use MBTA bus data to understand service performance trends by geography.

Main goal:
- To measure how MBTA bus performance varies across the Boston area and identify residents most affected by gaps in service

## Project status

| Goal | Status |
|---|---|
| Measure whether routes meet the timepoint requirements in the MBTA Service Delivery Policy | Done |
| Measure average delay and travel-time variation | Done |
| Find routes where actual times differ significantly from scheduled times | Done |
| Measure performance by location, and test its link to neighborhood income and race | Done |
| Estimate the time riders lose to poor service | Done, as a rough estimate |
| Build a model to predict delays by route, day, time, and season | Not started |

## What's in this repo

| Location | Contents |
|---|---|
| `boston_bus_equity_checkin.ipynb` | Full analysis, from data download to final figures |
| `Boston_Bus_Equity_CheckIn_Report.pdf` | Short October check-in report, without code |
| `figures/` | The 10 figures used in the notebook and report |
| `data/processed/` | Cleaned datasets and cleaning audit tables |
| `final/data_processing.py` | Separate analysis of MBTA prediction accuracy |

To run the notebook, install `numpy`, `scipy`, `matplotlib`, and `openpyxl`, then run all cells from the repo's main folder. It also needs the `unzip` tool, which comes with Colab, Linux, and Git for Windows. Missing raw data is downloaded into `data/raw/`, about 1.6 GB, which is not stored in the repo. Delete `data/processed/` to rebuild the cleaned data from scratch.

## Data we used

| Data | Coverage used | Used for |
|---|---|---|
| [Bus Arrival Departure Times 2024](https://mbta-massdot.opendata.arcgis.com/datasets/96c77138c3144906bce93d0257531b6a/about) | Weekdays, Jan-Nov 2024 | On-time rate, delay, wait, and trip time |
| [Bus Arrival Departure Times 2020](https://mbta-massdot.opendata.arcgis.com/datasets/4c1293151c6c4a069d49e6b85ee68ea4/about) | Weekdays, Jan-Feb 2020 | Pre-pandemic baseline |
| [Bus Ridership by Trip, Season, Route, Line, and Stop](https://mbta-massdot.opendata.arcgis.com/datasets/8daf4a33925a4df59183f860826d29ee/about) | Weekdays, Fall 2016-2025 | Riders on each route |
| [2025 System-Wide Passenger Survey](https://mbta-massdot.opendata.arcgis.com/datasets/2dac9c48bd3440c2bcf2a220614c667b_0/about) | Bus routes | Race and income of riders |
| [2015-2017 Passenger Survey](https://www.ctps.org/dv/mbtasurvey2018/index.html) | Bus routes | Comparison with earlier riders |
| [MBTA GTFS](https://www.mbta.com/developers/gtfs) | Stops file | Bus stop locations |
| [ACS 5-year median household income, B19013](https://censusreporter.org/tables/B19013/) | 2020-2024, census tracts in Suffolk, Middlesex, Norfolk, Essex, and Plymouth counties | Neighborhood income |
| [ACS 5-year race and ethnicity, B03002](https://censusreporter.org/tables/B03002/) | 2020-2024, same tracts | Neighborhood race |
| [TIGERweb census tract boundaries](https://tigerweb.geo.census.gov/tigerwebmain/TIGERweb_main.html) | 2020 tracts, same counties | Matching stops to tracts |
| [Rapid Transit and Bus Prediction Accuracy Data](https://mbta-massdot.opendata.arcgis.com/datasets/155ab68df00145cabddfb90377201b0e/about) | Bus and subway | Used by `final/data_processing.py` |

## How we processed the data

- **Time periods:** we compare Jan-Feb 2020 with Jan-Feb 2024 so that season does not affect the change. Other 2024 results use Jan-Nov, because the bus network changed in December 2024.
- **Weekdays only:** weekend schedules differ.
- **On time:** we apply the Service Delivery Policy tests. Scheduled service is judged against the timetable, and frequent service on the gaps between buses. Blank arrival times are left out of the main rate. Counting them as not on time lowers the 2024 rate from 66.3% to 61.4%.
- **Neighborhoods:** we match bus stop coordinates to census tracts with a point-in-polygon check in `matplotlib`, then attach each tract's income and race.
- **Riders:** we use survey results for route groups that list their routes, which cover 56% of boardings.

## What we found

"Yes" means the data back up the claim, but it does not prove what caused it.

| # | What we expected | True? | What we found |
|---|---|---|---|
| H1 | Fewer people ride the bus than before the pandemic, and the drop differs by route | Yes | Weekday riders are at 79% of their Fall 2019 level, and the typical route lost 20%. |
| H2 | Bus trips take longer and are less predictable than scheduled | Partly | A typical trip takes about as long as scheduled, but fast and slow trips on a route differ by about 16 minutes. |
| H3 | Riders wait longer than the schedule suggests | Yes | On frequent routes, the wait is 8.6 minutes, not the 6.9 the schedule suggests. |
| H4 | Some routes are much more reliable than others | Yes | Routes range from 40% to 80% on time. |
| H5 | The 15 target routes perform worse than other routes | Partly | They are on time about as often, but run about 1.4 minutes later on average. |
| H6 | Minority and low-income communities get worse service | Partly | On-time rates are about the same across neighborhoods, but buses run somewhat later in minority and lower-income areas. |
| H7 | A small number of routes cause most of the lost time | Weakly | The 15 routes losing the most time account for 45% of lost hours, but they also carry 38% of riders. |
| H8 | Buses were less reliable in 2024 than before the pandemic | Yes | From early 2020 to early 2024, the on-time rate fell from 73% to 69%, and average delay rose from 2.3 to 3.9 minutes. |

## Remaining work

- Week of November 8th: Finalize the primary data work and begin model training.
- Weeks of November 15th and 22nd: Primarily work on model training and evaluation, and start the final report.
- Week of November 29th: Fill any remaining gaps, finish the final report, and prepare for the Spark! demo day at the end of the semester.

## Additional sources

- [Service Delivery Policy](https://cdn.mbta.com/sites/default/files/2025-2-7-service-delivery-policy-fall-2024-final.pdf)
- [Livable Streets Better Buses Report](https://d3n8a8pro7vhmx.cloudfront.net/livablestreetsalliance/pages/6582/attachments/original/1569205099/lsa-better-buses-2019-v9-20sep19.pdf?1569205099) (source of the target routes)
- [Economic Impacts of MBTA](https://www.abettercity.org/news-and-events/blog/the-transportation-dividend-transit-investments-and-the-massachusetts-economy)
