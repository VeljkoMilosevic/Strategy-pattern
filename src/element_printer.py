import matplotlib.pyplot as plt


def print_elements(data):
    plt.bar(range(len(data)), data, color='red', edgecolor='black')
    plt.title("Elements of array")
    plt.xlabel("Element index")
    plt.ylabel("Element value")
    plt.show()
