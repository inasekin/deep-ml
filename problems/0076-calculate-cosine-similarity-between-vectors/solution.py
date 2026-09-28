import math

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        v1 (list/tuple): 1D array representing the first vector.
        v2 (list/tuple): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    dot_product = sum(a * b for a, b in zip(v1, v2))

    magnitude_v1 = math.sqrt(sum(a ** 2 for a in v1))
    magnitude_v2 = math.sqrt(sum(b ** 2 for b in v2))

    return dot_product / (magnitude_v1 * magnitude_v2)
