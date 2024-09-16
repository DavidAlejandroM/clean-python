from datetime import datetime
import logging
import os

class Logging:
    
    def __init__(self):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        root_dir = os.environ.get('GENOMICA_AGENT_HOME')
        if not root_dir:
            current_file_path = os.path.abspath(__file__)
            current_dir = os.path.dirname(current_file_path)
            root_dir = os.path.dirname(os.path.dirname(current_dir))
        log_dir = os.path.join(root_dir, 'logs')
        log_file = os.path.join(log_dir, f'{now}.log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        logging.basicConfig(filename=log_file,
                            datefmt='%d-%b-%y %H:%M:%S', 
                            filemode='w', 
                            format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                            level=logging.INFO)
        logging.getLogger('azure.storage').setLevel(logging.WARNING)
        self.logger = logging
        
    def info(self, message):
        logging.info(message)
        
    def error(self, message):
        logging.error(message)
        
    def warning(self, message):
        logging.warning(message)
    
    def debug(self, message):
        logging.debug(message)