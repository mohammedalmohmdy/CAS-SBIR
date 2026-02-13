
from scipy.stats import ttest_rel

def paired_t_test(method_a, method_b):
    stat, p = ttest_rel(method_a, method_b)
    return p
