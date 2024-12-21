from sorting_context import SortingContext
from insertion_sort import InsertionSort

context = SortingContext()
elements = [5, 4, 3, 2, 1]
context.set_sorting_algorithm(InsertionSort())
context.set_elements(elements)
context.sort()
