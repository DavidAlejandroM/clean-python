class SchedulerProperty:
    interval: int
    name: str
    def __init__(self, name: str, interval: int):
        self.name = name
        self.interval = interval
      

    def __str__(self) -> str:
        return f"name: {self.name}, timing: {self.timing}"