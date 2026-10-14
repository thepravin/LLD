from email_service import EmailService
from sms_service import SMSService


class NotificationService:
    def __init__(self):
        self.__email_service=EmailService()
        self.__sms_service=SMSService()

    def notifyByEmail(self, message):
        self.__email_service.send_email(message)

    def notifyBySMS(self,message):
        self.__sms_service.send_sms(message)

