'''
High-level modules(business logic) should not depend directly on low-level modules (specific implementations) both should depend on abstractions(interfaces)


notifiaction service depend on email, sms.... services
'''

from notification_service import NotificationService



if __name__ == "__main__":

    ns=NotificationService()

    ns.notifyByEmail("This is email...")
    ns.notifyBySMS("This is SMS...")