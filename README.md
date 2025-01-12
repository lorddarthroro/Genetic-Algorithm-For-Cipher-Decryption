# Genetic Algorithm Cipher Decryption
This project demonstrates the use of a genetic algorithm (GA) to decrypt a simple substitution cipher. The encryption maps each letter in the plaintext to a unique character in the ciphertext using a one-to-one random substitution. The decryption process uses a GA to iteratively optimize a mapping, aiming to recover the original plaintext.

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
