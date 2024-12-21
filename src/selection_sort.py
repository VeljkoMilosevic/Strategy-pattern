from abstract_sorting_algorithm import SortingAlgorithm
from element_printer import print_elements


class SelectionSorter(SortingAlgorithm):
    def sort(self, elements):
        print_elements(elements)
        for i in range(0, len(elements)):
            max_index = 0
            for j in range(0, len(elements)-i):
                if elements[j] > elements[max_index]:
                    max_index = j
            if elements[len(elements) - 1 - i] != elements[max_index]:
                elements[len(elements) - 1 - i], elements[max_index] = elements[max_index], elements[len(elements) - 1 - i]
                print_elements(elements)

