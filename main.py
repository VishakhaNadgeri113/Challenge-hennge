import sys
import functools

def process_case(x_str, y_str):
    try:
        x = int(x_str)
        y_parts = y_str.strip().split()
        if len(y_parts) != x:
            return "-1"
        y_numbers = list(map(int, y_parts))

        # Sum of 4th powers of non-positive numbers
        total = functools.reduce(
            lambda acc, val: acc + (val ** 4 if val <= 0 else 0),
            y_numbers,
            0
        )
        return str(total)
    except (ValueError, TypeError):
        return "-1"

def main():
    input_lines = sys.stdin.read().splitlines()

    try:
        n = int(input_lines[0])
    except (ValueError, IndexError):
        return

    results = []
    index = 1

    for _ in range(n):
        if index + 1 >= len(input_lines):
            results.append("-1")
            break
        x_line = input_lines[index]
        y_line = input_lines[index + 1]
        results.append(process_case(x_line, y_line))
        index += 2

    print('\n'.join(results))

if __name__ == "__main__":
    main()
