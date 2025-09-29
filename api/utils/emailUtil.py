from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.config import Config
from typing import List


config = Config('.env')
conf = ConnectionConfig(
    MAIL_USERNAME=config("MAIL_USERNAME"),
    MAIL_PASSWORD=config("MAIL_PASSWORD"),
    MAIL_FROM=config("MAIL_FROM"),
    MAIL_PORT=int(config("MAIL_PORT")),
    MAIL_SERVER=config("MAIL_SERVER"),
    MAIL_STARTTLS=config("MAIL_TLS", cast=bool, default=True),  # Đổi tên
    MAIL_SSL_TLS=config("MAIL_SSL", cast=bool, default=False),  # Đổi tên
    USE_CREDENTIALS=config("USE_CREDENTIALS", cast=bool, default=True)
)


async def send_email(subject: str, recipient: List, message: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
        subtype="html"
    )
    print(message)
    fm = FastMail(conf)
    await fm.send_message(message)