import smtplib,ssl

def send_email(message):
    #Enter your gmail id here.
    username="example@gmail.com"
    # App Generated Password here.
    password="yvwvkighpatudpsm"
    receiver="example@gmail.com"

    context=ssl.create_default_context()
    host="smtp.gmail.com"
    port=465
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
