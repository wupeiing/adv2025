from argparse import ArgumentParser

# def question_1(input_file):
#     total = 0
#     with open(input_file, "r") as file:
#         lines = file.read().splitlines()
#         for line in lines:
#             last_ind = len(line) - 1
#             num_map = {}
#             for i, v in enumerate(line):
#                 num_map[v] = i
#             for k, v in od.items(::-1):
#                 print(k, v)


#     print(total)

def question_1(input_file):
    total = 0  # sum of max joltages from all banks

    with open(input_file, "r") as file:
        lines = file.read().splitlines()

        for line in lines:
            line = line.strip()
            best = 0
            n = len(line)

            for i in range(n):
                for j in range(i + 1, n):
                    val = int(line[i]) * 10 + int(line[j])
                    if val > best:
                        best = val

            total += best  # ✅ add each bank's best result

    print(total)

def max_12_digit_joltage(line: str) -> int:
    stack = []
    remove = len(line) - 12  # number of digits we must remove

    for ch in line:
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    # If we still need to remove digits, trim from the end
    stack = stack[:12]

    return int("".join(stack))


def question_2(input_file):
    total = 0

    with open(input_file, "r") as file:
        lines = file.read().splitlines()

        for line in lines:
            line = line.strip()
            best = max_12_digit_joltage(line)
            total += best

    print(total)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--qid", type=str, required=True,
                        help="Question ID")
    parser.add_argument("--dry", type=str, required=False, default=False,
                        help="using sample input or not")
    args = parser.parse_args()
    if args.dry == "True":
        input_file = "./day3/input_sample.txt"
    else:
        input_file = "./day3/input.txt"
    if args.qid == "1":
        question_1(input_file)
    elif args.qid == "2":
        question_2(input_file)