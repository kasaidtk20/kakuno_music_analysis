import pandas as pd
import numpy as np

from app import params


print('----------------------------start')

#xとyを1つのcsvファイルにまとめる
tr_ans_df = pd.read_csv('data_y.csv', encoding = 'UTF-8')
tr_fea_df = pd.read_csv('data_x.csv', encoding = 'shift_jis')
tr_ans_df = tr_ans_df.set_index('filename')
tr_fea_df = tr_fea_df.set_index('filename')

ans_improw = tr_ans_df[params.imps]

data_xy = pd.merge(tr_fea_df, ans_improw, left_index=True, right_index=True, how='outer')
data_xy = data_xy.groupby(level=0).first()

#trainとtestを分割する
per = 0.8*len(data_xy)
per = int(np.round(per, 0))
data_xy_train = data_xy.sample(frac=0.8, random_state=0)
data_xy_test = data_xy.sample(frac=1, random_state=0)[per:]

data_xy_train.to_csv('data_xy_train.csv', encoding = 'shift_jis')
data_xy_test.to_csv('data_xy_test.csv', encoding = 'shift_jis')




print('------------------------------end')