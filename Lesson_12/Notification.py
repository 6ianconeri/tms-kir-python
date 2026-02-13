from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SmsNotification(Notification):
    def send(self, message):
        print(f"Сообщение '{message}' успешно отправлено через СМС")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Сообщение '{message}' успешно отправлено через Email")

class PostNotification(Notification):
    def send(self, message):
        print(f"Сообщение '{message}' успешно отправлено почтой")

sms = SmsNotification()
email = EmailNotification()
post = PostNotification()

sms.send("Привет, как дела? :)")
email.send("Привет, как дела? :)")
post.send("Привет, как дела? :)")