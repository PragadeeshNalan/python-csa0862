def find_sum_and_difference(elements, M, N):
    elements.sort(reverse=True)
    Mth_max = elements[M - 1]
    elements.sort()
    Nth_min = elements[N - 1]
    sum_result = Mth_max + Nth_min
    diff_result = abs(Mth_max - Nth_min)
    return Mth_max, Nth_min, sum_result, diff_result

elements = list(map(int, input("Enter the elements separated by space: ").split()))
max_length = len(elements)
print(f"Maximum length of M and N: {max_length}")

M = int(input(f"Enter the value of M (between 1 and {max_length}): "))
while M < 1 or M > max_length:
    M = int(input(f"Invalid Enter value of M (between 1 and {max_length}): "))

N = int(input(f"Enter the value of N (between 1 and {max_length}): "))
while N < 1 or N > max_length:
    N = int(input(f"Invalid Enter value of N (between 1 and {max_length}): "))

Mth_max, Nth_min, sum_result, diff_result = find_sum_and_difference(elements, M, N)
print(f"{M} Maximum Number = {Mth_max}")
print(f"{N} Minimum Number = {Nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {diff_result}")
