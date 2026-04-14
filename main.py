#задание выполнялось с использованием интернет-ресурсов
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def main():
    try:
        nums_input = input("Введите массив чисел через запятую: ")
        nums = list(map(int, nums_input.split(',')))
        target = int(input("Введите целевое значение (target): "))
        result = two_sum(nums, target)
        
        if result:
            print(f"{result}")
        else:
            print("Решение не найдено — нет двух чисел, дающих в сумме target")
            
    except ValueError:
        print("Ошибка! Пожалуйста, вводите только целые числа.")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

if __name__ == "__main__":
    main()
