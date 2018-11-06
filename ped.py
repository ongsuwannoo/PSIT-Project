"""PedPonFire"""
import math
def main(num):
    """Find Same Number"""
    lis = []
    for _ in range(num):
        lis.append(int(input()))
    lis.sort()
    gas = int(input())
    med = lis.count(gas/2)
    if med <= 1:
        count = 0
    else:
        count = math.factorial(med)//(math.factorial(med-2)*math.factorial(2))
    for i in lis:
        if i >= gas/2:
            break
        count += lis.count(gas-i)*lis.count(i)
    print(count)

main(int(input()))
