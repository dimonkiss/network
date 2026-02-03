import socket
import time


def speed_test_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)
    print("Сервер готовий до тестування швидкості...")

    conn, addr = server_socket.accept()
    print(f"Підключено: {addr}")

    total_received = 0
    start_time = time.time()

    while True:
        data = conn.recv(65536)
        if not data:
            break
        total_received += len(data)

    end_time = time.time()
    duration = end_time - start_time

    if duration > 0:
        speed_bps = total_received / duration
        speed_mbps = (speed_bps * 8) / (1024 * 1024)
        print(f"Отримано: {total_received / (1024 * 1024):.2f} MB")
        print(f"Час: {duration:.2f} сек")
        print(f"Швидкість: {speed_mbps:.2f} Mbps (Мбіт/с)")

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    speed_test_server()