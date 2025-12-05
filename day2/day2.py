from argparse import ArgumentParser


def get_magic_number(number):
    length = len(str(number))
    mid_len = 10**(length // 2)
    first_half = number // mid_len
    second_half = number % mid_len
    if first_half == second_half:
        print(number)
        return number
    return 0

def get_magic_number_2(number):
    number_str = str(number)
    length = len(number_str)
    mid = length // 2
    for i in range(mid+1):
        if i == 0:
            continue
        if number_str[:i] * (length // i) == number_str:
            print(number)
            return number
    return 0


def question_1():
    with open("./day2/input.txt", "r") as file:
        lines = file.read().split(",")
        count = 0
        for line in lines:
            target = line.split("-")
            start = int(target[0])
            end = int(target[1])
            for i in range(start, end + 1):
                count += get_magic_number(i)
    print(count)

def question_2():
    with open("./day2/input.txt", "r") as file:
        lines = file.read().split(",")
        count = 0
        for line in lines:
            target = line.split("-")
            start = int(target[0])
            end = int(target[1])
            for i in range(start, end + 1):
                count += get_magic_number_2(i)
    print(count)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--qid", type=str, required=True,
                        help="Question ID")
    args = parser.parse_args()
    if args.qid == "1":
        question_1()
    elif args.qid == "2":
        question_2()
