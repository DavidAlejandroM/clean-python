import os
import yaml
from pathlib import Path
from src.domain.model.scheduler import SchedulerProperty
from src.infraestructure.utils.env_utils import replace_env_vars

def load():
    root_dir = os.environ.get('GENOMICA_AGENT_HOME')
    if not root_dir:
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)
        root_dir = os.path.dirname(os.path.dirname(current_dir))
    with open(f'{root_dir}/application.yml', 'r') as file:
        properties = yaml.load(file, Loader=yaml.FullLoader)

    return replace_env_vars(properties)

def load_property_sheduler_datalake()-> SchedulerProperty:
    return SchedulerProperty(**load()['scheduler-agent'])