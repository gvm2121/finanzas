# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:03:59 2021

@author: gonzalo
"""

import numpy as np
import pandas as pd
#import pandas_datareader.data as web
import matplotlib.pyplot as plt

#list of df in portfolio
#df = ['AAPL','AMZN','MSFT','GOOG']
 
#download daily price data for each of the df in the portfolio
#data = web.DataReader(df,data_source='yahoo',start=start)['Adj Close']
#data can be stored by pd.Dataframe.to_csv(data,'data.csv')
#data = pd.DataFrame.from_csv('data.csv')

#convert daily stock prices into daily returns
csv=pd.read_csv('acciones_para_portfolio.csv', delimiter=";", encoding="utf-8", index_col=0)
df=pd.DataFrame(csv)
returns = -df.pct_change().dropna()

 
#calculate mean daily return and covariance of daily returns
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()
 
#set number of runs of random portfolio weights
num_portfolios = 25000
 
#set up array to hold results
#We have increased the size of the array to hold the weight values for each stock
results = np.zeros((12,num_portfolios))
 
for i in range(num_portfolios):
    #select random weights for portfolio holdings
    weights = np.array(np.random.random(9))
    #rebalance weights to sum to 1
    weights /= np.sum(weights)
 
    #calculate portfolio return and volatility
    portfolio_return = np.sum(mean_daily_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
 
    #store results in results array
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    #store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2,i] = results[0,i] / results[1,i]
    #iterate through the weight vector and add data to results array
    for j in range(len(weights)):
        results[j+3,i] = weights[j]

#convert results array to Pandas DataFrame

results_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe','LTM','SQM_B','COPEC','SALFA','VAPORES','CAP','BSAN','CMPC','FALAB'])
 
#locate position of portfolio with highest Sharpe Ratio
max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
#locate positon of portfolio with minimum standard deviation
min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]
#create scatter plot coloured by Sharpe Ratio
plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu',s=1)
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.colorbar()
#plot red star to highlight position of portfolio with highest Sharpe Ratio
plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=100)
#plot green star to highlight position of minimum variance portfolio
plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=100)
print(min_vol_port)