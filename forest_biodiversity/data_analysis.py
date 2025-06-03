# This file was renamed from statistics.py to data_analysis.py to avoid shadowing the stdlib statistics module.

import pandas as pd
import numpy as np
from forest_biodiversity.agents import Tree, selected_species

def compute_species_stats(model):
    """Return a DataFrame with counts and mean size for each species."""
    data = []
    for sp in selected_species:
        trees = [a for a in model.agents_by_type[Tree] if a.species == sp]
        count = len(trees)
        mean_size = np.mean([t.size for t in trees]) if trees else 0
        data.append({
            'species': sp,
            'count': count,
            'mean_size': mean_size
        })
    return pd.DataFrame(data)

def compute_shannon_index(model):
    """Compute the Shannon diversity index for the current model state."""
    from math import log
    species_counts = [len([a for a in model.agents_by_type[Tree] if a.species == sp]) for sp in selected_species]
    total = sum(species_counts)
    if total == 0:
        return 0.0
    proportions = [count / total for count in species_counts if count > 0]
    shannon = -sum(p * log(p) for p in proportions)
    return shannon
