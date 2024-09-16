class BeanContainer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BeanContainer, cls).__new__(cls)
            cls._instance.beans = {}
        return cls._instance

    def add_bean(self, name, bean):
        self.beans[name] = bean

    def get_bean(self, name):
        if name not in self.beans:
            raise Exception(f"Bean {name} not found")
        return self.beans.get(name)