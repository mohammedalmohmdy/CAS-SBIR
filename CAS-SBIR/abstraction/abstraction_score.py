
import torch

def normalize_features(x):
    return (x - x.min()) / (x.max() - x.min() + 1e-8)

def compute_abstraction_score(features, weights):
    norm = normalize_features(features)
    score = (norm * weights).sum(dim=-1)
    return torch.clamp(score, 0, 1)
