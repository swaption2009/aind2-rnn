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
    step_size = 1                                            # set step size at 1
    
    for i in range(0, len(series) - window_size, step_size): # loop through the series from beginning
        X.append(series[i:i + window_size])                  # add inputs from the series from i index to window size
        y.append(series[i + window_size])                    # add output from the series at index (i + window size)
    
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y


# TODO: build an RNN to perform regression on our time series input/output data
hidden_units = 200  # set hidden units variable

def build_part1_RNN(step_size, window_size):
    # initiate Keras RNN architecture
    model = Sequential()
    # add input layer with 200 hidden units and input shape of window size and 
    model.add(LSTM(hidden_units, input_shape=(window_size, len(chars))))
    # add fully connected hidden layer with number of unique characters
    model.add(Dense(len(chars))
    # add output layer with softmax activation layer
    model.add(Activation('softmax'))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    unique_chars = list(sorted(set(text)))

    # loop through unique characters for inspection and removal in the next step
    for i, c in enumerate(unique_chars):
        print(str(i) + ":", str(c), end=" ")

    # remove as many non-english characters and character sequences as you can 
    dropped_chars = unique_chars[1:10] + unique_chars[13:26] + unique_chars[27:28] + unique_chars[54:]
    print("\n" + "characters to be removed are: ", dropped_chars)

    # replace unwanted character to blank space
    for i in dropped_chars:
        text = text.replace(i,'')

    # shorten any extra dead space created above
    text = text.replace('  ',' ')
        

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
