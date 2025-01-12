import random
import json
import string
from collections import Counter
import nltk
from nltk.corpus import words

# Load the word list using NLTK
def load_word_list():
    return set(word.upper() for word in words.words())

# Generate a random one-to-one mapping of the English alphabet
def generate_random_mapping():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# Decrypt the ciphertext using a given mapping
def decrypt_with_mapping(ciphertext, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    return "".join(reverse_mapping.get(char, char) for char in ciphertext)

# Fitness function that combines word count and letter frequency
def fitness_function(plaintext, word_list):
    # Split plaintext into words
    words_in_plaintext = plaintext.split()
    
    # Count valid words
    valid_word_count = sum(1 for word in words_in_plaintext if word in word_list)
    
    # Base score from letter frequencies
    letter_frequencies = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
        'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
        'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
        'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
        'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
    }
    plaintext_counter = Counter(plaintext)
    total_letters = sum(plaintext_counter.values())
    
    frequency_score = 0
    for letter, freq in letter_frequencies.items():
        observed_freq = (plaintext_counter.get(letter, 0) / total_letters) * 100 if total_letters > 0 else 0
        frequency_score += abs(freq - observed_freq)
    
    # Combine scores (higher is better, so we negate frequency_score)
    total_score = valid_word_count * 10 - frequency_score  # Adjust weight of word count as needed
    return total_score

# Initialize a population of random mappings
def initialize_population(size):
    return [generate_random_mapping() for _ in range(size)]

# Select two parents based on their fitness scores
def select_parents(population, fitnesses):
    return random.choices(population, weights=fitnesses, k=2)

# Combine two parent mappings to produce a valid child mapping
def crossover(parent1, parent2):
    keys = list(parent1.keys())
    split = random.randint(1, len(keys) - 1)
    
    # Start with part of parent1's mapping
    child_mapping = {key: parent1[key] for key in keys[:split]}
    
    # Fill the remaining entries from parent2, avoiding duplicates
    used_values = set(child_mapping.values())
    for key in keys[split:]:
        if parent2[key] not in used_values:
            child_mapping[key] = parent2[key]
            used_values.add(parent2[key])
    
    # Fill any missing letters to ensure the mapping is complete
    remaining_keys = [key for key in keys if key not in child_mapping]
    remaining_values = [value for value in keys if value not in child_mapping.values()]
    child_mapping.update(zip(remaining_keys, remaining_values))
    
    return child_mapping

# Mutate a mapping by swapping two random letters
def mutate(mapping):
    keys = list(mapping.keys())
    a, b = random.sample(keys, 2)
    mapping[a], mapping[b] = mapping[b], mapping[a]

# Evolve the population using the genetic algorithm
import matplotlib.pyplot as plt

def evolve_population(ciphertext, population, generations, word_list, initial_mutation_rate=0.1):
    mutation_rate = initial_mutation_rate
    fitness_history = []  # To store best fitness scores

    for generation in range(generations):
        # Evaluate fitness for each mapping
        fitnesses = [fitness_function(decrypt_with_mapping(ciphertext, mapping), word_list) for mapping in population]
        
        # Normalize fitness values to be positive
        min_fitness = min(fitnesses)
        if min_fitness < 0:
            fitnesses = [f - min_fitness + 1 for f in fitnesses]

        # Get the best fitness and store it
        best_fitness = max(fitnesses)
        fitness_history.append(best_fitness)

        # Select the best mapping for debugging
        best_mapping = population[fitnesses.index(best_fitness)]
        best_decrypted = decrypt_with_mapping(ciphertext, best_mapping)
        print(f"Generation {generation + 1}: Best fitness = {best_fitness:.2f}")
        print(f"Decrypted Text (Best): {best_decrypted[:100]}...\n")

        # Adapt mutation rate if stuck
        if generation > 0 and fitnesses.count(best_fitness) > 0.5 * len(fitnesses):
            mutation_rate = min(0.5, mutation_rate + 0.05)  # Increase mutation rate if stuck
        else:
            mutation_rate = max(0.1, mutation_rate - 0.01)  # Gradually decrease mutation rate otherwise

        # Create new population
        new_population = []
        for _ in range(len(population)):
            parent1, parent2 = select_parents(population, fitnesses)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)

        population = new_population

    # Plot fitness history
    plot_fitness_history(fitness_history)

    return population[fitnesses.index(max(fitnesses))]


def plot_fitness_history(fitness_history):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(fitness_history) + 1), fitness_history, marker="o", linestyle="-", color="b")
    plt.title("Best Fitness Score Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid()
    plt.savefig("fitness_plot.png")  # Save the plot to a file
    plt.show()  # Display the plot


# Load the ciphertext from file
def load_ciphertext():
    with open("ciphertext.txt", "r") as file:
        return file.read()

def main():
    # Load the ciphertext
    ciphertext = load_ciphertext()
    
    # Load the word list
    word_list = load_word_list()
    
    # Initialize the population
    population_size = 1000
    generations = 10000
    population = initialize_population(population_size)
    
    # Run the genetic algorithm
    best_mapping = evolve_population(ciphertext, population, generations, word_list)
    
    # Decrypt the ciphertext with the best mapping
    best_decrypted = decrypt_with_mapping(ciphertext, best_mapping)
    print("\nFinal Decrypted Text:")
    print(best_decrypted)
    
    # Save the best mapping to a file
    with open("decrypted_mapping.json", "w") as file:
        json.dump(best_mapping, file)

if __name__ == "__main__":
    main()
