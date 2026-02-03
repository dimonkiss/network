import socket


def start_client():
    # 1. Створення сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '127.0.0.1'
    port = 12345

    try:
        # 4. Встановлення з'єднання
        client_socket.connect((server_ip, port))
        print(f"Підключено до сервера {server_ip}")

        # 5. Відправка даних
        message = "Привіт, Сервер! Це Клієнт."
        client_socket.send(message.encode('utf-8'))

        # 6. Отримання відповіді
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Відповідь сервера: {data}")

    finally:
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
        print("Клієнт завершив роботу.")


if __name__ == "__main__":
    start_client()