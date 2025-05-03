
class PositiveIntegerField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self  # Zugriff über Klasse
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Wert muss eine positive ganze Zahl sein.")
        setattr(instance, self.name, value)


class JobConfig:
    retries = PositiveIntegerField()
    timeout = PositiveIntegerField()

    def __init__(self, retries, timeout):
        self.retries = retries
        self.timeout = timeout


job = JobConfig(retries=3, timeout=10)
print(job.retries)   # → 3

job.retries = 5
print(job.retries)   # → 5

job.timeout = -1     # → ValueError: Wert muss eine positive ganze Zahl sein.
