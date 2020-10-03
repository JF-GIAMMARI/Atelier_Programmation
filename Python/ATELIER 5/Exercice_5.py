"""
Exercice 5 de l'atelier 5 : Mesure & comparaison des temps d'exécution
file       = "Exercice_5.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""

from Exercice_2 import mix_list
from Exercice_4 import extract_elements_list
import matplotlib.pyplot as plt
from random import *
import time


def perf_test(all_func: list, len_list: list, moy_exec: int, extract: bool = False) -> tuple:
    """
    Compares two mixing functions with multiple list sizes
    :param extract: Define if is extract test or not
    :param all_func: List of function to comapre
    :param len_list: All list length to test
    :param moy_exec: Number of tests per list per function
    :return: Tuples of list with all average time per size and per function
    """

    stat_func = []
    func_name = []

    for i in range(len(all_func)):
        stat_func.append([])
        func_name.append(all_func[i].__name__)

    for e in len_list:
        time_func = []
        turn_list = []

        for i in range(e):  # Generate list with the e lentgh
            turn_list.append(i)
        shuffle(turn_list)  # Mix the list
        for f in range(len(all_func)):  # For all functions
            for i in range(moy_exec):  # Test for x run
                if extract:
                    int_extract = int(len(turn_list) / 2)  # Define extract number 1/2 Length
                    start = time.perf_counter()
                    all_func[f](turn_list, int_extract)
                    end = time.perf_counter()
                    time_func.append(end - start)
                else:
                    start = time.perf_counter()
                    all_func[f](turn_list)
                    end = time.perf_counter()
                    time_func.append(end - start)
            stat_func[f].append(sum(time_func) / len(time_func))  # Add the average to stat
            time_func = []

    return stat_func, func_name, len_list


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
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


length_list = [10, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
try_ex = 300
draw_chart(perf_test([mix_list, shuffle], length_list, try_ex), "Comparatif des fonctions de mixage")
draw_chart(perf_test([extract_elements_list, sample], length_list, try_ex, True),
           "Comparatif des fonctions d'extraction")
