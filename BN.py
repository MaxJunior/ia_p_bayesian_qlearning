# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        """ parents : holds the positions in the prob of the node parents"""
        self.parents = parents
        """ list of probability of each event in the network """
        self.prob = prob
    
        """ probability representation [ 1.0 - required_probability, required_probability] """
    def computeProb(self, evid):
        if self.parents == [] :
            return  [1.0 - self.prob[0], self.prob[0]]
       
    #    get the value(True oR False) of the parents nodes 
        post_list = [evid[index] for index in self.parents]
        if len(post_list) == 1 :
            requested_prob = self.prob[post_list[0]]
            return [1.0 - requested_prob,  requested_prob]

        # copy the array of probability
        probability_list = self.deep_copy(self.prob)      
        
        for index in range(len(post_list)):
            """ this is the value of the probability requested """
            if index  ==  len(post_list) - 1:
                 return [1.0 - probability_list[post_list[index]] , probability_list[post_list[index]]]
            """"  the next probability_list is the sublist of the current one depending on the value """
            probability_list = probability_list[post_list[index]]

    def deep_copy(self,matrix):
        """ copy a matrix """    
        return [line[:] for line in matrix]
    
            
    def prob_finder (self,lista, list_bool):
       print("My bool_list : ", list_bool)
       print("Prob_list  :", lista)
      
       for index in range(len(list_bool)):
         
         if(index < len(list_bool) - 1):
           #  print("index : ", index)
             lista = lista[list_bool[index]]
             print("My list : ",lista)
         else:
             print("list_bool val : ", list_bool[index])
             print("Probality requested : ", lista[list_bool[index]] )
             return lista[list_bool[index]]
             
    
class BN():
    def __init__(self, gra, prob):
        self.graph = gra
        self.nodes = prob # contem os nos

    def computePostProb(self, evid):
        pass
    
        return 0
        
        
    def computeJointProb(self, evid):
        result= 1.0
        print(evid)
        for index in range(len(self.nodes)) :
            
            print("Killmonger : ", self.nodes[index].computeProb(evid)[evid[index]])
            result  *=  self.nodes[index].computeProb(evid)[evid[index]]
            
        return result
        
        
        
