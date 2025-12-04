import pandas as pd
import numpy as np
from scipy import stats

def compute_de(expr, group1_idx, group2_idx):
    x1 = expr.iloc[group1_idx]
    x2 = expr.iloc[group2_idx]
    
    # log2 fold-change
    logfc = np.log2(x1.mean(axis=0) + 1) - np.log2(x2.mean(axis=0) + 1)
    
    # Welch t-tests
    pvals = stats.ttest_ind(x1, x2, axis=0, equal_var=False).pvalue
    
    return pd.DataFrame({"log2FC": logfc, "pval": pvals})

if __name__ == "__main__":
    print("This file defines differential expression functions.")
