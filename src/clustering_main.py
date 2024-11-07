"""
Main file for clustering artworks.
"""

import argparse
import pandas as pd
from artwork_clustering import ArtworkClusterer


if __name__ == "__main__":
    # command line arguments
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--finetuned_model", type=str, default="models/finetuned-v2.pt")
    parser.add_argument("--signifiers", type=str, default="data/signifiers.pkl")
    parser.add_argument("--dataset", type=str, default="data/embeddings.csv")
    parser.add_argument("--method", type=str, default=None)
    parser.add_argument("--n_terms", type=int, default=5)

    parser.add_argument("--n_clusters", type=int, default=10)
    parser.add_argument("--eps", type=float, default=0.2)
    parser.add_argument("--min_samples", type=int, default=20)
    parser.add_argument("--reduce_with", type=str, default=None)
    parser.add_argument("--n_components", type=int, default=32)
    parser.add_argument("--represent_with", type=str, default="centroid")

    args = parser.parse_args()

    df = pd.read_csv(args.dataset)
    # 1. initialize the clusterer
    clusterer = ArtworkClusterer(
        model_path=args.finetuned_model,
        dataset=df,
        signifiers_path=args.signifiers
    )

    # 2. perform clustering
    clusterer.cluster(
        method=args.method,
        reduce_with=args.reduce_with,
        represent_with=args.represent_with,
        n_terms=args.n_terms,
        n_clusters=args.n_clusters,
        eps=args.eps,
        min_samples=args.min_samples,
        n_components=args.n_components
    )
