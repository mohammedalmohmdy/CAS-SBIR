
DATASET_REGISTRY = {}
MODEL_REGISTRY = {}
LOSS_REGISTRY = {}

def register_dataset(name):
    def wrap(cls):
        DATASET_REGISTRY[name]=cls
        return cls
    return wrap

def register_model(name):
    def wrap(cls):
        MODEL_REGISTRY[name]=cls
        return cls
    return wrap

def register_loss(name):
    def wrap(cls):
        LOSS_REGISTRY[name]=cls
        return cls
    return wrap
