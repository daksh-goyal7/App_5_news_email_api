import smtplib,ssl

def send_email(message):
    username="adygoyal07@gmail.com"
    password="yvwvkighpatudpsm"
    receiver="adygoyal07@gmail.com"

    context=ssl.create_default_context()
    host="smtp.gmail.com"
    port=465
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)