import csv
from typing import List


class Node:
    def __repr__(self) -> str:
        return f"{{{self.name}:{self.f_cost}}}"

    def __str__(self) -> str:
        return self.__repr__()

    def __init__(self, name: str, f_cost: int = 0):
        self.name = name
        self.f_cost: int = f_cost

    def successors(self) -> List[str]:
        successors = []
        with open("cities.csv", newline='') as dataFile:
            reader = csv.DictReader(dataFile)
            for row in reader:
                if row["city1"] == self.name:
                    successors.append(row["city2"])
        return sorted(successors)

    def g(self, parent: str) -> int:
        distance = -1
        with open("cities.csv", newline='') as dataFile:
            reader = csv.DictReader(dataFile)
            for row in reader:
                if row["city1"] == self.name:
                    if row["city2"] == parent:
                        distance = int(row["distance"])
        return distance
