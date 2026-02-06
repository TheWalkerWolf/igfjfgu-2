import socket

HOST = "10.90.14.78"  # Замените на IP сервера
PORT = 13337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Получаем приветственное сообщение от сервера
    welcome_msg = s.recv(1024)
    print(welcome_msg.decode('utf-8'), end='')
    
    while True:
        # Пользователь вводит сообщение
        user_input = input("You: ")
        
        # Отправляем сообщение серверу
        s.sendall(user_input.encode('utf-8'))
        
        # Получаем ответ от сервера
        data = s.recv(1024)
        print(data.decode('utf-8'), end='')
        
        # Если пользователь ввел "exit", выходим
        if user_input.lower() == "exit":
            break

print("Disconnected from server")