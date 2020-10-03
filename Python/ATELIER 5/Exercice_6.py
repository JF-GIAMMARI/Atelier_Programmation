"""
Exercice 6 de l'atelier 5 : Tri à votre mode
file       = "Exercice_6.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

import matplotlib.pyplot as plt
from random import *
import time


def sort_list(list_to_sort: list) -> list:
    """
    Sorting with bubble sort a list
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


def perf_test(all_func: list, tailles_list_test: list, nbr_run: int, conf: int = 0) -> list:
    """
    Compares two mixing functions with multiple list sizes
    :param all_func: List of function to comapre
    :param tailles_list_test: All list length to test
    :param nbr_run: Number of tests per list per function
    :param conf : Config (1 -> Standar, 2 -> Pre-Sorted list, 3 -> Pre Sorted Inverse list)
    :return: Tuples of list with all average time per size and per function
    """

    stat_func = []  # List of list of run time per function and per list length

    for i in range(len(all_func)):
        stat_func.append([])

    for e in tailles_list_test:
        times_func = []
        turn_list = []

        if conf == 0 or conf == 2:
            for i in range(e):  # Generate list with the e lentgh
                turn_list.append(i)
        if conf == 1:
            for i in range(e, 0, -1):  # Generate list with the e lentgh
                turn_list.append(i)
        if conf == 2:
            shuffle(turn_list)  # Mix the list

        for f in range(len(all_func)):  # For all functions
            for i in range(nbr_run):  # Test for x run
                start = time.perf_counter()
                all_func[f](turn_list)
                end = time.perf_counter()
                times_func.append(end - start)
            stat_func[f].append(sum(times_func) / nbr_run)  # Add the average to stat
            times_func = []

    return stat_func


def draw_chart(axis: list, label: list, title: str, scale: list):
    """
    Drawing list in a chart
    :param axis: Data x axis
    :param label: Name of data
    :param scale: Scale of data
    :param title: Fig title
    :return: None
    """

    fig, ax = plt.subplots()
    for i in range(len(axis)):
        ax.plot(scale, axis[i], label=label[i])
    ax.set(xlabel='Nombre de valeur', ylabel='Temps (s)', title=title)
    ax.legend(loc='best', shadow=True, fontsize='x-large')
    plt.show()


length_list = [250, 500]
sort_global = perf_test([sort_list, sorted], length_list, 100)
sort_global += perf_test([sort_list, sorted], length_list, 100, 1)  # Tableau deja trier
sort_global += perf_test([sort_list, sorted], length_list, 100, 2)  # Tableau tirer inversement
draw_chart(sort_global,["sort_list  (1)", "sorted (1)", "sort_list > (2)", "sorted > (2)", "sort_list < (3)", "sorted < (3)"],
           "Comparatif des fonctions de tri", length_list)
