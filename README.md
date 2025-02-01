# Genetic Algorithm Cipher Decryption 🧬🔐
This project demonstrates the use of a genetic algorithm (GA) to decrypt a simple substitution cipher. The encryption maps each letter in the plaintext to a unique character in the ciphertext using a one-to-one random substitution. The decryption process uses a GA to iteratively optimize a mapping, aiming to recover the original plaintext.

# 🔥Challenge For the Reader!🔥 

I've left a ciphertext in the repository that is not able to be decrypted with the current script. Try adjusting the parameters, fitness model, and word list to see if you can decrypt it!

# Why Use a Genetic Algorithm for Deciphering?💡
Substitution ciphers are a type of monoalphabetic cipher where each letter in the plaintext is replaced with another letter or symbol. To decrypt such a cipher, one must determine the correct mapping of ciphertext symbols back to plaintext letters.

## The Challenge⚔️: 
There are 
26
!
26! (factorial of 26) possible mappings for the English alphabet, making brute-force decryption infeasible for long ciphertexts.
## Heuristic Approach: A genetic algorithm is ideal because it efficiently searches large, complex solution spaces by mimicking biological evolution.
The GA doesn’t guarantee the optimal solution but performs well in finding "good enough" solutions by iteratively improving the population of candidate mappings.

## How the Genetic Algorithm Works

![image](https://github.com/user-attachments/assets/dd428d2c-6339-47ce-a812-02086cac30a8)

A genetic algorithm solves optimization problems by evolving a population of candidate solutions through a process inspired by natural selection. Here's how it applies to deciphering substitution ciphers:

### 1. Initialization 🌱
Population: The algorithm starts with a population of random mappings between ciphertext symbols and plaintext letters.
Diversity: A diverse initial population ensures the algorithm explores different parts of the solution space.
### 2. Fitness Function🏋️‍♂️
Each candidate mapping is evaluated based on how well it deciphers the ciphertext. The fitness function scores each mapping by:

#### Word Validity: Counting valid English words in the decrypted text.
Letter Frequency: Comparing the frequency of letters in the decrypted text with the expected frequencies in English (e.g., 'E' is the most common letter).
A higher fitness score indicates that the mapping produces more readable and meaningful text.

### 3. Selection🎯
Mappings with higher fitness scores are more likely to be selected as "parents" for the next generation. This ensures that better solutions have a greater influence on the next population.

### 4. Crossover🔀
Two parent mappings are combined to produce a new "child" mapping:

A portion of one parent’s mapping is copied to the child.
The remainder is filled using the other parent, ensuring the child’s mapping is valid (one-to-one).
### 5. Mutation🎲
To introduce randomness and avoid premature convergence to local optima:

A small portion of the child’s mapping is randomly altered (e.g., swapping two letters).
Mutation ensures the algorithm explores new solutions that may not be reachable through crossover alone.
### 6. Evolution🚀
The next generation is created from selected parents and mutated offspring.
Over successive generations, the population evolves toward mappings that produce higher fitness scores.
### 7. Stopping Criterion
#### The algorithm terminates when:

##### A sufficiently high fitness score is achieved (e.g., the decrypted text closely resembles readable English).
##### A fixed number of generations is reached.
## Advantages and Disadvantages of Using a Genetic Algorithm
### Scalability 📈:

GAs can handle the large solution space of substitution ciphers (26! mappings) more efficiently than brute-force methods.
### Heuristic Search:

Unlike deterministic approaches, GAs are heuristic, meaning they can find approximate solutions even when the problem is not fully understood.
### Adaptability:

The fitness function can be tailored to incorporate domain-specific knowledge, such as word lists or language patterns.
### Robustness:

GAs perform well in noisy or incomplete data environments, making them ideal for decrypting ciphertexts with errors or ambiguities.
Why the GA Might Struggle
### Word List Limitations 📖:

The fitness function heavily relies on a word list, which can bias the algorithm toward lesser-used words (e.g., "DESSA") instead of common phrases.
### Local Optima:

GAs can sometimes get stuck in suboptimal solutions, especially if the population lacks diversity.
### Time Complexity:

While faster than brute-force, GAs still require many generations and a sizable population to achieve good results for long ciphertexts.
### Conclusion
The genetic algorithm is a powerful tool for deciphering substitution ciphers because it combines randomness with optimization. While not guaranteed to find the optimal solution, it balances exploration and exploitation, making it highly effective for large solution spaces. Its performance can be further enhanced by refining the fitness function and introducing techniques to maintain population diversity.

# How It Works
## Encryption:

A plaintext message (e.g., HELLO WORLD) is encrypted using a randomly generated substitution cipher.
## Example Cipher Mapping:
Copy code
A -> Z   B -> X   C -> K   D -> G   E -> Q
F -> O   G -> P   H -> J   I -> A   J -> M
K -> L   L -> R   M -> Y   N -> F   O -> T
P -> N   Q -> B   R -> C   S -> U   T -> H
U -> W   V -> D   W -> E   X -> V   Y -> S
Z -> I
Example Ciphertext: JQRRT ECCTG
## Decryption:

The GA starts with a population of random mappings.
Fitness is evaluated based on:
Valid English word count.
Similarity of letter frequencies to English text.
Over successive generations, the GA evolves better mappings through selection, crossover, and mutation.
## Files
### encrypt.py: Encrypts a plaintext message using a random substitution cipher.
### ga_decrypt.py: Decrypts the ciphertext using a genetic algorithm.
### plaintext.txt: The plaintext message.
### ciphertext.txt: The encrypted message.
### cipher_mapping.json: The random substitution cipher used for encryption.
### decrypted_mapping.json: The best mapping found by the GA.
### fitness_plot.png: A graph showing the fitness progression over generations.
## Usage
### 1. Generate Plaintext
Run generate_plaintext.py to create a plaintext message:

bash
Copy code
python generate_plaintext.py
### 2. Encrypt the Plaintext
Encrypt the message using:

python encrypt.py
### 3. Decrypt the Ciphertext
Use the genetic algorithm to decrypt the message:
python ga_decrypt.py

### 4. Visualize Fitness
At the end of the decryption process, a graph (fitness_plot.png) will show the fitness progression over generations.

## Challenges and Observations
### Word List Limitations
The project relies on a dictionary of English words to evaluate decryption accuracy. However, this introduces challenges:

### Rare Words: Lesser-used words like DESSA and TARSI are treated as valid, skewing fitness scores.
### Ambiguity: High word counts in the plaintext may incorrectly reward mappings that generate valid but unrelated words.
## Potential Improvements:
Replace the current word list with a more refined set of commonly used words.
Introduce penalties for rare words or prioritize high-frequency words.
Convergence Issues
The GA occasionally converges prematurely to suboptimal solutions (local optima). To mitigate this:
Increase population diversity with techniques like adaptive mutation and random immigrants.
Adjust the fitness function to balance word count and letter frequency.
Future Enhancements
### Refine Word List:
Use a curated dictionary of high-frequency words to improve fitness evaluation.
### Dynamic Fitness Adjustment:
Weight letter frequency more heavily in the early generations and shift to word count in later stages.
### Alternative Optimization:
Experiment with other optimization techniques, such as simulated annealing or hybrid algorithms.
