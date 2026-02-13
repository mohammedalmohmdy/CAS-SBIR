
import torch.nn as nn, torch.nn.functional as F
from core.registry import register_loss

@register_loss("adaptive_triplet")
class AdaptiveTripletLoss(nn.Module):
    def __init__(self, base_margin=0.2, lambda_weight=0.7):
        super().__init__()
        self.base_margin=base_margin
        self.lambda_weight=lambda_weight
    def forward(self,a,p,n,ab):
        margin=self.base_margin+self.lambda_weight*ab
        dpos=1-F.cosine_similarity(a,p)
        dneg=1-F.cosine_similarity(a,n)
        return (dpos-dneg+margin).relu().mean()
