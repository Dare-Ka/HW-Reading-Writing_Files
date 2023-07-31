import os.path
import os
cook_book = {}
with open("recipes.txt", 'rt', encoding='utf-8') as recipes:
    for line in recipes:
        if line == '\n':
            continue
        else:
            line = line.strip()
            if not line.isdigit():
                dish_name = line
                cook_book.setdefault(dish_name, [])
            else:
                for i in range(int(line)):
                    ingredients = recipes.readline().strip().split(' | ')
                    cook_book[dish_name].append({'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]})
print(cook_book)

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r',encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


file_for_writing = os.path.abspath('\Users\1395329\Desktop\«Открытие и чтение файла, запись в файл»\Новая папка')
base_path = os.getcwd()
location = os.path.abspath('\Users\1395329\Desktop\«Открытие и чтение файла, запись в файл»\Новая папка')
rewriting(file_for_writing, base_path, location)
    
