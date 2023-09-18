from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py29',
        f'Привет перейди по этой ссылке чтобы активировать аккаунт: \n\n '
        f'http://localhost:8000/api/account/activate/{code}',
        'kimerkin3@gmail.com',
        [email]
    )