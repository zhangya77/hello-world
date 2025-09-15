import re
from collections import Counter


def count_words_pythonic(filename):
    """
    使用Pythonic方式统计文本文件中单词出现次数

    参数:
        filename (str): 要分析的文本文件路径

    返回:
        dict: 键为单词，值为出现次数的字典
    """
    try:
        # 使用with语句安全地打开文件
        with open(filename, 'r', encoding='utf-8') as file:
            # 一次性读取整个文件内容
            text = file.read().lower()

            # 使用正则表达式提取所有单词
            words = re.findall(r'\b\w+\b', text)

            # 使用Counter直接统计单词频率
            word_counter = Counter(words)

            # 使用字典推导式过滤掉出现次数少于2次的单词（可选）
            # result = {word: count for word, count in word_counter.items() if count >= 2}

            # 直接返回Counter对象（它已经是字典的子类）
            return dict(word_counter)

    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 未找到")
        return {}
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return {}


# 测试函数
if __name__ == "__main__":
    # 创建一个测试文件
    test_content = """
    Hello world! This is a test file.
    Hello again, this is only a test.
    Testing, testing, 1, 2, 3.
    """

    with open("test_file.txt", "w") as f:
        f.write(test_content)

    # 使用改进后的函数统计单词
    result = count_words_pythonic("test_file.txt")

    # 打印结果
    for word, count in sorted(result.items()):
        print(f"{word}: {count}")