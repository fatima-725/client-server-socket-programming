import socket
import json

s = socket.socket()
print("server created")
s.bind(("127.0.0.1",9999))
s.listen(3)
print("waiting for the connection")
conn = True
while conn:
    c,addr = s.accept()
    print (addr)
    recievedMsg = c.recv(1024).decode()
    print("Client", recievedMsg)

    if recievedMsg == "exit":
        conn = False
        break

    if recievedMsg >= "85" :
        msg = "Your grade is A"
    elif recievedMsg >= "80" and recievedMsg <= "84":
        msg = "Your grade is A-"
    elif recievedMsg >= "75" and recievedMsg <= "79":
        msg = "Your grade is B+"
    elif recievedMsg >= "71" and recievedMsg <= "74":
        msg = "Your grade is B"
    elif recievedMsg >= "68" and recievedMsg <= "70":
        msg = "Your grade is B-"
    elif recievedMsg >= "64" and recievedMsg <= "67":
        msg = "Your grade is C+"
    elif recievedMsg >= "61" and recievedMsg <= "63":
        msg = "Your grade is C"
    elif recievedMsg >= "58" and recievedMsg <= "60":
        msg = "Your grade is C-"
    elif recievedMsg >= "54" and recievedMsg <= "57":
        msg = "Your grade is D+"
    elif recievedMsg >= "50" and recievedMsg <= "53":
        msg = "Your grade is D"
    else:
        msg = "Your grade is F"

    c.send(bytes(msg, 'UTF-8'))

    with open('data.json','a', encoding='utf-8') as f:
       json.dump("Client:",f)
       json.dump(recievedMsg, f)
       f.write('\n')
       json.dump("Server:", f)
       json.dump(msg, f)
       f.write('\n')


c.close()
s.close()