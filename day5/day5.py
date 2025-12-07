from argparse import ArgumentParser

def question_1(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f]

    ranges = []
    ids = []
    reading_ranges = True

    for line in lines:
        if line == "":
            reading_ranges = False
            continue

        if reading_ranges:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            ids.append(int(line))

    fresh_count = 0

    for x in ids:
        for start, end in ranges:
            if start <= x <= end:
                fresh_count += 1
                break  # stop once it's confirmed fresh

    print(fresh_count)

def question_2(input_file):
    ranges = []

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:   # stop at the blank line
                break
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

    # Sort ranges by starting value
    ranges.sort()

    total_fresh = 0
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            # Overlapping or touching → merge
            cur_end = max(cur_end, end)
        else:
            # Disjoint → finalize previous range
            total_fresh += cur_end - cur_start + 1
            cur_start, cur_end = start, end

    # Add the final merged range
    total_fresh += cur_end - cur_start + 1

    print(total_fresh)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--qid", type=str, required=True,
                        help="Question ID")
    parser.add_argument("--dry", type=str, required=False, default=False,
                        help="using sample input or not")
    args = parser.parse_args()
    if args.dry == "True":
        input_file = "./day5/input_sample.txt"
    else:
        input_file = "./day5/input.txt"
    if args.qid == "1":
        question_1(input_file)
    elif args.qid == "2":
        question_2(input_file)