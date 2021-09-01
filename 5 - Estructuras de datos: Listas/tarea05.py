
ron = ["botellas de ron"]*30
burger = ["hamburguesas"]*6
tomate = ["tomates"]*2
lista = []

shopping_list = ron + burger + tomate + ["pack de lonchas de queso", "bote de ketchup", "bote de mayonesa", "bote de mostaza"]

print(len(shopping_list))

for x in shopping_list:
    print(x)

for list in shopping_list:
    if list not in lista:
        lista.append(list)
        print(list, end=",")





