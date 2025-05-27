def probability(n, k, letters):
    if len(letters) != n:
        print("You have exceeded or not met the n limit")
        return

    if k > n:
        print("Choose limit exceeded")
        return

    # Function to generate combinations manually
    def generate_combinations(arr, k):
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return result

    total_combinations = generate_combinations(letters, k)
    count_with_a = [combo for combo in total_combinations if 'a' in combo]

    probability_value = len(count_with_a) / len(total_combinations)
    print(f"{probability_value:.4f}")


# Usage
n = int(input())
letters = input().split()
k = int(input())
probability(n, k, letters)
