import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    # my code block
    n = 0
    i = window_size
    
    if window_size >= len(series):              # check if window size is bigger than data size
        print("Window size has to be less than series size.")
    else:
        while (n < len(series) - window_size):  # loop through data series less window size to stay inbound
            y.append(series[i])                 # add output at i index
            X.append(series[i-window_size:i])   # add inputs within window size before i index
            i += 1
            n += 1

    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y


# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    model = Sequential()                                         # initiate Keras RNN architecture 
    model.add(LSTM(200, input_shape=(X.shape[1], X.shape[2])))   # add input layer with 200 nodes
    model.add(Dense(58))                                         # add hidden fully connected layer with 58 nodes 
    model.add(Dropout(0.3))                                      # add dropout to prevent overfitting
    model.add(Dense(y.shape[1], activation='softmax'))           # add output layer with softmax activation


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    unique_chars = []
    unique_chars = list(set(text))
    print(unique_chars)

    # remove as many non-english characters and character sequences as you can 
    remove_chars = ['â', '$', 'é', 'è', '@', '&', '_', '(', ')', 'à', '%']
    for i in remove_chars:
        if i in text:
            i = ''
    

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    # my code block
    for i in range(0, len(text) - window_size, step_size):   # loop through until end of window size at x step size
        inputs.append(text[i:i + window_size])               # add input characters by window size before i index
        outputs.append(text[i + window_size])                # add a character at index i as the output
    
    return inputs,outputs
