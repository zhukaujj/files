from pprint import pprint


def create_cook_book(recipes):
    recipes_book = {}
    with open(recipes, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            number_of_ingridients = int(file.readline().strip())
            ingr_list = []
            for items in range(number_of_ingridients):
                ingr = {}
                line = file.readline().strip().split('|')
                ingr['ingredient_name'] = line[0]
                ingr['quantity'] = int(line[1])
                ingr['measure'] = line[2]
                ingr_list.append(ingr)
            recipes_book[dish_name] = ingr_list
            file.readline()
    return recipes_book


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridients in cook_book[dish]:
                ingridient, quantity, measure = ingridients
                if ingridients[ingridient] in shopping_list:
                    shopping_list[ingridients[ingridient]]['quantity'] += ingridients[quantity] * person_count
                else:
                    shopping_list[ingridients[ingridient]] = {'measure': ingridients[measure],
                                                              'quantity': ingridients[quantity] * person_count}
        else:
            print(f'Такого блюда "{dish}" нету в книге рецептов')
    return shopping_list


cook_book = create_cook_book('recipes.txt')
shopping = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(cook_book)
pprint(shopping)


