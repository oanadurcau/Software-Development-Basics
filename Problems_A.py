# Set A
import math


def prime(n):
    for div in range(2, int(math.sqrt(n)) + 1):
        if n % div == 0:
            return 0
    return n


# [1] Generați primul număr prim mai mare decât numărul natural dat n.


m = int(input("n="))

print("pb 1")
n = m

if n < 2:
    n = 2

while n:
    if prime(n) == 0:
        n += 1
    else:
        print(n)
        break

# [2] Pentru un număr natural n, determinați numerele prime p1 și p2 astfel încât n = p1 + p2 (conjectura lui Goldbach).

print("pb 2")
n = m
if n < 2 or n % 2 == 1:
    print("Goldbach's conjecture does not hold for n = {0} ".format(n))
else:
    for d in range(2, int(n / 2)):
        if prime(n - d) != 0 and prime(d) != 0:
            print(d, n - d)
            break

# [3] Pentru un număr natural dat, găsiți numărul minim m format cu aceleași cifre. De exemplu. n = 3658, m = 3568.

print("pb 3")
n = m
number_list = []
while n > 0:
    number_list.append(n % 10)
    n //= 10
number_list.sort()
print(number_list)
new_number = 0
cont = 0
ok = 0

for x in range(0, len(number_list)):
    if number_list[x] == 0:
        cont += 1
    else:
        if number_list[0] == 0 and number_list[x] != 0 and ok == 0:
            new_number = (new_number * 10 + number_list[x]) * 10 ** cont
            ok = 1
        else:
            new_number = new_number * 10 + number_list[x]
print(new_number)

# [4] Pentru un număr natural dat, găsiți cel mai mare număr natural scris cu aceleași cifre. De exemplu. n = 3658, m = 8653.

print("pb 4")
n = m
number_list = []
while n > 0:
    number_list.append(n % 10)
    n //= 10
number_list.sort(reverse=1)
print(number_list)

new_number = 0

for x in range(0, len(number_list)):
    new_number = new_number * 10 + number_list[x]
print(new_number)

# [5] Generați numărul prim mai mic decât numărul natural dat n. Dacă nu există un astfel de număr, trebuie afișat un mesaj.

print("pb 5")
n = m
n = n - 1
while n > 1:
    if prime(n) == 0:
        n -= 1
    else:
        print(n)
        break
if n == 1:
    print("This number does not exist")
