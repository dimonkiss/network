import socket
import time


def speed_test_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '127.0.0.1'
    client_socket.connect((server_ip, 12345))

    # Генеруємо 100 МБ даних
    data_size_mb = 100
    chunk = b'X' * 65536
    total_bytes = data_size_mb * 1024 * 1024
    iterations = total_bytes // len(chunk)

    print(f"Починаю відправку {data_size_mb} MB...")
    start_time = time.time()

    for _ in range(iterations):
        client_socket.sendall(chunk)

    # Використовуємо shutdown, щоб сервер зрозумів, що дані закінчилися
    client_socket.shutdown(socket.SHUT_WR)

    end_time = time.time()
    duration = end_time - start_time

    speed_mbps = (total_bytes * 8) / (duration * 1024 * 1024)
    print(f"Тест завершено за {duration:.2f} сек")
    print(f"Ваша швидкість відправки: {speed_mbps:.2f} Mbps")

    client_socket.close()


if __name__ == "__main__":
    speed_test_client()