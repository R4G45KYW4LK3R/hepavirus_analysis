from operator import itemgetter
import matplotlib.pyplot as plt

# These must be imported from `aa-relative-freq.py` results
from aa_relative_freq import aa_relative_freq_per_category, aa_freq_per_category, all_aa_freq

def get_amino_acid_stats(aa, category):
    return '%s: freq ratio = %.2f, freq in category = %.4f, general freq = %.4f' % (
        aa,
        aa_relative_freq_per_category[category][aa],
        aa_freq_per_category[category][aa],
        all_aa_freq[aa]
    )

for category, aa_relative_freq in aa_relative_freq_per_category.items():
    max_aa, _ = max(aa_relative_freq.items(), key=itemgetter(1))
    min_aa, _ = min(aa_relative_freq.items(), key=itemgetter(1))
    
    print(f'{category}:')
    print('\t' + get_amino_acid_stats(max_aa, category))
    print('\t' + get_amino_acid_stats(min_aa, category))

    # --- Plot ---
    plt.figure(figsize=(6, 4))
    plt.bar([max_aa, min_aa],
            [aa_relative_freq[max_aa], aa_relative_freq[min_aa]],
            color=['green', 'red'])
    plt.title(f'Most vs Least Enriched AA in {category.capitalize()}')
    plt.ylabel('Relative Frequency Ratio')
    plt.tight_layout()
    plt.savefig(f'high-low-aa-{category}.png')
    plt.close()

print("High-low frequency plots saved.")
