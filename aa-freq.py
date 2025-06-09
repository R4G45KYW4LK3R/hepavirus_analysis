from collections import Counter
import matplotlib.pyplot as plt

def normalize(counter):
    total = sum(counter.values())
    return {key: count / total for key, count in counter.items()}

amino_acid_counter = Counter()
import json

with open('../data/herpesvirus_genome.json') as f:
    data = json.load(f)

for coding_region in data['coding_regions']:
    amino_acid_counter.update(coding_region['translation'])

amino_acid_frequencies = normalize(amino_acid_counter)
print(amino_acid_frequencies)

# --- PLOT ---
plt.figure(figsize=(10, 6))
plt.bar(amino_acid_frequencies.keys(), amino_acid_frequencies.values(), color='skyblue')
plt.xlabel('Amino Acid')
plt.ylabel('Frequency')
plt.title('Amino Acid Frequency in Herpesvirus Proteome')
plt.tight_layout()
plt.savefig('aa-frequency.png')  # Save plot to file
plt.show()  # Show plot (if using a graphical interface)
