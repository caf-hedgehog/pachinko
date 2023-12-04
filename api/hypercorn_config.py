import multiprocessing

# サーバーがバインドするホストとポートを指定
bind = "0.0.0.0:8000"

# ワーカープロセス数を設定
workers = multiprocessing.cpu_count() * 2 + 1
threads = 4

accesslog = "-"
errorlog = "-"
loglevel = "info"
capture_output = "True"

timeout = 120
