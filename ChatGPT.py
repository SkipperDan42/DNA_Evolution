import random

def generate_dna_strand(length):
    """Generate a random DNA strand of a given length."""
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choice(bases) for _ in range(length))

# Dictionary of genes and corresponding physical features
genes = {
    'AAAT': 'Blue eyes',
    'CGCG': 'Brown hair',
    'TTAT': 'Tall height',
    'GGCC': 'Freckles',
    'ATGC': 'Green eyes',
    'TATA': 'Curly hair',
    'GAGA': 'Dimples'
}

# Dictionary of transcription factors and their effects on genes
transcription_factors = {
    'ACTG': {'AAAT': True},  # ACTG activates Blue eyes
    'TGCA': {'CGCG': False}, # TGCA deactivates Brown hair
    'GACT': {'TTAT': True},  # GACT activates Tall height
    'CTGA': {'GGCC': False}, # CTGA deactivates Freckles
    'CAGT': {'ATGC': True},  # CAGT activates Green eyes
    'GTAC': {'TATA': False}, # GTAC deactivates Curly hair
    'AGCT': {'GAGA': True}   # AGCT activates Dimples
}

# Color codes for terminal output
COLOR_MOTHER = "\033[95m"  # Magenta
COLOR_FATHER = "\033[94m"  # Blue
COLOR_BOTH = "\033[92m"    # Green
COLOR_NEITHER = "\033[91m" # Red
COLOR_RESET = "\033[0m"    # Reset

def find_genes(dna_strand, genes, transcription_factors, mother_strand=None, father_strand=None):
    """Find genes in a DNA strand and return the corresponding features, considering transcription factors."""
    active_genes = {gene: False for gene in genes.keys()}

    # Check for transcription factors
    for tf, effects in transcription_factors.items():
        if tf in dna_strand:
            for gene, state in effects.items():
                active_genes[gene] = state

    # Determine active features and their sources
    found_features = []
    color_coded_dna = []

    for i in range(len(dna_strand)):
        base = dna_strand[i]
        if mother_strand and father_strand:
            if base == mother_strand[i] and base == father_strand[i]:
                color_coded_dna.append(COLOR_BOTH + base + COLOR_RESET)
            elif base == mother_strand[i]:
                color_coded_dna.append(COLOR_MOTHER + base + COLOR_RESET)
            elif base == father_strand[i]:
                color_coded_dna.append(COLOR_FATHER + base + COLOR_RESET)
            else:
                color_coded_dna.append(COLOR_NEITHER + base + COLOR_RESET)
        else:
            color_coded_dna.append(base)

    for gene, feature in genes.items():
        if gene in dna_strand and active_genes[gene]:
            if mother_strand and father_strand:
                if gene in mother_strand and gene in father_strand:
                    source = COLOR_BOTH + feature + COLOR_RESET
                elif gene in mother_strand:
                    source = COLOR_MOTHER + feature + COLOR_RESET
                elif gene in father_strand:
                    source = COLOR_FATHER + feature + COLOR_RESET
                else:
                    source = COLOR_NEITHER + feature + COLOR_RESET
            else:
                source = feature
            found_features.append(source)

    return found_features, ''.join(color_coded_dna)

def crossover(strand1, strand2):
    """Perform crossover between two DNA strands."""
    length = min(len(strand1), len(strand2))
    crossover_point = random.randint(1, length - 1)
    new_strand1 = strand1[:crossover_point] + strand2[crossover_point:]
    new_strand2 = strand2[:crossover_point] + strand1[crossover_point:]
    return new_strand1, new_strand2

def meiosis(strand1, strand2):
    """Simulate meiosis for two DNA strands."""
    # Duplicate chromosomes
    duplicated_strand1 = strand1 + strand1
    duplicated_strand2 = strand2 + strand2

    # Crossing over
    strand1_a, strand1_b = crossover(duplicated_strand1, duplicated_strand2)
    strand2_a, strand2_b = crossover(duplicated_strand2, duplicated_strand1)

    # Random segregation into gametes
    gamete1 = random.choice([strand1_a, strand1_b])
    gamete2 = random.choice([strand2_a, strand2_b])

    return gamete1, gamete2

def simulate_meiosis_for_parent():
    """Simulate meiosis for a parent to produce gametes."""
    # Set the length of each DNA strand
    strand_length = 50  # Adjust as needed

    # Generate 23 pairs of DNA strands (chromosomes)
    chromosomes_1 = [generate_dna_strand(strand_length) for _ in range(23)]
    chromosomes_2 = [generate_dna_strand(strand_length) for _ in range(23)]

    # Perform meiosis for each pair of chromosomes
    gametes = []

    for i in range(23):
        gamete1, gamete2 = meiosis(chromosomes_1[i], chromosomes_2[i])
        gametes.append(random.choice([gamete1, gamete2]))

    # Combine gametes to form a complete set
    combined_gamete = ''.join(gametes)
    return combined_gamete

def create_random_zygote(parent1, parent2):
    """Create a zygote by randomly selecting each base from the corresponding positions in the parent chromosomes."""
    zygote = []
    for base1, base2 in zip(parent1, parent2):
        zygote.append(random.choice([base1, base2]))
    return ''.join(zygote)

# Simulate meiosis for two parents
gamete1_parent1 = simulate_meiosis_for_parent()
gamete2_parent1 = simulate_meiosis_for_parent()

gamete1_parent2 = simulate_meiosis_for_parent()
gamete2_parent2 = simulate_meiosis_for_parent()

# Form a zygote from one gamete of each parent using meiosis
zygote_meiosis = gamete1_parent1 + gamete1_parent2

# Form a zygote by randomly selecting each base from the parent chromosomes
parent1_combined = ''.join([gamete1_parent1, gamete2_parent1])
parent2_combined = ''.join([gamete1_parent2, gamete2_parent2])
zygote_random = create_random_zygote(parent1_combined, parent2_combined)

# Find features in the zygotes
features_zygote_meiosis, colored_dna_meiosis = find_genes(zygote_meiosis, genes, transcription_factors, mother_strand=parent1_combined, father_strand=parent2_combined)
features_zygote_random, colored_dna_random = find_genes(zygote_random, genes, transcription_factors, mother_strand=parent1_combined, father_strand=parent2_combined)

print("Parent 1 Gamete 1:", gamete1_parent1)
print("Parent 1 Gamete 2:", gamete2_parent1)
print("Parent 2 Gamete 1:", gamete1_parent2)
print("Parent 2 Gamete 2:", gamete2_parent2)

print("\nZygote (Meiosis):")
print(colored_dna_meiosis)
print("Features in Zygote (Meiosis):")
for feature in features_zygote_meiosis:
    print(feature)

print("\nZygote (Random Selection):")
print(colored_dna_random)
print("Features in Zygote (Random Selection):")
for feature in features_zygote_random:
    print(feature)