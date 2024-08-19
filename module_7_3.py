import re

class FileCreator:
    def __init__(self, file_contents):
        self.file_contents = file_contents

    def create_and_write_to_file(self):
        for file_name, content in self.file_contents.items():
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(content)

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = self._read_and_process_file(file_name)
            all_words[file_name] = words
        return all_words

    def _read_and_process_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            # Заменяем все знаки препинания и специальные символы на пробел
            content = re.sub(r'[^\w\s]', ' ', content)
            words = content.split()
            return words

    def find(self, word):
        word_positions = {}
        all_words = self.get_all_words()
        word_casefolded = word.casefold()
        for file_name, words in all_words.items():
            for index, w in enumerate(words):
                if w.casefold() == word_casefolded:
                    word_positions[file_name] = index
                    break
        return word_positions

    def count(self, word):
        word_counts = {}
        all_words = self.get_all_words()
        word_casefolded = word.casefold()
        for file_name, words in all_words.items():
            count = sum(1 for w in words if w.casefold() == word_casefolded)
            word_counts[file_name] = count
        return word_counts

# Основное выполнение
if __name__ == "__main__":
    # Создание и запись содержимого в файлы
    file_contents = {
        'file1.txt': "word1,  word2, ",
        'file2.txt': "word3, word4, ",
        'file3.txt': "word5, word6, word7"
    }
    file_creator = FileCreator(file_contents)
    file_creator.create_and_write_to_file()

    finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
    print(finder.get_all_words())
    print(finder.find('word1'))
    print(finder.count('word1'))
    print()
    # Создание и запись содержимого в файл
    file_creator = FileCreator({'test_file.txt': "It's a text for task. Найти везде, используйте его для самопроверки. Успехов в решении задачи. TEXT TEXT TEXT."})
    file_creator.create_and_write_to_file()

    # Создание экземпляра WordsFinder и вызов методов
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))     # Позиция слова 'TEXT'
    print(finder2.count('teXT'))    # Количество слова 'teXT'