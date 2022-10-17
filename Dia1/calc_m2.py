#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 

#Crie uma função que retorne dois valores em uma tupla 
#contendo a quantidade de latas de tinta a serem compradas e o
#preço total a partir do tamanho de uma parede (em m²).

def calc_ink(area):
    cover, liter = 3, 18
    tin_price, coverage_area = 80.00, cover * liter
    qty_tins = round(area / coverage_area, 2)
    final_price = round(qty_tins * tin_price, 2)
    result = (qty_tins, final_price) 
    print(type(result), result)

    
calc_ink(54)
calc_ink(108)
calc_ink(60)
