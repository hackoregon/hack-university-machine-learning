import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:\\Users\\Ebrahim\\Downloads\\table.csv'

df = pd.read_csv(filename)
df = df.sort('Date', ascending=True).reset_index(drop='True')
df.plot(x = 'Date', y = 'Close')
ts = np.array(df.Close)

def Weighted_MA_predictor(w,ts):
    
    w=w/float(np.linalg.norm(w,1))
    window_len = len(w)
    squared_error=[]
    x_next_predict_list=[]
    for i in range(window_len,len(ts)-1):
        x_block = ts[i-window_len:i]
        x_next_predict = np.dot(w,x_block)
        squared_error.append(np.power(ts[i+1]-x_next_predict,2))
        x_next_predict_list.append(x_next_predict)
    NMSE = np.mean(squared_error)/(len(ts)-2)
    print 'Normalized MSE is ' + str(NMSE)    
    plt.plot(ts,label='Actual')
    plt.plot(range(window_len,len(ts)-1),x_next_predict_list, label='Predicted')
    plt.legend(loc='best')
    plt.title('Normalized MSE is ' + str(NMSE))
    plt.xlabel('w = ' + str(w))
    return(NMSE)
    
w=np.array([1,1,1,1,1])

alpha=1
n=5
w=np.exp(-alpha*np.arange(n,-1,-1))

Weighted_MA_predictor(w,ts)



