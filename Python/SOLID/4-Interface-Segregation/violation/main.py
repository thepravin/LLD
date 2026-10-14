# Interface segregation principle ensures that classes are not forced to implement methods they don't need.


from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass


class Worker(Employee):
    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Worker is working")


class Robot(Employee):
    def eat(self):
        raise Exception("Robot can't eat")

    def work(self):
        print("Robot is working")