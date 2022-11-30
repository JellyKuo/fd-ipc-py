import os
 
print ("[second.py] Start")
 
# 選項 1: 使用自訂 FD 3
# * 執行命令: python first.py 3> >( 3>&0- python second.py )
#            ┌────────────── ┌─ ┌─ ┌──── ┌─────────────── ─
#  1. 執行第一個 Python       │  │  │     └ 2. 執行第二個 Python
#                            │  │  └ 3. 3>&0- 將後面程式原本的 Stdin (FD 0) 重新導向至 FD 3 (3>&0)，並關閉 FD 0 (-)
#                            │  └ 4. >(...) 執行括弧內的命令，並取得其 Stdin (FD 0) 的 Global FD 檔案路徑
#                            │  └    此命令的輸出為 /dev/fd/XXX，是一個代表後面程式 FD 0 的一個路徑，這個動作叫 Process Substition
#                            └ 5. 將左邊程式的 FD 3 打開，並且將內容輸出至後面這個檔案
# * 使用選項 2 時不需此行
pipe_file = os.fdopen(3, "r")
 
# 選項 2: 使用 Stdin (FD 0)
# * 執行命令: python first.py 3> >( python second.py )
#            ┌────────────── ┌─ ┌─ ┌─────────────── ─
#  1. 執行第一個 Python       │  │  └ 2. 執行第二個 Python
#                            │  └ 3. >(...) 執行括弧內的命令，並取得其 Stdin (FD 0) 的 Global FD 檔案路徑
#                            │  └    此命令的輸出為 /dev/fd/XXX，是一個代表後面程式 FD 0 的一個路徑，這個動作叫 Process Substition
#                            └ 4. 將左邊程式的 FD 3 打開，並且將內容輸出至後面這個檔案
# * 因為選項 2 使用 Stdin，等同直接於 Console 輸入的效果，可以透過單獨跑起來直接打字的方式測試 second 程式
#   但也會造成若 second 程式本身已有使用 Console 控制 (並非 first 輸入的操控)，first 串接時需要繞過 Console 的話，選項 1 就可以達到這個效果
 
while(True) :
    # 選項 1: 使用 readline() 讀取
    # 注意 readline 不會將最後的換行符號移除
    pipe_file_line = pipe_file.readline()
    print("[second.py] Receive data with pipe_file: " + pipe_file_line)
 
    # 選項 2: 使用 input 讀取
    # inp = input()
    # print("[second.py] Receive data with input: " + inp)
