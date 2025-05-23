import numpy as np
import pandas as pd
from typing import List, Tuple
import json
import matplotlib.pyplot as plt

class GeneticAlgorithm:
    def __init__(
        self,
        population_size: int = 100,
        generations: int = 50,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.8,
        elite_size: int = 10
    ):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        self.best_fitness_history = []
        self.avg_fitness_history = []

    def load_data(self, filepath: str) -> Tuple[List[float], List[float], float]:
        """Carrega dados do arquivo JSON"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data['weights'], data['values'], data['capacity']

    def initialize_population(self, n_items: int) -> np.ndarray:
        """Inicializa população aleatória"""
        return np.random.randint(2, size=(self.population_size, n_items))

    def fitness(self, individual: np.ndarray, weights: List[float], 
                values: List[float], capacity: float) -> float:
        """Calcula fitness do indivíduo"""
        total_weight = np.sum(individual * weights)
        if total_weight > capacity:
            return 0
        return np.sum(individual * values)

    def selection(self, population: np.ndarray, fitness_scores: np.ndarray) -> np.ndarray:
        """Seleção por torneio"""
        selected = np.zeros((self.population_size, population.shape[1]))
        for i in range(self.population_size):
            # Seleciona 3 indivíduos aleatórios
            tournament = np.random.choice(
                self.population_size, 
                size=3, 
                replace=False
            )
            # Escolhe o melhor
            winner = tournament[np.argmax(fitness_scores[tournament])]
            selected[i] = population[winner]
        return selected

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Crossover de ponto único"""
        if np.random.random() < self.crossover_rate:
            point = np.random.randint(1, len(parent1))
            child1 = np.concatenate([parent1[:point], parent2[point:]])
            child2 = np.concatenate([parent2[:point], parent1[point:]])
            return child1, child2
        return parent1, parent2

    def mutation(self, individual: np.ndarray) -> np.ndarray:
        """Mutação bit a bit"""
        for i in range(len(individual)):
            if np.random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def evolve(self, weights: List[float], values: List[float], capacity: float) -> Tuple[np.ndarray, float]:
        """Evolui a população"""
        n_items = len(weights)
        population = self.initialize_population(n_items)
        
        for generation in range(self.generations):
            # Calcula fitness
            fitness_scores = np.array([
                self.fitness(ind, weights, values, capacity)
                for ind in population
            ])
            
            # Guarda histórico
            self.best_fitness_history.append(np.max(fitness_scores))
            self.avg_fitness_history.append(np.mean(fitness_scores))
            
            # Seleciona elite
            elite_indices = np.argsort(fitness_scores)[-self.elite_size:]
            elite = population[elite_indices]
            
            # Nova população
            new_population = elite.copy()
            
            # Preenche resto da população
            while len(new_population) < self.population_size:
                # Seleção
                parents = self.selection(population, fitness_scores)
                
                # Crossover
                for i in range(0, len(parents), 2):
                    if i + 1 < len(parents):
                        child1, child2 = self.crossover(parents[i], parents[i+1])
                        new_population = np.vstack([new_population, child1, child2])
            
            # Mutação
            for i in range(len(new_population)):
                new_population[i] = self.mutation(new_population[i])
            
            population = new_population
        
        # Retorna melhor solução
        final_fitness = np.array([
            self.fitness(ind, weights, values, capacity)
            for ind in population
        ])
        best_idx = np.argmax(final_fitness)
        return population[best_idx], final_fitness[best_idx]

    def plot_history(self):
        """Plota histórico de fitness"""
        plt.figure(figsize=(10, 6))
        plt.plot(self.best_fitness_history, label='Melhor Fitness')
        plt.plot(self.avg_fitness_history, label='Fitness Médio')
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.title('Evolução do Algoritmo Genético')
        plt.legend()
        plt.grid(True)
        plt.savefig('fitness_history.png')
        plt.close()

def main():
    # Exemplo de uso
    ga = GeneticAlgorithm(
        population_size=100,
        generations=50,
        mutation_rate=0.1,
        crossover_rate=0.8,
        elite_size=10
    )
    
    # Carrega dados
    weights, values, capacity = ga.load_data('data/knapsack_data.json')
    
    # Executa algoritmo
    best_solution, best_fitness = ga.evolve(weights, values, capacity)
    
    # Plota resultados
    ga.plot_history()
    
    # Salva resultados
    results = {
        'best_solution': best_solution.tolist(),
        'best_fitness': float(best_fitness),
        'total_weight': float(np.sum(best_solution * weights)),
        'selected_items': [i for i, x in enumerate(best_solution) if x == 1]
    }
    
    with open('results/genetic_algorithm_results.json', 'w') as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main() 