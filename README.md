Программа обращается к сетевым устройствам и выводит в консоль
пароли от wi fi сетей и их названия, которые были введены в ручную.
 Цель - быстро посмотреть wi fi пароль, который забыл!

**Объяснение:**

1. Код использует модуль `subprocess` для выполнения команд в командной строке.
2. Сначала выполняется команда "netsh wlan show profiles" для получения списка профилей Wi-Fi, и вывод декодируется с использованием кодировки 'cp866'.
3. Затем извлекаются имена профилей Wi-Fi из вывода.
4. Инициализируется пустая строка `pass_wifi` для хранения имен профилей и паролей Wi-Fi.
5. Происходит итерация по каждому профилю Wi-Fi, выполняется команда "netsh wlan show profile <profile_name> key=clear" для получения подробной информации о каждом профиле, включая пароль.
6. Извлекается информация о пароле из вывода и добавляется к строке `pass_wifi`.
7. Наконец, выводятся собранные имена профилей Wi-Fi и пароли. Если возникают исключения в процессе выполнения, выводится сообщение об ошибке.
