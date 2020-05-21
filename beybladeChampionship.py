def main():
    T = int(input())
    for testcase in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.sort(reverse=True)
        B.sort(reverse=True)
        i = 0
        j = 0
        ctr = 0
        while(i < len(A) and j < len(B)):
            while(B[j] >= A[i]):
                if j == len(B)-1:
                    break
                j += 1
            else:
                ctr += 1
            i += 1
            j += 1
        print(ctr)

main()
