# Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії 
# та сортує в піддиректорії, назви яких базуються на розширенні файлів.

# Також візьміть до уваги наступні умови:
# 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях 
# до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
# 2. Рекурсивне читання директорій:
# Має бути написана функція, яка приймає шлях до директорії як аргумент.
# Функція має перебирати всі елементи у директорії.
# Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
# Якщо елемент є файлом, він має бути доступним для копіювання.
# 3. Копіювання файлів:
# Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
# Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

import os
from pathlib import Path

if not os.path.exists('dist'):
    os.mkdir('dist')
def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")
            yield element

def move_file(file_path, new_path='dist'):
    new_path = Path(new_path)
    if not new_path.exists():
        new_path.mkdir(parents=True, exist_ok=True)
    for file in file_path:
        destination = new_path / file.name
        print(f"Move file: Moving {file} to {destination}")
        file.rename(destination)

if __name__ == "__main__":
    while True:
        user_input = input("Введіть шлях: ")
        args = user_input.lower().split()
        if len(args) < 1:
            print("Введіть шлях до вихідної директорії та шлях до директорії призначення.")
            continue
        parent_folder_path = Path(args[0])
        if not parent_folder_path.exists():
            print("Введіть існуючий шлях.")
            continue
        new_path = Path(args[1]) if len(args) > 1 else Path('dist')
        file = parse_folder(parent_folder_path)
        move_file(file, new_path)
        
        action = input("Введіть 'q' для виходу або будь-яку клавішу для продовження: ")
        if action == 'q':
            print("Програма завершена.")
            break
        else:
            continue