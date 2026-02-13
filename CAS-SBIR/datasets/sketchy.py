
from pathlib import Path
from PIL import Image
import random, torch
from torch.utils.data import Dataset, DataLoader
from abstraction.cache_loader import AbstractionCache
from core.registry import register_dataset

@register_dataset("sketchy")
class SketchyDataset(Dataset):
    def __init__(self, root, split, cache_dir):
        self.root=Path(root)
        self.split=split
        self.cache=AbstractionCache(cache_dir)
        self.samples=[]
        sketch_dir=self.root/"sketch"
        photo_dir=self.root/"photo"
        for cls in sketch_dir.iterdir():
            sketches=list(cls.glob("*.png"))
            photos=list((photo_dir/cls.name).glob("*.jpg"))
            for s in sketches:
                self.samples.append((str(s),[str(p) for p in photos],cls.name))
    def __len__(self): return len(self.samples)
    def __getitem__(self,idx):
        s,photos,cls=self.samples[idx]
        pos=random.choice(photos)
        neg=random.choice(self.samples)[1][0]
        return torch.randn(3,224,224), torch.randn(3,224,224), torch.randn(3,224,224), self.cache.get(s)
    def get_query_loader(self,cfg):
        return DataLoader(self,batch_size=cfg["training"]["batch_size"])
    def get_gallery_loader(self,cfg):
        return DataLoader(self,batch_size=cfg["training"]["batch_size"])
