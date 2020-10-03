"""
Exercice 8 de l'atelier 5 : Visualiser les algorithmes de tri
file       = "Exercice_8.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

import matplotlib.pyplot as plt
from random import *
import time
from Exercice_7 import *


def perf_test(all_func: list, tailles_list_test: list, nbr_run: int) -> tuple:
    """
    Compares two mixing functions with multiple list sizes
    :param all_func: List of function to comapre
    :param tailles_list_test: All list length to test
    :param nbr_run: Number of tests per list per function
    :return: Tuples of list with all average time per size and per function
    """

    stat_func = []  # List of list of run time per function and per list length
    func_name = []  # List of function name

    for i in range(len(all_func)):  # Fill list by default
        stat_func.append([])
        func_name.append(all_func[i].__name__)

    for e in tailles_list_test:
        times_func = []
        turn_list = []

        for i in range(e):  # Generate list with the e lentgh
            turn_list.append(i)
        shuffle(turn_list)  # Mix the list

        for f in range(len(all_func)):  # For all functions
            for i in range(nbr_run):  # Test for x run
                start = time.perf_counter()
                all_func[f](turn_list)
                end = time.perf_counter()
                times_func.append(end - start)
            stat_func[f].append(sum(times_func) / nbr_run)  # Add the average to stat
            times_func = []

    return stat_func, func_name, tailles_list_test


def draw_chart(data: list, title: str):
    """
    Drawing list in a chart
    :param data: Data, Name, Scale
    :param title: Fig title
    :return: None

    """
    label = data[1]
    axis = data[0]
    scale = data[2]
    fig, ax = plt.subplots()
    for i in range(len(axis)):
        ax.plot(scale, axis[i], label=label[i])
    ax.set(xlabel='Nombre de valeur', ylabel='Temps (s)', title=title)
    ax.legend(loc='best', shadow=True, fontsize='x-large')
    plt.show()


length_list = [10, 100, 200, 300, 400, 500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000]
function_to_test = [insertion_sort, selection_sort, bubble_sort, merge_sort,radix_sort, sorted] # radix_sort decrepeted
draw_chart(perf_test(function_to_test, length_list, 10), "Comparatif des fonctions de tri")
