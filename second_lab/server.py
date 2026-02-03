import socket

# Налаштування
UDP_IP = "0.0.0.0"
UDP_PORT = 5005

# 1. Створення сокета (AF_INET = IPv4, SOCK_DGRAM = UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Прив'язка до порту
sock.bind((UDP_IP, UDP_PORT))

print(f"Сервер запущено на порту {UDP_PORT}. Очікування повідомлень...")

while True:
    # 4. Отримання даних (buffer size = 1024 байта)
    data, addr = sock.recvfrom(1024)
    print(f"Отримано повідомлення: {data.decode('utf-8')} від {addr}")

    sock.sendto(b"Message received!", addr)