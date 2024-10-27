T=int(input())

wave=[1,1,1]

for i in range(3,100):
    wave.append(wave[i-3]+wave[i-2])

for _ in range(T):
    N=int(input())
    print(wave[N-1])