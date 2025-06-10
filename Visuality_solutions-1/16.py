def multiply(x, y):
    if len(x[0]) != len(y):
        raise ValueError(
            f"Çarpım işlemi yapılamaz, çünkü 1. matrisin sütun "
            f"sayısı olan {x[0]}, ikinci matrisin satır sayısı "
            f"olan {len(y)} sayısına eşit değil."
        )
    return [
        [
            sum(x[i][k] * y[k][j] for k in range(len(x[0]))) 
            for j in range(len(y[0]))
        ] 
        for i in range(len(x))
    ]

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

b = [
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

c = multiply(a,b)
print(c)