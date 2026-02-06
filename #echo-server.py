import socket
import time

HOST = "0.0.0.0"
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        counter = 1
        while True:
            # Отправляем сообщение клиенту
            message = f"Server message #{counter}\n"
            conn.sendall(message.encode('utf-8'))
            
            # Проверяем, не отправил ли клиент "exit"
            try:
                conn.settimeout(0.5)  # Небольшая задержка для проверки
                data = conn.recv(1024)
                if data:
                    client_msg = data.decode('utf-8').strip()
                    print(f"Received: {client_msg}")
                    if client_msg.lower() == "exit":
                        conn.sendall(b"Server stopping...\n")
                        break
            except socket.timeout:
                pass
            
            counter += 1
            time.sleep(1)  # Задержка между сообщениями

print("Connection closed")