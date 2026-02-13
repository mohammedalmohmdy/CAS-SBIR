
import numpy as np, json
from pathlib import Path

class AbstractionCache:
    def __init__(self, cache_dir):
        cache_dir=Path(cache_dir)
        self.scores=np.load(cache_dir/"scores.npy")
        with open(cache_dir/"meta.json") as f:
            meta=json.load(f)
        self.map={p:i for i,p in enumerate(meta["paths"])}
    def get(self,path):
        return float(self.scores[self.map[path]])
