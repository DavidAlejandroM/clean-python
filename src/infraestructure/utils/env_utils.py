import os, re

def replace_env_vars(value):
    """
    Reemplaza las variables de entorno en un valor dado.

    Args:
        value (str, dict, list): El valor en el que se reemplazarán las variables de entorno.

    Returns:
        str, dict, list: El valor con las variables de entorno reemplazadas.

    Raises:
        None

    Examples:
        >>> replace_env_vars("${HOME}")
        '/Users/username'
        >>> replace_env_vars("Hello, ${NAME}!")
        'Hello, John Doe!'
    """
    if isinstance(value, str):
        match = re.match(r'\$\{(.+)\}', value)
        if match:
            env_var = match.group(1)
            return os.getenv(env_var)
        else:
            return value
    elif isinstance(value, dict):
        return {k: replace_env_vars(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [replace_env_vars(v) for v in value]
    else:
        return value