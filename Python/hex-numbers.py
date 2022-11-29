#This code written for solving https://quera.ir/problemset/277/
def hex_numbers(n):
    numbers = list(map(int,str(n)))
    new_numbers = []
    for number in numbers:
        if number > 1:
            new_numbers.append(str(1))
        else:
            new_numbers.append(str(number))
    return(int("".join(new_numbers), base=2))
if __name__ == "__main__":
    print(hex_numbers(int(input())))