import smtplib  # Импортируем библиотеку по работе с SMTP
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML
import asyncio


async def message(to_whom, username):
    addr_from = "weini_xuamshou@mail.ru"  # Адресант
    addr_to = to_whom  # Получатель
    password = "Ei1oyIUyJ3k-"  # Пароль

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресант
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = 'Приближение олимпиады!'
    body = f"Добрый день, {username}! Завтра откроется регистрация на олимпиаду РАНХиГС."
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Создаем объект SMTP
        server.starttls()  # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)  # Получаем доступ
        server.send_message(msg)  # Отправляем сообщение
        server.quit()
    except:
        pass
