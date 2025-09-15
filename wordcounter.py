import re
from collections import Counter

def count_words(filename):
    word_count = Counter()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                word_count.update(words)
    except FileNotFoundError:
        print(f"Error File:'{filename}' not found")
        return {}
    except Exception as e:
        print(f"Read file error:{e}")
        return {}

    return dict(word_count)

if __name__ == "__main__":
    test_content = """
    Hello world! This is a test file.
    Hello again, this is only a test.
    Testing, testing, 1, 2, 3. 2.
    """

    with open("test_content.txt", "w") as f:
        f.write(test_content)

    print("*" * 20)
    result=count_words("test_content.txt")
    for word,count in sorted(result.items()):
        print(f"{word}:{count}")
    try:
        with open("test_content.txt", "r") as f:
            f.readline()
    except FileNotFoundError:
        print(f"File not found")





