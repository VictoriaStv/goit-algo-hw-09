import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def print_result(amount, coins_dict):
    print(f"Сума: {amount}")
    print("Монети:")
    for coin, count in sorted(coins_dict.items(), reverse=True):
        print(f"  Номінал {coin}: {count} шт.")
    print()

# Тест
if __name__ == "__main__":
    amount = 113
    num_tests = 100  # Кількість тестів
    total_time = 0
    
    for _ in range(num_tests):
        start_time = time.time()
        greedy_result = find_coins_greedy(amount)
        execution_time = time.time() - start_time
        total_time += execution_time
    
    average_time = total_time / num_tests
    print("Жадібний алгоритм:")
    print_result(amount, greedy_result)
    print(f"Середній час виконання: {average_time:.100f} секунд")
