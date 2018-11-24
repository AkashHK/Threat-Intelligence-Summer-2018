# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pandas import Series
import sys
from datetime import time
import numpy
import statsmodels.api

f=open("key.txt",'r')
a=f.readline()
b=int(a.rstrip())

def fun(i,k):


    sys.stdout=open(str(k+1)+'/'+str(i-1)+'.csv',"w")

    
    dateparse = lambda dates: pd.time.strptime(dates,'%H-%M-%S.%f')
    data = pd.read_csv(str(k+1)+'/sep'+str(i)+'.csv')

    ts=Series.from_csv(str(k+1)+'/sep'+str(i)+'.csv',header=0)
    info = pd.read_csv(str(k+1)+'/sep'+str(i)+'.csv')

    num_of_for = 10  #NUMBER OF FORECASTS

    flag = 0
    count = 0

    s = info['#Passengers'].values


    for z in s:
        if z == 0:
            count = count + 1

    if count >= 0.99*len(ts):
        flag = 1

    if flag == 1: 
        for i in range(num_of_for):
            print(0)

    else:
		def fun(ser):
			co = 0
			c1 = 0
			for e in ser[len(ser)-12:]:
				if e == 0:
					co = co + 1
				if e == 1:
					c1 = c1 + 1 
				if co > c1:
					ser[len(ser) - 3] = 1
				if co < c1:
					ser[len(ser) - 3] = 0
			return ser	
			
		tsmod=fun(ts)
		ts_log = np.sqrt(tsmod)


		moving_avg =ts_log.rolling(12).mean()


		ts_log_moving_avg_diff = ts_log - moving_avg

		ts_log_diff = ts_log - ts_log.shift()

		from statsmodels.tsa.seasonal import seasonal_decompose
		decomposition = seasonal_decompose(ts_log,freq = 2)

		trend = decomposition.trend
		seasonal = decomposition.seasonal
		residual = decomposition.resid

		ts_log_decompose = residual


		from statsmodels.tsa.statespace import sarimax

		model = sarimax.SARIMAX(ts_log,order=(4, 1, 1),enforce_stationarity=False,enforce_invertibility=False)
		results_ARIMA = model.fit()

		predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)

		predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()


		predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
		predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
		predictions_ARIMA_log.head()


		predictions_ARIMA = np.square(predictions_ARIMA_log)

		start_index = len(ts)
		end_index = len(ts)
		
		forecast = results_ARIMA.forecast(steps = num_of_for)
		
		for p in forecast:
		    print(p)


		sys.stdout.close()
for k in range(b):
	for i in range(1,39):
	    fun(i,k)
 





