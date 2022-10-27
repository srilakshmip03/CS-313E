def permute(a, idx):
    hi = len(a)
    #if we're at the end
    if idx == hi:
        if a == ["A", "B", "C", "D"]:
            print("")
        else:
            print(a)
    #swapping
    else:
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx + 1)
            a[idx], a[i] = a[i], a[idx]

def main():
    a = ["A", "B", "C", "D"]
    permute(a, 0)

main()