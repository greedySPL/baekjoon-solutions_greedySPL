def main():
    N = int(input()) # 사람 수
    P = list(map(int, input().split())) # 돈을 인출하는데 걸리는 시간
    P.sort()
    t = 0
    x = 0
    
    for i in range(len(P)):
        t = t + P[i]
        x = x + t
        
    print(x)

main()