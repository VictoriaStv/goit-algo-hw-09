import time

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_used[x] = coin

    result = {}
    while amount > 0:
        coin = last_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

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
        dp_result = find_min_coins(amount)
        execution_time = time.time() - start_time
        total_time += execution_time
    
    average_time = total_time / num_tests
    print("Алгоритм динамічного програмування:")
    print_result(amount, dp_result)
    print(f"Середній час виконання: {average_time:.100f} секунд")
