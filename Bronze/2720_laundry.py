def main():
    # Q:0.25, D:0.1, N:0.05, P:0.01
    # 거스름 돈 항상 5$ under, 동전개수 최소
    
    T = int(input())
    C = [25, 10, 5, 1]
    
    for _ in range(T):
        c = int(input())
        t = [0, 0, 0, 0]
        for i in range(4):
            t[i] = c // C[i]
            c = c % C[i]
        print(" ".join(map(str, t)))

if __name__ == "__main__":
    main()