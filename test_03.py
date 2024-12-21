def countBinarySubstrings(s: str) -> int:
    total = 0
    i = 0

    while i < len(s):
        count_0 = 0
        count_1 = 0

        if s[i] == "0":
            # count consective 0's first
            while i < len(s) and s[i] == "0":
                count_0 += 1
                i += 1

            j = i

            while j < len(s) and s[j] == "1":
                count_1 += 1
                j += 1

        elif s[i] == "1":
            # count consective 1's first
            while i < len(s) and s[i] == "1":
                count_1 += 1
                i += 1

            j = i

            while j < len(s) and s[j] == "0":
                count_0 += 1
                j += 1

        total += min(count_0, count_1)

    return total


def main() -> None:
    print(countBinarySubstrings("0001110010"))
    print(countBinarySubstrings("00110011"))


if __name__ == '__main__':
    main()

# countBinarySubstrings('00110011') => 6
