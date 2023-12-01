import socket
conn = True
while conn:
    c = socket.socket()
    c.connect(("127.0.0.1",9999))

    mesg = input("Marks - ")
    c.send(bytes(mesg, 'UTF-8'))
    if mesg == "exit":
        conn = False
        break


    receivedmesg = c.recv(1024).decode()
    print("Server:", receivedmesg)
c.close()