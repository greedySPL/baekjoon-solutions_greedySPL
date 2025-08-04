def main():
    button = [300, 60, 10]
    T = int(input())
    result = [0, 0, 0]

    for i in range(3):
        result[i] = T // button[i]
        T = T % button[i]

    if T != 0:
        print("-1")
    else:
        print(" ".join(map(str,result)))

if __name__ == "__main__":
    main()