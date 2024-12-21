from abstract_sorting_algorithm import SortingAlgorithm


class SortingContext:
    def __init__(self):
        self.elements = []
        self.sorting_algorithm = None

    def set_elements(self, elements):
        self.elements = elements

    def set_sorting_algorithm(self, sorting_algorithm: SortingAlgorithm):
        self.sorting_algorithm = sorting_algorithm

    def sort(self):
        self.sorting_algorithm.sort(self.elements)
