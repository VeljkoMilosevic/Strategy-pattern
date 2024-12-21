from abc import ABC

from abstract_sorting_algorithm import SortingAlgorithm
from element_printer import print_elements


class InsertionSort(SortingAlgorithm, ABC):
    def sort(self, elements):
        print_elements(elements)
        for i in range(1, len(elements)):
            curr_index = i
            j = i - 1
            while j >= 0 and elements[curr_index] < elements[j]:
                elements[j], elements[curr_index] = elements[curr_index], elements[j]
                j = j - 1
                curr_index = curr_index - 1
                print_elements(elements)
