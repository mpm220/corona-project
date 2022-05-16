# used the WHO-covid-19-global-data to practice pandas:

Which countries had the most new cases of covid reported during the year after the vaccine was rolled out on 2020-12-02?

pre_vaccine_total: timeframe from earliest case in dataset to the day of release 2020-12-02.
post_vaccine_total: same length of time as above following the release of vaccine ( 2020-12-02 to 2021-10-03 ).
delta: post_vaccine_total - pre_vaccine_total to obtain new cases over time frame.

results:

                          pre_vaccine_total  post_vaccine_total     delta
Country
United States of America           13700830            43227577  29526747
India                               9499413            33791061  24291648
Brazil                              6335878            21427073  15091195
The United Kingdom                  1681821             8030442   6348621
Turkey                              1461758             7182943   5721185
