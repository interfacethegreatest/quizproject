 # -*- coding: utf-8 -*-

import random
from globalVariables import *
from BrainGui import *

class Speciate:
    '''
    ''' 
    
    
    
    def __str__(self):
        pass
        
        
    
    def getCompareDifferenceCD(self, brainA, brainB):
        c1 = 1.0
        c2 = 1.0
        c3 = 0.4
        e = self.getExcessGenesE(brainA, brainB)
        d = self.getDisjointGenesD(brainA, brainB)
        w = self.getWeightAverageW(brainA, brainB)
        n = self.getLargestNetworkN(brainA, brainB)
        return ((e*c1)/n) + ((d*c2)/n) + (w*c3)
    
    
    
    def getLargestNetworkN(self, brainA, brainB):
     conLengthA = sum(1 for connection in brainA.connList if connection.ennabled)
     conLengthB = sum(1 for connection in brainB.connList if connection.ennabled)

     return max(conLengthA, conLengthB)

    
    def getWeightAverageW(self, brainA, brainB):
     innovation_weightsA = {connection.innovation_ID: connection.conn_Weight for connection in brainA.connList if connection.ennabled}
     innovation_weightsB = {connection.innovation_ID: connection.conn_Weight for connection in brainB.connList if connection.ennabled}

     total_weight = 0.0
     matching_count = 0

     for innovation_ID in innovation_weightsA:
        if innovation_ID in innovation_weightsB:
            total_weight += abs(innovation_weightsA[innovation_ID] - innovation_weightsB[innovation_ID])
            matching_count += 1

    # Avoid division by zero
     return total_weight / matching_count if matching_count > 0 else 0.0
      
        
    def getExcessGenesE(self, brainA, brainB):
        '''
        NEEDS TO BE TESTED ON LARGER NETWORKS
        Parameters
        ----------
        bNetA : Brain
            An object of type Brain stores in globalVariables.py.
        bNetB : TYPE
            DESCRIPTION.

        Returns
        -------
        The number of excess genes in bNetB that do not exist in bNetA.

        '''
        """Get the excess genes (Innovation IDs) in genome2 that do not exist in genome1."""
        """Excess genes are those outside the range of netA , """
        """first find the range of net A,"""
        """initialise obj holders"""
        lowerRangeID = None
        upperRangeID = None
        e = 0
        """ return list[obj0] and list[len(list)-1], i.e. upper and lower ranges"""
        lowerRangeID = brainA.connList[0]
        upperRangeID = brainA.connList[len(brainA.connList)-1]
        """ loop through brainB, if any list[i].innovation_ID is less than lowerRangeID or,
        greater than upperRangeID, increment e number by 1,"""
        for i in range(len(brainB.connList)):
            store = brainB.connList[i]
            if (brainB.connList[i].innovation_ID < lowerRangeID.innovation_ID or brainB.connList[i].innovation_ID > upperRangeID.innovation_ID) and (brainB.connList[i].ennabled):
              e+=1  
        return e
        
    def getDisjointGenesD(self, brainA, brainB):
        '''
        NEEDS TO BE TESTED ON LARGER NETWORKS
        '''
        
        def extract_innovation_ids(connections_list):
         '''
         Parameters
         ----------
         connections_list : List
             Lists all connections contained within the brain NN object.

         Returns
         -------
         innovation_ids : TYPE
             allows for checking of disjoint genes in list_a/b.

         '''
         innovation_ids = {conn.innovation_ID for conn in connections_list if conn.ennabled}
         return innovation_ids

        list_a = extract_innovation_ids(brainA.connList)
        list_b = extract_innovation_ids(brainB.connList)

        d = 0  # Counter for disjoint genes

         # Check for disjoint genes in list_a
        for gene_id in list_a:
          if gene_id not in list_b:
            d += 1

         # Check for disjoint genes in list_b
        for gene_id in list_b:
          if gene_id not in list_a:
            d += 1

        return d
 
 
    def speciateGen0(self, population):
        
        def recurrentSpeciate(grouping, species):
            while 0 in species.values():
                grouping +=1
                speciesNil = {key:value for key, value in species.items() if value == 0 }
                randomInd = random.choice(list(speciesNil.items()))
                species.pop(randomInd[0])
                randomInd = (randomInd[0], grouping)
                for key,value in species.items():
                        if self.getCompareDifferenceCD(randomInd[0], key) < self.compatibilityThreshold and value == 0:
                                species[key] = grouping
                        else: 
                                pass
                species.update({randomInd[0]:randomInd[1]})
                recurrentSpeciate(grouping, species)
        
        species = dict()
        grouping = 0
        species = {individual: grouping for individual in population}
        recurrentSpeciate(grouping, species)
        return species
        
    def getOffSpring(self, dictionary = dict, species = list):
         # Use set to get unique values
         unique_values = set(dictionary.values())

         # Initialize a dictionary to store the count of each unique value
         value_counts = {value: 0 for value in unique_values}

         # Count occurrences of each unique value
         for value in dictionary.values():
          value_counts[value] += 1
         #Zip together the species groups with the fitness values
         zippedFitnessGroup = list(zip(dictionary.values(), species))
         #obtain the Fa value for reach fitness
         for key, value in value_counts.items():
             #loop through the count of each group,
             for i in range(len(zippedFitnessGroup)):
              if key == zippedFitnessGroup[i][0]:
                  #if the zipped group is equal to the counted group,
                  fa = zippedFitnessGroup[i][1]/value
                  #divide the fitness by the count to obtain the fa, append to the tuple,
                  zippedFitnessGroup[i]= (zippedFitnessGroup[i][0], zippedFitnessGroup[i][1], fa )
        
        # generate the sum total average
         newFitness = list()  
         #loop through the group / frequency dict,
         for key,value in value_counts.items():
             #create a variable to sum up grouped fa values,
             nAvgFa = 0
             #loop through the zipped fitness and group values,
             for i in range(len(zippedFitnessGroup)):
                 #if the group / frequency dict group matches the tuple group, sum the value into the 
                 if key == zippedFitnessGroup[i][0]:
                     nAvgFa += zippedFitnessGroup[i][2]
            #Once all the Fa values are summed, divide by the value, ie             
             nAvgFa = nAvgFa / value 
             newFitness.append(nAvgFa)
         gloAvgCount = 0    
         #get global average 
         for i in range(len(zippedFitnessGroup)):
             gloAvgCount += zippedFitnessGroup[i][2]
         gloAvgCount = gloAvgCount / len(zippedFitnessGroup)
             
         #allowed offspring = newAvgFofA / GlobalAverage
         #create a new dictionary to store new offspring,
         offspring = dict()
         for key,value in value_counts.items():
             offspring.update({key: round(newFitness[key-1] / gloAvgCount *value)})
             
         
         
         
         # count the length of value counts,
         #store the value in an object
         #loop though each j of the fitness , dividing the corresponding
         return offspring, zippedFitnessGroup
        
    
    def returnResult(self):
        return self.test, self.offspring_Categories, self.zippedGroups
                
    def __init__(self, speciesTargetSize):
     self.parameters = GlobalVariables(2, 1, 0, 0)
     self.test = Run_Test(self.parameters, population_size=50)
     self.compatibilityThreshold = 2.0
     self.offspring_Categories, self.zippedGroups = self.getOffSpring(self.speciateGen0(self.test.outputs), self.test.fitness)
     self.populationSize = len(self.zippedGroups)
     self.speciesTarget = speciesTargetSize
     self.gens = 1
     
     self.speciesSize = len(self.offspring_Categories)

     

def main():
    speciate = Speciate(5)

if __name__=="__main__": 
  outputs = main() 