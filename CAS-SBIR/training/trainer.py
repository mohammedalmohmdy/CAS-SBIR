
class Trainer:
    def __init__(self, model, loss_fn, optimizer):
        self.model=model
        self.loss_fn=loss_fn
        self.optimizer=optimizer
    def train(self,loader):
        self.model.train()
        for s,p,n,a in loader:
            out=self.model(s,p,a)
