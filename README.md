# Документация к чат-боту

## Обзор

Данная программа на Python реализует чат-бота, используя сочетание библиотеки `transformers` от Hugging Face и библиотеки `TextBlob` для обработки естественного языка (NLP). Библиотека `transformers` используется для загрузки предварительно обученной модели каузального языка, которая генерирует ответы для диалога. `TextBlob` применяется для предварительной коррекции текста, что позволяет обеспечить более грамматически корректный ввод в модель.

## Особенности

- **Коррекция текста**: Программа использует `TextBlob` для исправления базовых грамматических ошибок во вводимом тексте перед его обработкой.
- **Модель для диалога**: Использует токенизатор `codegen-350M-mono` от Salesforce и модель `DialoGPT-medium` от Microsoft для генерации диалогового текста.
- **Интерактивный чат**: Запускает интерактивную оболочку, которая позволяет пользователю вести диалог с ботом и получать ответы в реальном времени.

## Требования

- Python версии 3.x
- Библиотека `transformers`
- Библиотека `TextBlob`

Кроме того, для использования коррекции текста с помощью `TextBlob` могут потребоваться ресурсы `nltk`, такие как 'punkt', 'averaged_perceptron_tagger' и 'wordnet'.

## Установка
Установите необходимые библиотеки с помощью `pip`:
pip install transformers textblob

## Использование
Для использования чат-бота запустите скрипт. После инициализации чат-бот предложит ввести текст. Он исправит ваш ввод, если это необходимо, и затем предоставит ответ. Чтобы выйти из чата, введите 'exit'.

## Функции
correct_text(input_text: str) -> str
Принимает строку input_text, исправляет грамматику с использованием TextBlob и возвращает исправленный текст в виде строки.

chatbot_response(input_text: str) -> str
Принимает строку input_text, исправляет текст с помощью функции correct_text и генерирует ответ с помощью предварительно обученной языковой модели. Возвращает ответ чат-бота в виде строки.
