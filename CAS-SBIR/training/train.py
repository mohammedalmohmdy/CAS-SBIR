
from training.seed_control import set_seed

def main():
    set_seed(42)
    print("Training pipeline initialized.")

if __name__ == "__main__":
    main()
