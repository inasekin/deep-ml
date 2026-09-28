import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    if degree < 0:
        return []
        
    result = []
    for x in data:
        row = [float(x ** d) for d in range(degree + 1)]
        result.append(row)
        
    return result