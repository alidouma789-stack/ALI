def trouver_maximum(liste):
    max_val = liste[0]
    for nombre in liste:
        if nombre > max_val:
            max_val = nombre
    return max_valb  