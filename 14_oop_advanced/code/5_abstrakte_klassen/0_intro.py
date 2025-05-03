from abc import ABC, abstractmethod


class Worker(ABC):
    def __init__(self, name):
        self.name = name
        self._tools = []

    @property
    @abstractmethod
    def tools(self): ...

    @abstractmethod
    def task(self): ...


class Carpenter(Worker):
    def task(self):
        print(f"{self.name} is doing carpentry work with: {self.tools}")

    @property
    def tools(self):
        return self._tools

    @tools.setter
    def tools(self, tools):
        self._tools = tools


c = Carpenter("Carlo")
c.tools = ["Saw", "Screwdriver"]
c.task()
