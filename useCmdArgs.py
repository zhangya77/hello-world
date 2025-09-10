import sys


def main():
    if len(sys.argv) < 2:
        print("Error Please give a file path as an argv")
        print(f"Usage: {sys.argv[0]} /path/to/your/file")
        sys.exit(1)

    file_path = sys.argv[0]
    argv = sys.argv[1]
    print("Now run")
    print(f"The file path is {file_path}\nargv is {argv}")

    for i in range(1, 11):
        if i == 5:
            continue
        if i == 8:
            break
        print(i)
    print("\n" + "*" * 30 + "\n")

    i = 1
    while i <= 10:
        if i == 5:
            i += 1
            continue
        if i == 8:
            break
        print(i)
        i += 1


if __name__ == "__main__":
    print("call main")
    main()
