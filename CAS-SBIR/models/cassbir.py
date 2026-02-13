
import torch.nn as nn, torch.nn.functional as F, torchvision.models as models
from core.registry import register_model

@register_model("cassbir")
class CASSBIR(nn.Module):
    def __init__(self, embedding_dim=512):
        super().__init__()
        self.backbone=models.resnet18(weights=None)
        self.fc=nn.Linear(512,embedding_dim)
    def encode(self,x):
        x=self.backbone(x)
        x=self.fc(x)
        return F.normalize(x,dim=1)
    def forward(self,s,p,a):
        return self.encode(s), self.encode(p)
