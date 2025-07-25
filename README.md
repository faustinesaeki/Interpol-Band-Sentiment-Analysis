# Interpol-Band-Sentiment-Analysis

---

### Important note / Важные замечания:
- Interpol's music is very gloomy by itself, so it's kinda hard to pick one or even five songs that are the "gloomiest".
- I'm not a data scientist, just interested in this field and wanted to try stuff out, so the results **MAY NOT BE ACCURATE**.
- If you have suggestions on how to improve the code, I would love to know how.
- I used the model only to analyze the lyrics. Tempo and key emotions are just weights that are added to the existing results, so I'm not sure how good of a practice is this.
- If you want to use the code on other artist, keep in mind that I had to clean a few lyrics and erase the "contributors" part before the song.

---

- Музыка Interpol сама по себе мрачная, так что выбрать даже несколько песен может быть проблематично.
- Я не дата саентист, просто интересуюсь этой темой, так что результаты могут **быть неточными**.
- Если у вас есть предложения по тому, как улучшить код, я была бы рада узнать.
- Модель использовалась только для анализа текста песен. Эмоции от темпа и тональности -- веса, добавляемые к оригинальному результату, так что я не уверена по поводу того, насколько эта практика хорошая.
- Если вы хотите использовать код для другого исполнителя, имейте в виду, что пришлось несколько песен дочищать вручную (текст перед песней).

---
## Used stuff / Использованные штуки:
- Model / Модель: [bhadresh-savani/distilbert-base-uncased-emotion](https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion)
- Genius API
- Tunebat (key (тональность) / tempo (темп)): [\*тык\*](https://tunebat.com/)
- Libs (Библиотеки) : streamlit, transformers, pandas, lyricsgenius, plotly.express

---

## About / О проектике:
- `Getting Lyrics.ipynb` -- Getting lyrics using Genius API, cleaning (получение текста с Genius API и чистка текста)
- `Analysis.ipynb` -- Sentiment analysis (Эмоциональный анализ)
- `data/` -- Different versions of data on different steps (Разные версии данных на разных шагах)
- `assets/` -- Funny pics (Картиночки)
- `visuals.py` -- Visualisation using Streamlit (Визуализация с помощью Streamlit)
- `visuals_markdown.py` -- Markdown for Streamlit (kinda chaotic) (Разметка и стили для Streamlit (довольно хаотично выглядит))

## Installation / Установка:

``` bash
pip install -r requirements.txt -r local_requirements.txt
```
- `requirement.txt` - only for Streamlit to work (только для работы Streamlit)
- `local_requirements.txt` - for other files to work, contains `transformers` and `torch` (Для работы других файлов, содержит тяжёлые библиотеки)

## Preview / Превью:

<img width="944" height="913" alt="image" src="https://github.com/user-attachments/assets/28364b00-4dd4-4036-8fb3-317b1d9ba16d" />
