import sys
import math

input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

boonja = (a1 * b2) + (a2 * b1)
boonmo = b1 * b2

while math.gcd(boonja, boonmo) != 1:
    new_boonja = boonja // math.gcd(boonja, boonmo)
    new_boonmo = boonmo // math.gcd(boonja, boonmo)
    boonja = new_boonja
    boonmo = new_boonmo

print(boonja, boonmo)