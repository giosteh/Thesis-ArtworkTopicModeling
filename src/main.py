
import argparse
from finetuning import CLIPFinetuner


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ep", "--epochs", type=int, default=50)
    parser.add_argument("-bs", "--batch_size", type=int, default=64)
    parser.add_argument("-lr", "--learning_rate", type=float, default=5e-5)
    parser.add_argument("-l", "--load", type=str, default=None)

    args = parser.parse_args()

    # finetuning
    finetuner = CLIPFinetuner(
        model_name="ViT-B/32",
        batch_size=args.batch_size,
        lr=args.learning_rate
    )

    if args.load:
        finetuner.load_model(args.load)

    finetuner.fit(epochs=args.epochs)    
