Практическое занятие Nginx

python3 -m venv venv
source activate
pip3 install -r req.txt

uvicorn main:app --host 0.0.0.0 --port 8888

Документация
https://nginx.org/en/docs/

Задача 1 

Установите nginx и получите от него в браузере hello world


Задача 2
Измените конфигурационный файл так чтобы он обслуживал index1.html и index2.html

в бразуре по адресу http://localhost:8080/plants/ и http://localhost:8080/cosmos/

исправить возможную ошибку? В конфиге ли проблема?

Задача 3
Изменть конфигурационный файл так чтобы не проходили запросы от Insomnia|Selenium|WebDriver|HeadlessChrome
делать в директиве server

Для проверки
curl -H "User-Agent: Insomnia/2023.5.5" http://localhost:8080/cosmos/

Задача 4
Настроить обратный прокси для ФастАпи сервера в Main.py



Полезные команды
# Если установили через Homebrew
cd /usr/local/etc/nginx

# тест перед запуском
sudo nginx -t

# запуск nginx
sudo nginx
root /Users/konstantinreznikov/PycharmProjects/nginx_task;

# проверить что nginx запущен
sudo systemctl status nginx

# проверить что nginx слушает порт
sudo netstat -tulpn | grep :80

# перезапуск nginx
sudo nginx -s reload

# остановить nginx
sudo nginx -s stop

# если порт занят
sudo lsof -i :8080
sudo netstat -tulpn | grep :8080
sudo kill -9 <PID>


Логи

Linux
    Access Log: /var/log/nginx/access.log
    Error Log: /var/log/nginx/error.log
macOS
    Access Log: /usr/local/var/log/nginx/access.log
    Error Log: /usr/local/var/log/nginx/error.log
