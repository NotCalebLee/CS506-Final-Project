# CS506-Final-Project

Project Members: Caleb Lee, Emir Kavukcu, Travis Meyer, Toriana Mullins, Ziad Alharbi

We are following the Spark! project "Boston Bus Equity." Boston's public transport, particularly the MBTA, is a core piece of the Massachusetts bay area. It serves over 1 million people a day and has an estimated economic value of 11.4 billion per year, meaning the quality of service directly impacts people's quality of life (A Better City). The goal of this project is to use MBTA bus data to understand service performance trends by geography.

Main goal:
- To measure how MBTA bus performance varies across the Boston area and identify residents most affected by gaps in service

Specific goals: 
- Measure the performance of buses by analyzing:
  - Reliability of bus arrival and departure times (does the route hit the timepoint requirements outlined in the MBTA service delivery policy)
  - Average delay and travel-time variation for trips
- Measure performance of buses by geographical location
  - Identify areas with consistently abnormal service (i.e. find routes where the difference in intended times and actual time is statistically significant)
  - Test whether bus performance is tied with neighborhood characteristics such as median household income, ethnic background, etc.
- Build a model to accurately predict delays on specific routes during specific days, times, and seasons
- To quantify the impact that poor service quality has on riders (hours lost through total delays on a route or a similar metric)

What data needs to be collected?

A lot of the data we will be using is accessible through the MBTA (accessible with ArcGIS). This data includes a system wide passenger survey, bus ridership data (broken up by routes, stops, and seasons), and reliability data shows with bus arrival and departure times. Data on people, specifically geographic information, will be taken from census surveys, and surveys within Massachusetts such as MassDOT. We will use GeoPandas to join the stop coordinates to census tracts. We will then merge the census data through those same tracts, which will allow us to look at routes in relation to the people who are most affected by any quality disparities. 

2015-2017 Passenger Survey: https://www.ctps.org/dv/mbtasurvey2018/index.html#navButton
Ridership Data: https://mbta-massdot.opendata.arcgis.com/search?q=ridership%20time%20period%20season
Bus Arrival and Departure Times 2018-2024: https://mbta-massdot.opendata.arcgis.com/search?collection=dataset&q=mbta%20bus%20arrival%20departure%20time

Project Timeline:
- Week of October 11th: Start looking into data sources and collecting what is relevant and applicable. 
- Week of October 18th: Begin cleaning data and finding trends tying metrics together.
- Week of October 25th and November 1st: Work on data visualization of statistically significant relationships. (This is given two weeks as we accept the possibility that finding significant relationships can be challenging)
- Week of November 8th: Finalize the primary data work and begin model training.
- Week of November 15th and 22nd: Primarily work on model training and evaluation. Starting the basis of the final report is also a priority.
- Week of November 29th: Work to make the project feel complete and thorough. Find any gaps or supplementary work that can further our goals, as well as finishing the final report. Additionally, as this is a Spark! project, we have the added responsibility of demo day at the end of the semester. We will prepare anything we feel in necessary for that side of our project.

Additional Sources:
Service Delivery Policy: https://cdn.mbta.com/sites/default/files/2025-2-7-service-delivery-policy-fall-2024-final.pdf
Economic Impacts of MBTA: https://www.abettercity.org/news-and-events/blog/the-transportation-dividend-transit-investments-and-the-massachusetts-economy
