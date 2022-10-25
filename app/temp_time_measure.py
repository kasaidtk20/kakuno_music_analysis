import time

# 時間計測開始
time_sta = time.perf_counter()
# 処理を書く（5秒停止する）
time.sleep(5)
# 時間計測終了
time_end = time.perf_counter()
# 経過時間（秒）
tim = time_end- time_sta