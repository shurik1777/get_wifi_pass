import subprocess

try:
    # Выполнение команды "netsh wlan show profiles" и декодирование вывода с использованием кодировки 'cp866'
    data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')

    # Извлечение имен профилей из вывода
    profiles = [i.split(':')[1][1:-1] for i in data if "Все профили пользователей" in i]

    # Инициализация пустой строки для хранения профилей Wi-Fi и паролей
    pass_wifi = ''

    # Итерация по каждому профилю Wi-Fi
    for i in profiles:
        # Выполнение команды "netsh wlan show profile <profile_name> key=clear" для каждого профиля
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split(
            '\n')

        # Итерация по выводу команды
        for j in result:
            # Проверка, содержит ли строка "Содержимое ключа"
            if "Содержимое ключа" in j:
                # Добавление имени профиля Wi-Fi и пароля в строку pass_wifi
                pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"

    # Вывод собранных профилей Wi-Fi и паролей
    print(pass_wifi)

except Exception as ex:
    # Вывод сообщения об ошибке, если возникает исключение
    print(f'Ошибка: {ex}')
