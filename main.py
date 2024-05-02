from flask import Flask, render_template
from bs4 import BeautifulSoup
from collections import Counter
import re

app = Flask(__name__)


@app.route('/', methods=['GET'])
def count_words():
    # Путь к файлу index.html в папке templates
    filepath = 'templates/index.html'

    try:
        # Читаем содержимое файла index.html
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Используем BeautifulSoup для парсинга HTML и извлечения текста
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()

        # Приводим текст к нижнему регистру и разбиваем на слова
        words = re.findall(r'\b\w+\b', text.lower())

        # Подсчитываем количество повторений каждого слова
        word_count = Counter(words)

        # Сортируем словарь по значениям (количеству повторений) в порядке убывания
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

        # Возвращаем результат в виде HTML-страницы, используя шаблон
        return render_template('index.html', word_count=sorted_word_count)

    except Exception as e:
        # Если произошла ошибка, возвращаем ее сообщение
        return str(e), 500


if __name__ == '__main__':
    # Запуск приложения Flask на порту 5000
    app.run(port=5000)