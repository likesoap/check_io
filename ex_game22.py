import sendgrid
# import os
from sendgrid.helpers.mail import *


def send_email(email_addr: str, name: str):
    sg = sendgrid.SendGridAPIClient(
        apikey='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')
    from_email = Email("test@example.com")
    to_email = Email(email_addr)
    subject = "Welcome"
    content = Content(
        "text/plain", 'hello'+name+', welcome!')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
