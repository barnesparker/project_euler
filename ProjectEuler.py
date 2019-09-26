import pdb
import math

### 10,0001 prime
# count = 1
# num = 3
# primes = []
# primes.append(2)
# def test_prime(num, p):
#     if num % p == 0:
#         return False
#     return True
#
# while (count != 10001):
#     for p in primes:
#         still_prime = test_prime(num, p)
#         if still_prime == False:
#             num += 1
#             break
#     else:
#         count += 1
#         print(str(count) + "    " + str(num))
#         primes.append(num)
#         num += 1



### Largest Product in a series
# big_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# start_index = 0
# end_index = 13
# biggest_prod = 1
# while end_index < len(big_num):
#     chunk = big_num[start_index:end_index:1]
#     product = 1
#     for digit in chunk:
#         product *= int(digit)
#     if product > biggest_prod:
#         biggest_prod = product
#     start_index += 1
#     end_index += 1
# print(biggest_prod)


### Special Pythagorean Triplet
# found = False
# for a in range(1, 1000):
#     for b in range(a, 1000):
#         for c in range(b, 1000):
#             if a + b + c == 1000:
#                 print(str(a) + " + " + str(b) + " + " + str(c) + " = 1000")
#                 if a ** 2 + b ** 2 == c ** 2:
#                     break
#         else:
#             continue
#         break
#     else:
#         continue
#     break
#
# print(a * b * c)

### Summation of Primes
# sum = 0
# n = 2000001
# primes = [True] * n
# for i in range(2, n):
#     if primes[i] == True:
#         sum += i
#         j = 2
#         while (i * j < n):
#             primes[i * j] = False
#             j += 1
# print(sum)


### Largest product in a grid

# grid = \
# [[8,2,22,97,38,15,00,40,00,75,4,5,7,78,52,12,50,77,91,8],
# [49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,00],
# [81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65],
# [52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91],
# [22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80],
# [24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50],
# [32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70],
# [67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21],
# [24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72],
# [21,36,23,9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95],
# [78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92],
# [16,39,5,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57],
# [86,56,00,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58],
# [19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40],
# [4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66],
# [88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69],
# [4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36],
# [20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16],
# [20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54],
# [1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]]

# largest = 1
# col = 0
# row = 0
# def compare_largest(num, largest):
#     if num > largest:
#         return num
#     return largest
# while row < len(grid):
#     col = 0
#     prod = 1
#     while col < len(grid[row]):
#         if col + 4 < 20:
#             for i in range(0, 4):
#                 prod *= grid[row][col + i]
#             largest = compare_largest(prod, largest)
#             prod = 1
#             if row + 4 < 20:
#                 for i in range(0, 4):
#                     prod *= grid[row + i][col + i]
#                 largest = compare_largest(prod, largest)
#                 prod = 1
#         if row + 4 < 20:
#             for i in range(0, 4):
#                 prod *= grid[row + i][col]
#             largest = compare_largest(prod, largest)
#             prod = 1
#             if col - 4 > 0:
#                 for i in range(0, 4):
#                     prod *= grid[row + i][col - i]
#                 largest = compare_largest(prod, largest)
#                 prod = 1
#         col += 1
#     row += 1
# print(largest)

### Highly divisible triangular number
# num_divisors = 1
# n = 2
# tri = 1
# def get_primes(n):
#     prime_nums = []
#     primes = [True] * n
#     for i in range(2, n):
#         if primes[i]:
#             prime_nums.append(i)
#             j = 2
#             while i * j < n:
#                 primes[i * j] = False
#                 j += 1
#
#     return prime_nums
#
# def factor(num, factors):
#     for prime in all_primes:
#         if prime > int(math.sqrt(num)):
#             return factors
#         if num % prime == 0:
#             factors.add(prime)
#             factors.add(num / prime)
#             factor(num / prime, factors)
# all_primes = get_primes(100000)
# while num_divisors < 500:
#     fs = set()
#     tri += n
#     n += 1
#     count = len(factor(tri, fs))
#     print(str(tri) + "  " + str(count) + "    Record: " + str(num_divisors))
#     if count > num_divisors:
#         num_divisors = count
#         print("new record!                          " + str(num_divisors))
#
# print(num_divisors)

### Longest Collatz Sequence
# def collatz(num, counter):
#     if num == 1:
#         return counter
#     if num % 2 == 0:
#         counter += 1
#         return collatz(num / 2, counter)
#     else:
#         counter += 1
#         return collatz(3 * num + 1, counter)
#
#
# biggest = 1
# biggest_chain = 1
# for num in range(1, 1000000):
#     chain = collatz(num, 1)
#     if chain > biggest_chain:
#         biggest = num
#         biggest_chain = chain
#     print(num)
# print(biggest)
# print(biggest_chain)

### Lattice Paths (UNSOLVED)
# dim = 15
# def find_path(x, y, count=0):
#     # print(str(x) + "   " + str(y))
#     if (x == dim and y == dim):
#         count += 1
#         return count
#     elif (x == dim):
#         return find_path(x, y + 1, count)
#     elif (y == dim):
#         return find_path(x + 1, y, count)
#     else:
#         count = find_path(x + 1, y, count)
#         return find_path(x, y + 1, count)
# print(find_path(1, 1))

### Power Digits
# num = str(2 ** 1000)
# sum = 0
# for digit in num:
#     sum += int(digit)
# print(sum)

### Number letter counts
ones = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
teens = {'0': 3, '1': 6, '2': 6, '3': 8, '4': 8, '5': 7, '6': 7, '8': 8, '9': 8}
tens = {'0': 0, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
def ones(num):
    return ones.get(num)
def tens(num):
    return tens.get(num)
total = 0
for number in range(1, 1001):
    num_str = str(number)
    if (number == 1000):
        total += 11
    if len(num_str) == 3:
        total += ones(num_str[0]) + 7
        if (num_str[1] != '0' and num_str[2] != '0'):
            total += 3
            if num_str[1]
        else:
            total +=






