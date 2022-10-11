#!/usr/bin/env python3
# In our case heuristic represents the distance in straight line from any city to bycarest
from enum import Enum
from operator import attrgetter
import os
import sys
from typing import List, Tuple
from Node import Node, heuristic


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# The goal is to find the shortest path to Bucharest

class Result(Enum):
    SUCCESS = 1
    FAILURE = 2

def recursive_best_first_search(start: str):
    start_node = Node(start)
    start_node.f_cost = start_node.h()
    _, _, solution = RBFS(start_node, sys.maxsize)
    solution.reverse()
    print("")
    for city in solution:
        if city == "bucharest":
            print(city)
        else:
            print(f"{city} -> ", end='')
    return solution
    

count = 0

def RBFS(current_node: Node, f_limit: int) -> Tuple[Result, int, List[str]]:
    global count
    print(f"RBFS[{count}], f_limit: {f_limit}, node: {current_node}")
    count = count + 1
    if current_node.name == "bucharest":
        return Result.SUCCESS, current_node.f_cost, ["bucharest"]

    successors: List[Node] = []
    for succ in current_node.successors():
        succ_node = Node(succ)
        succ_node.dist_to_origin = current_node.dist_to_origin + \
            succ_node.get_distance_to(current_node.name)
        succ_node.f_cost = max(
            succ_node.g() + succ_node.h(), current_node.f_cost)
        successors.append(succ_node)

    print(f"\tsuccs: {successors}")
    if len(successors) == 0:
        return Result.FAILURE, sys.maxsize, []
    while True:
        successors.sort(key=attrgetter("f_cost"))
        best = min(successors, key=attrgetter("f_cost"))
        if best.f_cost > f_limit:
            return Result.FAILURE, best.f_cost, []
        alternative: int = sys.maxsize
        altname = "n/a"
        if len(successors) > 1:
            alternative, altname = successors[1].f_cost, successors[1].name
        print(f"\talternative: {{{altname}:{alternative}}}")
        print(f"best: {best}")
        result, best.f_cost, result_list = RBFS(
            best, min(f_limit, alternative))
        print(f"\tbest: {best}")
        if result != Result.FAILURE:
            result_list.append(current_node.name)
            return result, best.f_cost, result_list


def start():
    cls()
    print("Romanian City Problem using the RBFS\n")
    #print(f"Available start city\n -> {[key  for key in heuristic.keys()]}")
    start_city = input("Insert the start city: ")
    while not start_city in heuristic.keys():
        cls()
        print("The city you enterd is not valid, please try another one.\n")
        start_city = input("Insert the start city: ")
    if start_city == "bucharest":
        print("You are already at the goal!")
        return Result.SUCCESS
    return recursive_best_first_search(start_city)


def main():
    while start():
        ty = 1 if input("\n \t Do you want to try again? y/n:  ") == "y" else 0
        if not ty:
            return -1


###########################################################

if __name__ == '__main__':
    main()
