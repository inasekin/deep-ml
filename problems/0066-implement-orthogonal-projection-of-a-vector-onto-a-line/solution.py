
def orthogonal_projection(v, L):
    dot_v_L = 0
    dot_L_L = 0
    result = []
    
    i = 0

    while i < len(v):
        dot_v_L += v[i] * L[i]
        dot_L_L += L[i] * L[i]
        i += 1

    k = dot_v_L / dot_L_L

    i = 0
    while i < len(L):
        val = round(L[i] * k, 3)
        result.append(val)
        i += 1
        
    return result
