import os
import time
 
print("[first.py] Start")
 
# 以寫入模式開啟 FD 3
# FD 0: Stdin, 1: Stdout, 2: Stderr, 3 ~ 9 可以自由使用。避免使用 9 以上，Shell 內部會使用
# 第三個參數 0 為 buffer size，Python 預設所有 IO 皆為 Buffered，須於執行時指定 python -u 或在開檔案時指定 unbuffered
# Unbuffered 很重要，因為輸出的目的地不是 Shell 而是另一個程式，Python 沒辦法判斷控制 Flush，如果沒有手動 Flush buffer 滿前在對面是接收不到的
pipe_file = os.fdopen(3, "wb", 0)
 
counter = 0
while(True):
    print(f"[first.py] Send data: {counter}")
    # 直接以 Write 寫入，這個範例使用換行符號 \n 做為結尾切割符號
    # Unbuffered IO 的關係，必須要傳入 bytes，不能傳入 string，所以要 encode
    pipe_file.write(f"Data {counter}\n".encode("utf-8"))
    # 也可以使用 b"..." 的方式，少寫 .encode("utf-8")
    # pipe_file.write(b"blah\n")
    counter += 1
    time.sleep(1)
