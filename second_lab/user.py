import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Привіт з лабораторної роботи!"

print(f"UDP ціль: {UDP_IP}:{UDP_PORT}")
print(f"Повідомлення: {MESSAGE}")

# 1. Створення сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. Відправка даних
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

# Чекаємо відповідь від сервера
data, server = sock.recvfrom(1024)
print(f"Відповідь від сервера: {data.decode('utf-8')}")

# 6. Закриття сокета
sock.close()