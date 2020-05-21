def main():

    N = int(input())
    quantity_needed = list(map(int, input().split()))
    quantity_present = list(map(int, input().split()))
    max_count_per_ingredient = list()
    flag = 0
    # Check if for any ingredient quantity_present = 0 and quantity_needed != 0, 
    # so that result is 0
    for i in range(N):
        if quantity_present[i] == 0 and quantity_needed[i] != 0:
            result = 0
            flag = 1
    # Calculate max count of powerpuff girls made per ingredient
    if flag == 0:
        for i in range(N):
            if quantity_needed[i] == 0:
                max_count_per_ingredient.append(100000000)
            else:
                max_count_per_ingredient.append(quantity_present[i] // quantity_needed[i])
        result = min(max_count_per_ingredient)
    print(result)

main()
