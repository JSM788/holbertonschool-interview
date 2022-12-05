def pascal_triangle(n):
    fila = [1]
    cero = [0]
    array = []

    if n <= 0:
        return []
    for num in range(n):
        array.append(fila)

        fila = [i + d for i, d in zip(fila + cero, cero + fila)]

    return array
