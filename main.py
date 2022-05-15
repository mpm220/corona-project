import numpy as np
import pandas as pd
import requests
import os


if __name__ == "__main__":
    
    file_path = "./data/covid/WHO-COVID-19-global-data.csv"
    df = pd.read_csv(file_path)

    """ Question, how did the growth in new cases change after vaccines were rolled out on 2020-12-02? """
    # find earliest recorded covid case in data set
    earliestReportedCase = df['Date_reported'].min()
    # sort data by date reported
    df.sort_values('Date_reported')
    # obtain data from up until 2020-12-02 
    preVaccine = df.loc[(df.Date_reported < '2020-12-03')]
    # find cumulative cases by country
    grouped_pre_df = preVaccine.groupby('Country')
    pre_vaccine_results = {}
    for key,item in grouped_pre_df:
        country = grouped_pre_df.get_group(key)
        pre_vaccine_results[key] = country["Cumulative_cases"].max()
    pre_result_df = pd.DataFrame(pre_vaccine_results.values(), index = pre_vaccine_results.keys(), columns=["pre_vaccine_total"])
    pre_result_df.index.name = "Country"
    

    """obtain data from same time frame after 2020-12-02, roughly 11 months post vaccine roll out"""
    post_vaccine = df.loc[((df.Date_reported > '2020-12-03') & (df.Date_reported < '2021-10-03'))]
    grouped_post_df = post_vaccine.groupby('Country')
    post_vaccine_results = {}
    for key,item in grouped_post_df:
        country = grouped_post_df.get_group(key)
        post_vaccine_results[key] = country["Cumulative_cases"].max()
    
    
    """Join result dictionary into one dataframe"""
    pre_result_df = pd.DataFrame(pre_vaccine_results.values(), index = pre_vaccine_results.keys(), columns=["pre_vaccine_total"])
    pre_result_df.index.name = "Country"
    post_result_df = pd.DataFrame(post_vaccine_results.values(), index = post_vaccine_results.keys(), columns=["post_vaccine_total"])
    post_result_df.index.name = "Country"
    end_data = pd.merge(pre_result_df, post_result_df, left_index = True, right_index=True)
    end_data['delta'] = end_data['post_vaccine_total'] - end_data['pre_vaccine_total']
    print(end_data.sort_values(by=['delta'], ascending=False))
    
