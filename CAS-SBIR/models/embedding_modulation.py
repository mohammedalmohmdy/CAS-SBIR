
import torch
import torch.nn as nn

class AbstractionModulation(nn.Module):
    def __init__(self, feature_dim):
        super().__init__()
        self.fc = nn.Linear(1, feature_dim)

    def forward(self, features, abstraction_score):
        gate = torch.sigmoid(self.fc(abstraction_score.unsqueeze(-1)))
        return features * gate
