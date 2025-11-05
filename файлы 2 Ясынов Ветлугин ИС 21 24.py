with open('список.txt', 'r', encoding='utf-8') as f:
    for номер, строка in enumerate(f):
        print(f"Строка {номер + 1}: {строка.strip()}")