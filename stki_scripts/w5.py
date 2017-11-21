"""
author rochanaph
September 21 2017
"""
import math
def euclidean(vector1, vector2):
    """
    fungsi untuk menghitung jarak antara 2 vektor dengan rumus euclidean ddistance
    :param vector1: vektor 1
    :param vector2: vektor
    :return:
    """
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist

def cosine(vector1, vector2):
    """
    :param vector1:
    :param vector2:
    :return:
    """

    dot  = sum([a*b for a,b in zip(vector1, vector2)])
    mag1 = math.sqrt(sum([a**2 for a in vector1]))
    mag2 = math.sqrt(sum([a**2 for a in vector2]))

    return round(dot/(mag1*mag2),4)*100
