import urllib
from csv import reader
import pandas as pd
import numpy as np
import pyqtgraph as pg
from sklearn.svm import SVR
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from multiprocessing import Process


def ma_50(ticker):
    ma=[]
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    y=d['Close']
    for i in range(len(y)-50):
        ma.append((sum(y[i:i+51])/50))
    return ma    

def ma_20(ticker):
    ma=[]
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    y=d['Close']
    for i in range(len(y)-20):
        ma.append((sum(y[i:i+21]/20)))
    return ma     
    

def closeprice(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve (url, stock)    
    with open(stock,'r') as f:
        next(f)
        data=list(reader(f))
    clsprc=[float(x[4]) for x in reversed(data)]
    return clsprc

def get_data(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    x=np.arange(1,len(d)+1,1.0)    
    data=[]
    for i in range(len(d)):
        temp=(x[i], d['Open'][i], d['Close'][i], d['Low'][i], d['High'][i])
        temp=tuple(temp)
        data.append(temp)
    return data  

def volume(ticker): 
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    #x=np.arange(1,len(d)+1,1.0)
    data=[]
    for i in range(len(d)):
        temp=[float(d['Volume'][i])/1e6]
        data.append(temp)
    return data 
  
  
def prediction_rbf(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    d.iloc[:] = d.iloc[::-1].values
    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1)
    X=np.arange(1,len(d)+1,1.0)
    X=np.reshape(X,(len(X),1))
    y=d['Close']
    y_rbf = svr_rbf.fit(X, y).predict(X)
    return y_rbf
    
def prediction_lin(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    d.iloc[:] = d.iloc[::-1].values
    svr_lin = SVR(kernel= 'linear', C= 1e3) 
    X=np.arange(1,len(d)+1,1.0)
    X=np.reshape(X,(len(X),1))
    y=d['Close']
    y_lin = svr_lin.fit(X, y).predict(X)
    return y_lin
    
def prediction_poly(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    d.iloc[:] = d.iloc[::-1].values
    svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
    X=np.arange(1,len(d)+1,1.0)
    X=np.reshape(X,(len(X),1))
    y=d['Close']
    y_poly = svr_poly.fit(X, y).predict(X)
    return y_poly    

def prediction_neural(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    d.iloc[:] = d.iloc[::-1].values
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]
    data=[]
    for i in range(len(d)):
        if i==0:
            data.append(float((d['Close'].values)[i]))
        elif i%2==0:
            data.append(float((d['Close'].values)[i]))
            
    trainX,trainY = create_dataset(data)
    #trainY=d['Close']
    #trainX=np.arange(1,len(d)+1,1.0)
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    history = model.fit(trainX, trainY,validation_split=0.33, nb_epoch=70, batch_size=5, verbose=0)
    
    #plt.plot(history.history['loss'])
    #plt.plot(history.history['val_loss'])
    #plt.legend(['train', 'test'], loc='upper right')
    #X=np.arange(1,300,1.0)
    # Our prediction for tomorrow
    prediction = model.predict(data)
    #print (prediction)
    return prediction  


    



"""
pool = ThreadPool(processes=2)
a=[prediction_rbf,prediction_lin]
hasil=[]
for i in a:
    async_result = pool.apply_async(i, ('goog',)) # tuple of args for foo
    hasil.append(async_result.get())
"""
"""
a=[prediction_rbf,prediction_lin]

for i in a:
    y=_thread.start_new_thread( i, ("goog",) )
    print (y)
    #_thread.start_new_thread( print_time, ("Thread-1", 2, ) )
"""   