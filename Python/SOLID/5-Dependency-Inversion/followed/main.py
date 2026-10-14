from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self,message):pass


class EmailService(NotificationChannel):
    def send(self, message):
        print(f"Sending Email : {message}")

class SMSService(NotificationChannel):
    def send(self, message):
        print(f"Sending SMS : {message}")


class NotificationService:
    def __init__(self, notifier:NotificationChannel):
        self.__notifier = notifier

    def notify(self, message):
        self.__notifier.send(message)



if __name__ == "__main__":

    sms_service = SMSService()
    email_service = EmailService()

    ns = NotificationService(sms_service)
    ns.notify("Sms...")
