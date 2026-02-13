
import argparse, torch
from utils.config import load_config
from utils.seed import set_seed
from core.builder import build_dataset, build_model, build_loss
from training.trainer import Trainer

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    args=parser.parse_args()
    cfg=load_config(args.config)
    for seed in cfg["experiment"]["seeds"]:
        set_seed(seed)
        dataset=build_dataset(cfg)
        loader=dataset.get_query_loader(cfg)
        model=build_model(cfg)
        loss=build_loss(cfg)
        opt=torch.optim.Adam(model.parameters(),lr=cfg["optimizer"]["lr"])
        trainer=Trainer(model,loss,opt)
        trainer.train(loader)
    print("Completed")
if __name__=="__main__":
    main()
