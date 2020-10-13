import requests
import numpy as np
import pandas as pd
import datetime
import dask.dataframe as dd
from datetime import timedelta, date
from tqdm.auto import tqdm


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


monitoring_site_locations_names = ['AQSID',
                                   'parameter name',
                                   'site code',
                                   'site name',
                                   'status',
                                   'agency id',
                                   'agency name',
                                   'EPA region',
                                   'latitude',
                                   'longitude',
                                   'elevation',
                                   'GMT offset',
                                   'country code',
                                   'Nan1',
                                   'Nan2',
                                   'MSA code',
                                   'MSA name',
                                   'state code',
                                   'state name',
                                   'county code',
                                   'county name',
                                   'Nan3',
                                   'Nan4']
hourly_data_names = ['Valid date',
                     'valid time',
                     'AQSID',
                     'site name',
                     'GMT offset',
                     'parameter name',
                     'reporting units',
                     'value',
                     'data source']
target_col = ['latitude', 'longitude', 'elevation', 'site name',
              'status', 'parameter name', 'reporting units', 'value']
start_date = date(2020, 10, 1)
end_date = date(2020, 10, 2)


async def read_csv(filename):
    df = pd.read_csv(filename, header=None)
    return df
for target_date in tqdm(daterange(start_date, end_date)):
    monitoring_site_locations = pd.read_csv(
        f"https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/{target_date.year}/{target_date.strftime('%Y%m%d')}/monitoring_site_locations.dat", delimiter="|", names=monitoring_site_locations_names, encoding="ISO-8859-1")
    for hour in tqdm(range(0, 24)):
        hourly_data = pd.read_csv(
            f"https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/{target_date.year}/{target_date.strftime('%Y%m%d')}/HourlyData_{target_date.strftime('%Y%m%d')}{hour:02d}.dat", delimiter="|", names=hourly_data_names, encoding="ISO-8859-1")
        hourly_data.merge(monitoring_site_locations, on=['site name', 'parameter name'])[
            target_col].to_csv(f"HourlyData_{target_date.strftime('%Y%m%d')}{hour:02d}.dat", index=False)
        break
    break
