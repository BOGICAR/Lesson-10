# Задание №2 - сделано
def hide_email(email) -> str:
    email = email.split('@')
    email_0 = email[0][:-3]
    email_1 = email[1][2:]
    email = email_0 + '***@**' + email_1
    return email


print(hide_email('somebody_email@gmail.com'))
