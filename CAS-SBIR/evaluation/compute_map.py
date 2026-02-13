
import numpy as np

def compute_map(ranked_indices, ground_truth):
    average_precisions = []
    for i, ranking in enumerate(ranked_indices):
        relevant = ground_truth[i]
        hits = 0
        precision_sum = 0
        for j, idx in enumerate(ranking):
            if idx in relevant:
                hits += 1
                precision_sum += hits / (j + 1)
        average_precisions.append(precision_sum / max(len(relevant), 1))
    return np.mean(average_precisions)
