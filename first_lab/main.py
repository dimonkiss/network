import requests
import urllib.request
import math
import socket
import struct


def ip_to_int(ip):
    """Перетворює рядок IP у 32-бітне ціле число."""
    return struct.unpack("!I", socket.inet_aton(ip))[0]


def get_mask_from_size(size):
    """Обчислює бітову маску на основі кількості адрес."""
    bits = 32 - int(math.log2(size))
    mask = (0xFFFFFFFF << (32 - bits)) & 0xFFFFFFFF
    return mask


def main():
    print("--- Етап 1: Визначення вашої IP-адреси ---")
    try:
        my_ip = requests.get('https://api.ipify.org').text
        print(f"Ваша публічна IP-адреса: {my_ip}")
        my_ip_int = ip_to_int(my_ip)
    except Exception as e:
        print(f"Помилка при отриманні IP: {e}")
        return

    print("\n--- Етап 2: Завантаження та пошук у базі RIR ---")
    # URL для RIPE (Європа та Україна)
    url = "ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-latest"

    try:
        response = urllib.request.urlopen(url)

        found = False
        for line in response:
            line = line.decode('utf-8').strip()

            # Пропускаємо коментарі та порожні рядки
            if line.startswith('#') or not line:
                continue

            parts = line.split('|')

            # Шукаємо лише записи ipv4
            if len(parts) >= 7 and parts[2] == 'ipv4':
                net_addr = parts[3]
                try:
                    hosts_count = int(parts[4])

                    net_int = ip_to_int(net_addr)
                    mask = get_mask_from_size(hosts_count)

                    # Логічна операція: (IP AND MASK) == (NET AND MASK)
                    if (my_ip_int & mask) == (net_int & mask):
                        print(f"Рядок із файлу: {line}")

                        # Додаткова інформація для наочності
                        prefix = 32 - int(math.log2(hosts_count))
                        print(f"Мережа: {net_addr}/{prefix}")
                        found = True
                        break
                except ValueError:
                    continue

        if not found:
            print("Адресу не знайдено")

    except Exception as e:
        print(f"Помилка при роботі з FTP: {e}")


if __name__ == "__main__":
    main()