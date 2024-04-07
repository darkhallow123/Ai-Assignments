from search import Problem, Node
import random
import itertools
import numpy as np
import sys
import time

class EightPuzzle(Problem):
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        return state.index(0)

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]
        return tuple(new_state)

    def goal_test(self, state):
        return state == self.goal

    def value(self, state):
        return sum(s != g for (s, g) in zip(state, self.goal))
      
def hill_climbing_steepest_ascent(problem):
    current = Node(problem.initial)
    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break
        neighbor = max(neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) <= problem.value(current.state):
            break
        current = neighbor
    return current.state
  
def hill_climbing_first_choice(problem):
    current = Node(problem.initial)
    while True:
        neighbors = current.expand(problem)
        random.shuffle(neighbors)  # Mezcla aleatoriamente los vecinos
        for neighbor in neighbors:
            if problem.value(neighbor.state) < problem.value(current.state):
                current = neighbor
                break
        else:  # Si no se encontró un vecino mejor
            break
    return current.state
  
def hill_climbing_random_restart(problem, num_restarts=100):
    best = None
    best_value = float('inf')
    for _ in range(num_restarts):
        solution = hill_climbing_steepest_ascent(problem)
        solution_value = problem.value(Node(solution).state)
        if solution_value < best_value:
            best = solution
            best_value = solution_value
    return best
  
def simulated_annealing(problem, schedule):
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return current.state  # Asegúrate de devolver el estado, no el nodo completo
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        if delta_e < 0 or random.uniform(0, 1) < np.exp(-delta_e / T):
            current = next_choice
          
def exp_schedule(k=20, lam=0.005, limit=1000):
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)
  
def generate_random_instance():
    instance = list(range(9))
    random.shuffle(instance)
    return tuple(instance)

def is_soluble(instance):
    inversions = 0
    for i in range(len(instance)):
        for j in range(i + 1, len(instance)):
            if instance[i] > instance[j] and instance[i] != 0 and instance[j] != 0:
                inversions += 1
    return inversions % 2 == 0
def test_algorithm(algorithm, problem_class, goal_state, num_instances=50):
    times = []
    solution_lengths = []
    solved_count = 0

    for _ in range(num_instances):
        initial_state = generate_random_instance()  # Genera instancia aleatoria
        soluble = is_soluble(initial_state)  # Chequea si es soluble
        if not soluble:
            continue  # Si no es soluble, pasa a la siguiente iteración
        
        problem = problem_class(initial_state, goal_state)
        start_time = time.time()
        solution = algorithm(problem)
        end_time = time.time()

        if solution:
            solved_count += 1
            solution_length = len(solution.solution()) if isinstance(solution, Node) else len(solution)
            solution_lengths.append(solution_length)
        else:
            solution_lengths.append(None)

        times.append(end_time - start_time)

    avg_time = sum(times) / len(times)
    avg_solution_length = sum(filter(None, solution_lengths)) / len(solution_lengths) if solution_lengths else float('inf')
    solved_percentage = (solved_count / num_instances) * 100

    print(f"Average time: {avg_time:.4f} seconds")
    print(f"Average solution length: {avg_solution_length}")
    print(f"Solved Percentage: {solved_percentage}%")
  
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Probando Hill Climbing Steepest-Ascent
test_algorithm(hill_climbing_steepest_ascent, EightPuzzle, goal_state)

# Probando Hill Climbing First-Choice
test_algorithm(hill_climbing_first_choice, EightPuzzle, goal_state)

# Probando Hill Climbing con Reinicio Aleatorio
test_algorithm(lambda p: hill_climbing_random_restart(p, num_restarts=5), EightPuzzle, goal_state)

# Probando Simulated Annealing
test_algorithm(lambda p: simulated_annealing(p, schedule=exp_schedule()), EightPuzzle, goal_state)
