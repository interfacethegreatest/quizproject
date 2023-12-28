import random
from globalVariables import *
from BrainGui import *
from Speciation import *
import copy

class CrossOver:
    
    
    def crossOver(self, parent1, populationBrain):
        for connections in populationBrain.connList:
           for parentConn in parent1.connList:
               if connections.innovation_ID == parentConn.innovation_ID:
                   connections.conn_Weight = parentConn.conn_Weight
    
    
    def splitParents(self, selected_parents, newTest, speciesSizes):
        count = 0
        for i in range(len(selected_parents)):
            brain1 = selected_parents[i][1][0][1]
            brain2 = selected_parents[i][1][1][1]
            speciesRange = selected_parents[i][0]
            population = newTest.outputs
            if selected_parents[i][1][0][0][1] > selected_parents[i][1][1][0][1]:
                parent1 = brain1
            else:
                parent1 = brain2
            try:
             for j in range(count, speciesRange+count):
                count+=1
                self.crossOver(parent1, population[j])
            except Exception:
                pass
            
    
    def __init__(self):
        self.gens = 0
        self.speciate = Speciate(5)
        self.test, self.species, self.zippedGroups = self.speciate.returnResult()
        self.temp_test = copy.copy(test)
        self.parameters = GlobalVariables(2, 1,0, 0)     
        self.zippedGroups = list(zip(zippedGroups, temp_test.outputs))
        #get two parents for each species,
        self.speciesParents = list()
        for key, value in self.species.items():
            #filter by looping through groups
            self.filteredBySpecies = [species for species in self.zippedGroups if species[0][0] == key]
            self.summedFitness = [fitness[0][1] for fitness in self.filteredBySpecies]
            self.weights = [value / sum(summedFitness) for value in self.summedFitness]
            self.selected_values = random.choices(self.filteredBySpecies, weights=self.weights, k = 2)
            self.speciesParents.append(selected_values)
        self.speciesParents = list(zip(species.values(), speciesParents))
        self.splitParents(speciesParents, test, species)
        self.speciate.compatibilityThreshold
            
    def __str__(self):
         f'Population : {len(speciesParents)}'
         f'Species : {len(species.items())}'
         f'Gens : {self.gens}'
         f'Comp Threshold = {self.speciate.compatibilityThreshold}'
            
            
            
            
def main():
    cr = CrossOver()

if __name__=="__main__": 
  outputs = main() 