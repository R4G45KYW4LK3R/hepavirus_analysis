from collections import Counter
import matplotlib.pyplot as plt
import json

# --- Helper function ---
def normalize(counter):
    total = sum(counter.values())
    return {key: count / total for key, count in counter.items()}

# --- Load data ---
with open('../data/herpesvirus_genome.json') as f:
    data = json.load(f)

# --- Overall amino acid frequency ---
all_aa_counter = Counter()
for coding_region in data['coding_regions']:
    all_aa_counter.update(coding_region['translation'])
all_aa_freq = normalize(all_aa_counter)

# --- Category-wise frequency ---
amino_acid_counts_per_category = {'envelope': Counter(), 'membrane': Counter(), 'capsid': Counter()}

for coding_region in data['coding_regions']:
    for category, aa_counter in amino_acid_counts_per_category.items():
        if category in coding_region['product'].lower():
            aa_counter.update(coding_region['translation'])

aa_freq_per_category = {}
aa_relative_freq_per_category = {}

for category, aa_counter in amino_acid_counts_per_category.items():
    aa_freq = normalize(aa_counter)
    aa_freq_per_category[category] = aa_freq
    aa_relative_freq = {aa: freq / all_aa_freq[aa] for aa, freq in aa_freq.items()}
    aa_relative_freq_per_category[category] = aa_relative_freq

# --- Plot ---
for category, aa_freq in aa_freq_per_category.items():
    plt.figure(figsize=(10, 5))
    plt.bar(aa_freq.keys(), aa_freq.values(), color='coral')
    plt.title(f'Amino Acid Frequency - {category.capitalize()} Proteins')
    plt.xlabel('Amino Acid')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'aa-frequency-{category}.png')
    plt.close()

print("Category-wise amino acid frequency plots saved as PNG files.")
