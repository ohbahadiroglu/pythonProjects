def hw3():
    cumulative_sum = 0
    n = int(input())
    x = int(input())
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    xnumerals=list()
    if x > 0:
        for i in range(x):
            xnumerals.append(int(input("Give a numeral: ")))
        xnumerals.reverse()
        ten_ex_digits=list()
        if n == 0 :
            cumulative_sum=0
        if n>=x:
            xnumerals= xnumerals * (n//x) + xnumerals[:n%x]
            for i in range(len(xnumerals)):
                ten_ex_digits.append(xnumerals[i]*10**i)
            count = len(ten_ex_digits)
            for num in ten_ex_digits:
                cumulative_sum += num * count
                count -= 1
        else:
            xnumerals=xnumerals[:n]
            for i in range(len(xnumerals)):
                ten_ex_digits.append(xnumerals[i]*10**i)
            count=len(ten_ex_digits)
            for num in ten_ex_digits:
                cumulative_sum += num * count
                count-=1
    else:
        cumulative_sum=0

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
    print(cumulative_sum)
    return cumulative_sum


if __name__ == "__main__":
    hw3()

