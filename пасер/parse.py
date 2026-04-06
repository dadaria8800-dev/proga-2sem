
ip_c = {}  # для IP
status_c = {}  # для кодов
path_c = {}  # для путей
total_size = 0  # для общего размера
total_requests = 0  # проценты


with open('logs.txt', 'r') as file:
    for line in file:
        if not line.strip():  # пропускаем пустые строки
            continue

        parts = line.split()

        ip = parts[0]
        path = parts[5]
        status = parts[7]
        size_str = parts[8]

        if ip in ip_c:
            ip_c[ip] += 1
        else:
            ip_c[ip] = 1

        if status in status_c:
            status_c[status] += 1
        else:
            status_c[status] = 1

        if path in path_c:
            path_c[path] += 1
        else:
            path_c[path] = 1

        if size_str.isdigit():
            total_size += int(size_str)

        total_requests += 1



print("Топ-5 IP-адресов по частоте:")
sorted_ips = sorted(ip_c.items(), key=lambda x: x[1], reverse=True)[:5]
for ip, count in sorted_ips:
    percent = (count / total_requests) * 100
    print(f"{ip} - {count} запросов ({percent:.1f}%)")

print("\nОбщее количество запросов:")
for status, count in status_c.items():
    percent = (count / total_requests) * 100
    print(f"{status} - {count} запроса ({percent:.1f}%)")

print("\nТоп 3 популярных путей:")
sorted_paths = sorted(path_c.items(), key=lambda x: x[1], reverse=True)[:3]
for path, count in sorted_paths:
    print(f"{path} - {count} запроса")

print(f"\nОбщий размер ответа: {total_size}")