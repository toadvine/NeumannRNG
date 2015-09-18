__author__ = 'benjamin_sanchez'

def main():
    a_count = int(input)
    if a_count <= 0:
        return "error"
    num_list = [int(x) for x in input().split()]
    for x in num_list:
        neu_rng(x)

def neu_rng(i):
    i **= 2
    if len(str(i)) < 8:
        while len(str(i)) < 8:
            i = "0" + str(i)
    i = str(i)
    i =
main()
