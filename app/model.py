import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Model
from keras.layers import Dense, Dropout, Activation, Flatten

import params  


print('----------------------------start')

#機械学習モデルの定義
class DNNModel:
    def __init__(
            self,
            input_size: int = params.INPUT_SIZE,
            hidden1_size: int = params.HIDDEN1_SIZE,
            hidden2_size: int = params.HIDDEN2_SIZE,
            hidden3_size: int = params.HIDDEN3_SIZE,
            hidden4_size: int = params.HIDDEN4_SIZE,
            hidden5_size: int = params.HIDDEN5_SIZE,
            hidden6_size: int = params.HIDDEN6_SIZE,
            hidden7_size: int = params.HIDDEN7_SIZE,
            hidden8_size: int = params.HIDDEN8_SIZE,
            hidden9_size: int = params.HIDDEN9_SIZE,

            dropout: int = params.DROPOUT,

            output_size: int = params.OUTPUT_SIZE) -> None:
        self.input: Input = Input(shape=(input_size,), name='input')
        self.hidden1: Dense = Dense(hidden1_size, activation='relu', name='hidden1')
        self.hidden2: Dense = Dense(hidden2_size, activation='relu', name='hidden2')
        self.hidden3: Dense = Dense(hidden3_size, activation='relu', name='hidden3')
        self.hidden4: Dense = Dense(hidden4_size, activation='relu', name='hidden4')
        self.hidden5: Dense = Dense(hidden5_size, activation='relu', name='hidden5')
        self.hidden6: Dense = Dense(hidden6_size, activation='relu', name='hidden6')
        self.hidden7: Dense = Dense(hidden7_size, activation='relu', name='hidden7')
        self.hidden8: Dense = Dense(hidden8_size, activation='relu', name='hidden8')
        self.hidden9: Dense = Dense(hidden9_size, activation='relu', name='hidden9')
        
        self.dropout: Dropout = Dropout(dropout)

        self.output: Dense = Dense(output_size, name='output')

    def build(self) -> Model:
        input = self.input
        x = self.hidden1(input)
        x = self.hidden2(x)
        x = self.dropout(x)
        x = self.hidden3(x)
        x = self.hidden4(x)
        x = self.hidden5(x)
        #x = self.hidden6(x)
        #x = self.hidden7(x)
        #x = self.hidden8(x)
        #x = self.hidden9(x)
        output = self.output(x)
        return Model(inputs=input, outputs=output)
        

print('------------------------------end')