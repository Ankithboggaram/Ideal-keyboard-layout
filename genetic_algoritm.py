import random 
import numpy as np

# Creating the population of the first generation
def init_population(population_size):
    # List containing all the characters on the keyboard
    keyboard_characters = list('qazwsxedcrfvtgbyhnujmik,ol.p;/')

    population = []
    
    for i in range(population_size):
        random_genome = keyboard_characters[:]
        # Shuffling the characters
        random.shuffle(random_genome)
        # Addding this to the population
        population.append(random_genome)
    
    return population

# Creating a function to combine two keyboards together
def mate(keyboard_layout1, keyboard_layout2):
    # Taking a random integer from 0 to 29 since we have 30 characters on the keyboard
    i = random.randint(0,29)
    length = random.randint(0,29)
    # Initailizing the child layout with blank spaces
    child = [' ' for i in range(30)]
    
    # Adding keys from keyboard layout 1
    for i in range(length):
        if i > 29:
            i = 0
        child[i] = keyboard_layout1[i]
        i += 1

    # Now adding the remaining keys from keyboard layout 2
    j = i
    while ' ' in child:
        if i > 29:
            i = 0
        if j > 29:
            j = 0
        character = keyboard_layout2[i]
        if character in child:
            i +=1
            continue
        child[j] = keyboard_layout2[i]
        j += 1
        i += 1

    # Creating a random mutation
    probability = random.random()
    if probability >= 0.9:
        position1 = random.randint(0,29)
        position2 = random.randint(0,29)
        allele1 = child[position1]
        allele2 = child[position2]
        child[position1] = allele2
        child[position2] = allele1

    return child

# Creating the next generation of layouts
def new_generation(population, fitness, population_size):
    new_generation = []
    sorted_population = [0 for i in range(population_size)]
    # Sorting population by Fitness value
    for i in range(len(population)):
        sorted_population[fitness[i]] = (population[i])

    # Copying the best 10% layouts to the next generation
    for i in range(int(population_size * 0.1)):
        new_generation.append(sorted_population[i])

    # Combining two keyboards from the top 50% of the generation and adding the new keyboard to the next generation
    for i in range(int(population_size * 0.9)):
        population1 = random.choice(sorted_population[:int(population_size * 0.5)])
        population2 = random.choice(sorted_population[:int(population_size * 0.5)])
        child = mate(population1, population2)
        new_generation.append(child)
    
    return new_generation

# Calculating the fitness value of the keyboard layout
def calculate_fitness(keyboard_layout):
    # https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html shows us the most frequently occurring letters
    # Ensure that these letters appear on the home row of the keyboard layout, to minimise distance travelled by fingers to reach them
    # Home row: https://www.computerhope.com/jargon/h/hrk.htm
    # Home row indices are 1, 4, 7, 10, 19, 22, 25, 28
    
    # Implementation pending
    
    return 0


# Calculating the fitness value of each keyboad layout in the population
def create_fitness_list(population, population_size):
    # Making a list containing the fitness rank of all the keyboard layouts
    fitness = []
    # This list will contain the integer value of fitness, 1 being most fit, population size being the least fit
    
    # This will be the actual implementation
    # for i in range(population_size):
    #     fitness.append(calculate_fitness(population[i]))

    # Dummy implemntation, randomly decides which layout is most fit
    fitness = random.sample(list(range(0,population_size)), len(list(range(0,population_size))))
    return fitness

# The main function
if __name__ == "__main__":

    # Initializing the population of size given by the user
    n = int(input("Enter the population size: "))
    population = init_population(n)

    iterations = int(input("Enter the number of generations: "))
    fitness = create_fitness_list(population, n)

    # Running the genetic algorithm
    i = 0
    while i < iterations:
        generation = new_generation(population, fitness, n)
        i += 1
    
    # Picking the keyboard layout from the last generation with the lowest distance measure (Most fit) to be the ideal keyboard layout
    print("After", iterations, "generations, the ideal layout is: ")
    print(np.array(generation[0]).reshape(3,10))