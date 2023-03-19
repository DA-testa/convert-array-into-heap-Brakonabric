# python3


def buildHeap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        minHeap(data, n, i, swaps)
    return swaps

def minHeap(data, n, i, swaps):
    lSide = 2 * i + 1
    rSide = 2 * i + 2
    min = i

    if lSide <= n - 1 and data[lSide] < data[min]:
        min = lSide
    if rSide <= n - 1 and data[rSide] < data[min]:
        min = rSide
    if i != min:
        data[i], data[min] = data[min], data[i]
        swaps.append((i, min))
        minHeap(data, n, min, swaps)

    


def main():
    print("[!] \tUse an input to choose files or input - F or I ?")
    textInput = input(">:: \t").upper()
    if "F" in textInput:
        print("[!] \tEnter file name or file path. For example '0'.")
        fileName = "tests/" + input(">:: \t")
        if 'a' in fileName:
            print("[Err]: \tForbidden name")
            return   
        file = open(fileName, "r")

        n = int(file.readline())
        data = list(map(int, file.readline().split()))
        assert len(data) == n
        swaps = buildHeap(data)

    elif "I" in textInput:
        print("[!] \tEnter text below.")
        n = int(input(">:: \t"))
        data = list(map(int, input(">:: \t").split()))
        assert len(data) == n
        swaps = buildHeap(data)
    else:
        print("[Err]:\tWrong input")
    pass

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
