import re
from collections import defaultdict

def count_words(filename):
    word_count = defaultdict(int)

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_count[word] += 1
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
    Testing, testing, 1, 2, 3.
    """

    with open("test_content.txt", "w") as f:
        f.write(test_content)

    result=count_words("test_content.txt")

    for word,count in sorted(result.items()):
        print(f"{word}:{count}")


