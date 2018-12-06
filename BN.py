# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

ALAMEDA CAMPUS
AI Project - Group 60
Rui Goncalves  - 69586
Maxwell Junior - 79457
      
"""
import itertools


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
        """ get the index of the prob requested """
        postProb_index = get_index_PostProb(evid)
        """ get the list of unknown prob"""
        unKnown_index_list = get_index_UnknownProb(evid)
        
        """  if there isnt a  post probability to compute  return the join prob of the evidence"""
        if postProb_index ==  -1 and unKnown_index_list == [] :
            return self.computeJointProb(evid)
    
        numb_unKnown_prob = len(unKnown_index_list)
        combo_list = get_n_combinations(numb_unKnown_prob)
        
        true_prob = 0.0
        false_prob = 0.0
        """ case the post_probability is True and False """
        for combo in combo_list:
       
           ev1 = new_evidence_method(1,evid,combo,unKnown_index_list,postProb_index)
           ev2 = new_evidence_method(0,evid,combo,unKnown_index_list,postProb_index)
           true_prob += self.computeJointProb(ev1)
           false_prob += self.computeJointProb(ev2)
           
           
        alfa =  1.0 / (true_prob + false_prob )
                
    
        return alfa * true_prob
    
    
    
    
        
    def computeJointProb(self, evid):
        result= 1.0
        print(evid)
        for index in range(len(self.nodes)) :
            
        #    print("Killmonger : ", self.nodes[index].computeProb(evid)[evid[index]])
            result  *=  self.nodes[index].computeProb(evid)[evid[index]]
            
        return result

""" get the index of the prob requested """
def get_index_PostProb(evid):
    index = -1
    for index in range(len(evid)):
        if evid[index] == -1:
            return index
        
""" get the index of prob that are unknown """
def get_index_UnknownProb(evid):
    unknown_index_list = []
    
    for index in range(len(evid)):
        if evid[index] == [] :
            unknown_index_list.append(index)
            
    return unknown_index_list
def  get_n_combinations( n):
    
      combo = list(itertools.product(range(2), repeat= n))

     # print(combo)
      return combo

def iterate_over(n):    
    my_list_elem = get_n_combinations(n)
    
    for el in my_list_elem :
        return el

def iterate_over_tuple(t_elem):
    for index in range(len(t_elem)):
        print(t_elem[index])


def new_evidence_method(post_case,evidencias, unknown, indexes, requested_prob):
    unknown = list(unknown)
    new_evidencias = list(evidencias)
    for index in range(len(unknown)) :
        new_evidencias[indexes[index]] = unknown[index]
    
    new_evidencias[requested_prob] = post_case
    
    return list(new_evidencias)