__author__ = 'benjamin_sanchez'


def main():
    a_count = int(input())
    if a_count <= 0:
        return "error"
    num_list = [int(x) for x in input().split()]
    for x in num_list:
        print(neu_rng(x), end=" ")


def neu_rng(i):
    init_num = i
    counter = 0
    done = False
    holder = list()
    while not done:
        i **= 2
        if len(str(i)) < 8:
            while len(str(i)) < 8:
                i = int("0" + str(i))
        if int(str(i)[2:6]) in holder:
            done = True
        else:
            holder.append(i)
            i = int(str(i)[2:6])
        counter += 1
    return counter

main()
