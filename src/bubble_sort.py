from element_printer import print_elements
from abstract_sorting_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    def sort(self, elements):
        print_elements(elements)
        for i in range(0, len(elements)):
            for j in range(0, len(elements)-1-i):
                if elements[j] > elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]
                    print_elements(elements)
