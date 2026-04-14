from two_sum import two_sum

# Список тестов
tests = [
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
    {"nums": [3, 3], "target": 6, "expected": [0, 1]},
    {"nums": [1, 2, 3], "target": 10, "expected": None},
    {"nums": [-1, -2, -3], "target": -6, "expected": None},
    {"nums": [], "target": 5, "expected": None},
    {"nums": [5], "target": 5, "expected": None}
]

all_passed = True
for i, test in enumerate(tests):
    result = two_sum(test["nums"], test["target"])
    if result == test["expected"]:
        print(f"Тест {i + 1}: ПРОЙДЕН")
    else:
        print(f"Тест {i + 1}: ОШИБКА")
        print(f"  Вход: nums={test['nums']}, target={test['target']}")
        print(f"  Ожидалось: {test['expected']}, получено: {result}")
        all_passed = False

if all_passed:
    print("\n Все тесты пройдены!")
else:
    print("\n Некоторые тесты не пройдены!")
