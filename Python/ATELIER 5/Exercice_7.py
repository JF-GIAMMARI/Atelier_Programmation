"""
Exercice 7 de l'atelier 5 : Les algorithmes de tri
file       = "Exercice_7.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from Exercice_2 import mix_list


def isSorted(list_to_check: list) -> bool:
    isSort = True
    for i in range(len(list_to_check) - 1):
        if list_to_check[i] > list_to_check[i + 1]:
            isSort = False
    return isSort


def stupid_sort(list_to_sort: list) -> list:
    """
    Sort the list with "Stupid sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """
    sorted_list = list_to_sort[:]
    is_sorted = isSorted(sorted_list)
    while not is_sorted:
        sorted_list = mix_list(sorted_list)
        is_sorted = isSorted(sorted_list)

    return sorted_list


def insertion_sort(list_to_sort: list) -> list:
    """
    Sort the list with "Insertion sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """
    sorted_list = list_to_sort[:]
    for i in range(len(sorted_list)):
        x = sorted_list[i]
        j = i
        while j > 0 and sorted_list[j - 1] > x:
            sorted_list[j] = sorted_list[j - 1]
            j = j - 1
        sorted_list[j] = x
    return sorted_list


def selection_sort(list_to_sort: list) -> list:
    """
    Sort the list with "Selection sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """
    sorted_list = list_to_sort[:]
    for i in range(len(sorted_list)):
        min = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min]:
                min = j
        if min != i:
            sorted_list[i], sorted_list[min] = sorted_list[min], sorted_list[i]

    return sorted_list


def bubble_sort(list_to_sort: list) -> list:
    """
    Sort the list with "Bubble sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """
    sorted_list = list_to_sort[:]
    length = len(sorted_list)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


def merge_sort(list_to_sort: list) -> list:
    """
    Sort the list with "Merge sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """
    sorted_list = list_to_sort[:]
    if len(sorted_list) <= 1:
        return sorted_list
    else:
        A = sorted_list[:len(sorted_list) // 2]
        B = sorted_list[len(sorted_list) // 2:]
        return merge_it(merge_sort(A), merge_sort(B))


def merge_it(A: list, B: list):
    """ Interativ algorythme for merge sorting
    :param A : List A
    :param B : List B
    """
    if not len(A) or not len(B):
        return A or B

    sorted_list = []
    i, j = 0, 0
    while len(sorted_list) < len(A) + len(B):
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i += 1
        else:
            sorted_list.append(B[j])
            j += 1
        if i == len(A) or j == len(B):
            sorted_list.extend(A[i:] or B[j:])
            break

    return sorted_list


def merge_rec(A: list, B: list):
    """ Recursiv algorythme for merge sorting
    :param A : List A
    :param B : List B
    """
    if not A:
        return B
    if not B:
        return A
    if A[0] < B[0]:
        return [A[0]] + merge_rec(A[1:], B)
    else:
        return [B[0]] + merge_rec(A, B[1:])


def radix_sort(list_to_sort: list) -> list: #Decrepeted
    """
    Sort the list with "Radix sort"
    :param list_to_sort: List to sort
    :return: Sorted list
    """

    sorted_list = list_to_sort[:]

    return sorted_list


def test_exercice7():
    """
    Test for exercice 7
    """
    to_sort = []
    for i in range(100):
        to_sort.append(i)
    to_sort = mix_list(to_sort)
    print("LIST ORIGINAL : ", to_sort)
    # print("Stupid sort : ", stupid_sort(to_sort))
    print("Insertion sort : ", insertion_sort(to_sort))
    print("Selection sort : ", selection_sort(to_sort))
    print("Bubble sort : ", bubble_sort(to_sort))
    print("Merge sort : ", merge_sort(to_sort))
    print("Radix sort : ", radix_sort(to_sort)) # Decrepeted


#test_exercice7()
