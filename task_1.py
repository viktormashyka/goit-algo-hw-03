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

import shutil
from pathlib import Path

def parse_folder(source_path, dest_path):
    try:
        for element in source_path.iterdir():
            if element.is_dir():
                # Якщо елемент є папкою, викликаємо функцію рекурсивно
                parse_folder(element, dest_path)
            elif element.is_file():
                # Сортуємо файли за розширеннями
                file_extension = element.suffix[1:]  # отримуємо розширення файлу без крапки
                new_dir = dest_path / file_extension
                # print(f"Parse folder: This is file - {element.name}")
                # yield element
                if not new_dir.exists():
                    new_dir.mkdir(parents=True, exist_ok=True)
                # Копіюємо файл у нову директорію
                shutil.copy2(element, new_dir / element.name)
                print(f"Файл {element.name} скопійовано до {new_dir}")
    except Exception as e:
        print(f"Помилка під час обробки: {e}")

def main():
    while True:
        user_input = input("Введіть шлях: ")
        args = user_input.lower().split()

        if len(args) < 1:
            print("Будь ласка, введіть шлях до вихідної директорії.")
            continue

        # source_path = Path(sys.argv[1])
        source_path = Path(args[0])

        # Встановлюємо директорію призначення, за замовчуванням - 'dist'
        # dest_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')
        dest_path = Path(args[1]) if len(args) > 1 else Path('dist')

        if not source_path.exists() or not source_path.is_dir():
            print("Вказаний шлях до вихідної директорії неправильний або не існує.")
            # sys.exit(1)
            continue
        if not dest_path.exists():
            dest_path.mkdir(parents=True, exist_ok=True)

        # Рекурсивно обробляємо вихідну директорію
        parse_folder(source_path, dest_path)
        print("Копіювання завершено.")

        action = input("Введіть 'q' для виходу або будь-яку клавішу для продовження: ")
        if action == 'q':
            print("Програма завершена.")
            break
        else:
            continue

if __name__ == "__main__":
    main()