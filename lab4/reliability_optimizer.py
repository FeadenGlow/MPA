import itertools
from math import comb

# Паралельна надійність
def reliability_parallel(qs):
    r = 1.0
    for q in qs:
        r *= q
    return 1 - r

# Загальна надійність конфігурації
def total_reliability(groups, elements_data):
    result = 1.0
    for group in groups:
        qs = [elements_data[i][0] for i in group]  # Qкз
        result *= reliability_parallel(qs)
    return result

# Генерація розбиттів у групах
def generate_groupings(combo, structure):
    indices = list(combo)
    all_partitions = []

    for g1 in itertools.combinations(indices, structure[0]):
        rest1 = list(set(indices) - set(g1))
        for g2 in itertools.combinations(rest1, structure[1]):
            rest2 = list(set(rest1) - set(g2))
            g3 = tuple(rest2)
            all_partitions.append((g1, g2, g3))

    return all_partitions

# Зчитування вхідного файлу
def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    structure = list(map(int, lines[0].split()))
    k = int(lines[1])
    elements_data = {}
    for line in lines[2:2 + k]:
        parts = line.strip().split()
        idx = int(parts[0])
        qkz = float(parts[1])
        qoz = float(parts[2])
        elements_data[idx] = (qkz, qoz)
    return structure, elements_data

# Основна функція
def find_best(filename):
    structure, elements_data = read_input(filename)
    total = sum(structure)
    all_ids = list(elements_data.keys())

    best_rel = 0.0
    best_config = None
    total_configs = 0

    for combo in itertools.combinations(all_ids, total):
        partitions = generate_groupings(combo, structure)
        for groups in partitions:
            rel = total_reliability(groups, elements_data)
            total_configs += 1
            if rel > best_rel:
                best_rel = rel
                best_config = groups

    print("Задана структура:", *structure)
    print("Кількість різнотипних елементів:", len(elements_data))
    print("Кількість різних конфігурацій:", total_configs)
    print("Максимальна надійність:", round(best_rel, 8))
    print("Досягнута на конфігурації:")
    for group in best_config:
        print(*group)

    with open("output.txt", "w") as f:
        f.write(f"Задана структура: {' '.join(map(str, structure))}\n")
        f.write(f"Кількість різнотипних елементів: {len(elements_data)}\n")
        f.write(f"Кількість різних конфігурацій: {total_configs}\n")
        f.write(f"Максимальна надійність: {round(best_rel, 8)}\n")
        f.write("Досягнута на конфігурації:\n")
        for group in best_config:
            f.write(' '.join(map(str, group)) + '\n')

find_best("input.txt")

