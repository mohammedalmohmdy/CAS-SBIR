
from core.registry import DATASET_REGISTRY, MODEL_REGISTRY, LOSS_REGISTRY

def build_dataset(cfg):
    return DATASET_REGISTRY[cfg['dataset']['name']](**cfg['dataset']['params'])

def build_model(cfg):
    return MODEL_REGISTRY[cfg['model']['name']](**cfg['model']['params'])

def build_loss(cfg):
    return LOSS_REGISTRY[cfg['loss']['name']](**cfg['loss']['params'])
