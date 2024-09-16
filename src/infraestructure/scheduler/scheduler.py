import time
import datetime as dt
import schedule as sche
import threading as th
from src.infraestructure.logging.logging import Logging
from src.domain.usecase.generic_use_case import GenericUseCase
from src.domain.model.scheduler import SchedulerProperty


class Scheduler:
    thread: th.Thread
    def __init__(self, use_case: GenericUseCase, property: SchedulerProperty, logger: Logging):
        self.use_case = use_case
        self.property = property
        self.scheduler = sche.every(self.property.interval).seconds.do(self.execute)
        self.logger = logger

    def start(self):
        self.logger.info(f'Starting scheduler {self.property.name}')
        self.thread = th.Thread(target=self.run, name=self.property.name)
        self.thread.start()
        self.thread.join()

    def execute(self):
        files = self.use_case.execute()

    def run(self):
        while True:
            sche.run_pending()
            time.sleep(1)

    def stop(self):
        self.thread.stop()
        sche.clear()
        self.logger.info(f'Stopping scheduler {self.property.name}')
        print(f'Stopping scheduler {self.property.name}')