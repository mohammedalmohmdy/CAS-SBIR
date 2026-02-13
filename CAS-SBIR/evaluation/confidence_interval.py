
import numpy as np
from scipy import stats

def compute_confidence_interval(results, confidence=0.95):
    mean = np.mean(results)
    std = np.std(results, ddof=1)
    n = len(results)
    h = stats.t.ppf((1 + confidence) / 2., n-1) * std / np.sqrt(n)
    return mean, h
