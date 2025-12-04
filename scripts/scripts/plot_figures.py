import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def volcano(df, fc_col="log2FC", p_col="pval", title="Volcano Plot"):
    plt.figure(figsize=(8,6))
    plt.scatter(df[fc_col], -np.log10(df[p_col]), s=10, alpha=0.5)
    plt.axvline(0.5, color="blue", linestyle="--")
    plt.axvline(-0.5, color="blue", linestyle="--")
    plt.axhline(-np.log10(0.05), color="blue", linestyle="--")
    plt.title(title)
    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10 p-value")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("This file contains plotting utilities.")
