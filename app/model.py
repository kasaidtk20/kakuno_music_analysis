import tensorflow as tf
from keras.api._v2 import keras
from keras.layers import Input, Dense
from keras.models import Model
import params  #./params.py


print('----------------------------start')

#機械学習モデルの定義
class DNNModel:
    def __init__(
            self,
            input_size: int = params.INPUT_SIZE,
            hidden1_size: int = params.HIDDEN1_SIZE,
            hidden2_size: int = params.HIDDEN2_SIZE,
            output_size: int = params.OUTPUT_SIZE) -> None:
        self.input: Input = Input(shape=(input_size,), name='input')
        self.hidden1: Dense = Dense(hidden1_size, activation='relu', name='hidden1')
        self.hidden2: Dense = Dense(hidden2_size, activation='relu', name='hidden2')
        self.output: Dense = Dense(output_size, name='output')

    def build(self) -> Model:
        input = self.input
        x = self.hidden1(input)
        x = self.hidden2(x)
        output = self.output(x)
        return Model(inputs=input, outputs=output)

print('------------------------------end')