
import numpy as np, cv2, json
from pathlib import Path
from abstraction.extractor import extract_features

def compute_cache(sketch_root, cache_dir):
    sketch_root=Path(sketch_root)
    cache_dir=Path(cache_dir)
    cache_dir.mkdir(parents=True,exist_ok=True)
    paths=list(sketch_root.rglob("*.png"))
    feats=[]
    for p in paths:
        img=cv2.imread(str(p),0)
        feats.append(extract_features(img))
    feats=np.vstack(feats)
    minv,maxv=feats.min(0),feats.max(0)
    norm=(feats-minv)/(maxv-minv+1e-8)
    scores=norm.mean(1)
    np.save(cache_dir/"scores.npy",scores)
    with open(cache_dir/"meta.json","w") as f:
        json.dump({"paths":[str(p) for p in paths]},f)
