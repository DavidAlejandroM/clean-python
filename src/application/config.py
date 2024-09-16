
from src.infraestructure.logging.logging import Logging
from src.infraestructure.scheduler import Scheduler
from src.domain.usecase import *
from src.infraestructure import *
from src.application.bean_container import BeanContainer

SCHEDULER = 'scheduler'
LOGGING = 'logging'
USE_CASE = 'use_case'

def scheduler() -> Scheduler:
    property = load_property_sheduler_datalake()
    container = BeanContainer()
    use_case = container.get_bean(USE_CASE)
    logger = container.get_bean(LOGGING)
    return Scheduler(use_case, property, logger)

# domain
def genericUseCase() -> GenericUseCase:
    container = BeanContainer()
    logger = container.get_bean(LOGGING)
    return GenericUseCase(logger)

def logger():
    return Logging()



def createAllBeans():
    """
    Crea y configura todos los beans necesarios para la aplicación.

    Returns:
        BeanContainer: El contenedor con todos los beans configurados.
    """
    container = BeanContainer()
    container.add_bean(LOGGING, logger())
    container.add_bean(USE_CASE, genericUseCase())
    container.add_bean(SCHEDULER, scheduler())

    return container
