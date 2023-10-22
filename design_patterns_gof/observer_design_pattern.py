"""
Observer design pattern:
The Observer design pattern is a behavioral design pattern that defines a
one-to-many dependency between objects. In this pattern, one object (the subject or publisher)
maintains a list of its dependents (observers or subscribers) and notifies them of state changes,
usually by calling one of their methods. It's a way to implement distributed event handling
systems, in which an object (the subject) maintains a list of observers interested in its state changes.
"""


# Observer (Subscriber) Interface
class Observer:
    def update(self, message):
        pass


# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")


# Subject (Publisher)
class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def state_change(self, new_state):
        self.notify_observers(f"State changed to {new_state}")


# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self.state = state

    def set_state(self, new_state):
        self.state = new_state
        self.state_change(new_state)


# Client
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject = ConcreteSubject("Initial State")
subject.register(observer1)
subject.register(observer2)

subject.set_state("New State")
