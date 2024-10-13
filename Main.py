
import numpy as np
import pandas as pd
import argparse
from Topsis import topsis  
def load(file_path):
    return pd.read_csv(file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--weights", nargs=5, type=float)
    
    args = parser.parse_args()
    
    df = load(args.input_file)

    # Default weights if none provided
    weights = [0.25] * 5 if args.weights is None else [w / sum(args.weights) for w in args.weights]
    weights_dict = dict(zip(['Accuracy', 'Precision', 'Recall', 'F1_score', 'ROC-AUC'], weights))

    results = df.groupby('Text').apply(lambda group: topsis(group, weights_dict)).reset_index(drop=True)
    results.to_csv(args.output_file, index=False)
    print(f"Saved in {args.output_file}")

if __name__ == "__main__":
    main()
