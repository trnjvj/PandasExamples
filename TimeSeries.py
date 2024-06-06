dates = pd.date_range("2000-01-01", periods=5)

dates.to_period(freq="M").to_timestamp()
Out[176]: 
DatetimeIndex(['2000-01-01', '2000-01-01', '2000-01-01', '2000-01-01',
               '2000-01-01'],
              dtype='datetime64[ns]', freq=None)