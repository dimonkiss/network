import socket


def start_server():
    # 1. Створення TCP сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Прив'язка до інтерфейсу
    host = '0.0.0.0'
    port = 12345
    server_socket.bind((host, port))

    # 3. Перехід у режим прослуховування
    server_socket.listen(1)
    print(f"Сервер запущено. Очікування підключення на {host}:{port}...")

    # 4. Прийняття нового з'єднання
    client_socket, addr = server_socket.accept()
    print(f"З'єднання встановлено з: {addr}")

    try:
        # 6. Отримання даних
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Отримано від клієнта: {data}")

        # 5. Відправка відповіді
        response = "Повідомлення отримано!"
        client_socket.send(response.encode('utf-8'))

    finally:
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
        server_socket.close()
        print("З'єднання закрито.")


if __name__ == "__main__":
    start_server()