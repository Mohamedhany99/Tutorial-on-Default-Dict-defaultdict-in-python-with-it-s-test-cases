from collections import defaultdict

def answer():
    ## Write your solution here
    first, second = map(int, input().split())
    # print("n = ",n)
    # print("m = ",m)
    d = defaultdict(list)
    # constructing the dd
    for i in range(first):
        d[input()].append(i+1)
    # the logic for the solution
    for j in range(second):
        # check if the key exists in the dd
        keyy = input()
        if keyy in d:
            # result
            print(*d[keyy])
        else:
            # if key value is do not exist
            print(-1)
if __name__ == '__main__':
    answer()