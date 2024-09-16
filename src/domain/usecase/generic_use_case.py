from src.infraestructure.logging.logging import Logging

class GenericUseCase:
    def __init__(self, logger: Logging):
        self.logger = logger

    def execute(self):
        self.logger.info('Executing use case')
    