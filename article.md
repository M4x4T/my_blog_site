
---

# **Article 2: How Machines Read Text**

## **The First Step: NLP Pre-processing**

---

## **The Hook: Before AI Understands, It Cleans**

Imagine you hand a messy notebook to a robot.

* Some words are in ALL CAPS
* Some are misspelled
* There are emojis, symbols, random punctuation

You understand it instantly.

The robot? Completely lost.

Before AI can understand language, it must **clean and organize it first**.

---

## **What is Pre-processing?**

**Pre-processing** is the **first step in any NLP system**, where raw text is transformed into a clean, structured format that machines can understand. ([LumiChats][1])

Think of it like cooking.

  You don’t throw whole vegetables into a dish.
You wash, peel, and cut them first.

NLP does the same with text.

---

## **Visual Idea **

  Add a simple graphic:

**Messy Text → Cleaning → Structured Words → AI Model**

---

## **Step-by-Step: How Machines Clean Text**

Let’s take a real example:

> “I LOVE running!!! 😄”

To a human: simple.
To a machine: chaos.

Here’s how NLP fixes it:

---

### **1. Text Cleaning (Removing Noise)**

* Remove punctuation: !!!
* Remove emojis 😄
* Normalize text

  Result:
**“I LOVE running”**

This step removes unnecessary symbols and inconsistencies. ([upGrad][2])

---

### **2. Lowercasing (Standardization)**

* “LOVE” → “love”

  Result:
**“i love running”**

Now the machine treats **“Love” and “love” as the same word**.

---

### **3. Tokenization (Breaking into Pieces)**

Tokenization splits text into smaller units called **tokens**. ([upGrad][3])

  Example:
“I love running” →
**[“i”, “love”, “running”]**

---

### **4. Stopword Removal (Filtering Noise Words)**

Remove common words like:

* “the”
* “is”
* “and”

  Result:
**[“love”, “running”]**

These words don’t carry strong meaning in many tasks.

---

### **5. Stemming & Lemmatization (Finding the Root)**

This is where things get interesting.

  Example:

* running → run
* runs → run
* ran → run

**Stemming**: cuts words roughly
**Lemmatization**: finds the correct dictionary form ([Educative][4])

  Final Result:
**[“love”, “run”]**

---

## **Before vs After (Big Picture)**

| Stage     | Output                 |
| --------- | ---------------------- |
| Raw Text  | “I LOVE running!!! 😄” |
| Cleaned   | “i love running”       |
| Tokenized | [i, love, running]     |
| Processed | [love, run]            |

  Now the machine can actually work with it.

---

## **Why This Step is Critical**

Without pre-processing:

* “run”, “running”, “ran” = different words
* Data becomes messy
* Models perform worse

With pre-processing:

* Words become **consistent**
* Noise is removed
* Accuracy improves

  It’s not optional—it’s **foundational**.

---

## **A Deeper Insight (Real-World Reality)**

Even small preprocessing decisions can affect model performance significantly, especially in tasks like sentiment analysis or classification. ([arXiv][5])

  Translation:
This “simple step” can make or break your AI.

---

## **Closing: From Chaos to Structure**

Pre-processing turns messy human language into something machines can actually understand.

It’s the invisible step behind:

* Chatbots
* Search engines
* AI assistants

---

## **What’s Next?**

Now that the text is clean…

  How does AI actually **understand meaning**?

In the next article, we’ll explore **Natural Language Understanding (NLU)**—the moment where machines go from reading words… to understanding intent.

---

---



[1]: https://www.lumichats.com/glossary/nlp-text-preprocessing?utm_source=chatgpt.com "NLP Text Preprocessing — Tokenization, Stemming, Lemmatization | LumiChats Glossary"
[2]: https://www.upgrad.com/blog/text-preprocessing-in-nlp/?utm_source=chatgpt.com "Text Preprocessing in NLP: Steps, Techniques & Example"
[3]: https://www.upgrad.com/blog/what-is-tokenization-and-stemming-techniques-in-nlp/?utm_source=chatgpt.com "Guide: What Is Tokenization and Stemming Techniques in NLP"
[4]: https://www.educative.io/answers/preprocessing-steps-in-natural-language-processing-nlp?utm_source=chatgpt.com "Preprocessing steps in Natural Language Processing (NLP)"
[5]: https://arxiv.org/abs/1707.01780?utm_source=chatgpt.com "On the Role of Text Preprocessing in Neural Network Architectures: An Evaluation Study on Text Categorization and Sentiment Analysis"

---

Вот перевод второй статьи на русский и турецкий языки. Я сохранил структуру, добавил визуальные пояснения и адаптировал примеры для лучшего понимания.

---

## **🇷🇺 Перевод на русский язык**

# **Статья 2: Как машины читают текст**

## **Первый шаг: Препроцессинг в NLP**

---

## **Зацепка: Прежде чем понять, ИИ должен навести порядок**

Представьте, что вы даете роботу блокнот с небрежными записями.

* Часть слов написана ЗАГЛАВНЫМИ БУКВАМИ.
* Есть опечатки.
* Полно эмодзи, символов и случайной пунктуации.

Вы поймете это мгновенно. Робот же — окончательно запутается.

Прежде чем ИИ сможет понять язык, он должен его **очистить и организовать**.

---

## **Что такое препроцессинг (предварительная обработка)?**

**Препроцессинг** — это первый этап в любой NLP-системе, где сырой текст превращается в чистый и структурированный формат, понятный машине.

Это похоже на приготовление еды.
Вы не бросаете овощи в кастрюлю целиком. Сначала вы их моете, чистите и режете.
NLP делает то же самое с текстом.



---

## **Шаг за шагом: Как машины чистят текст**

Возьмем реальный пример:
> «Я ОБОЖАЮ бегать!!! 😄»

Для человека — всё просто. Для машины — хаос. Вот как NLP исправляет это:

### **1. Очистка текста (Удаление шума)**
* Удаляем знаки препинания: !!!
* Удаляем эмодзи: 😄
* Нормализуем текст.

Результат: **«Я ОБОЖАЮ бегать»**

### **2. Приведение к нижнему регистру (Стандартизация)**
* «ОБОЖАЮ» → «обожаю»

Результат: **«я обожаю бегать»**
Теперь машина воспринимает «Обожаю» и «обожаю» как одно и то же слово.

### **3. Токенизация (Разбиение на части)**
Текст делится на мелкие единицы, называемые **токенами**.

Результат: **[«я», «обожаю», «бегать»]**

### **4. Удаление стоп-слов (Фильтрация «шумовых» слов)**
Удаляются часто встречающиеся слова, которые не несут глубокого смысла в ряде задач (местоимения, предлоги):
* «я»

Результат: **[«обожаю», «бегать»]**

### **5. Стемминг и Лемматизация (Поиск основы)**
Самый интересный этап. Машина приводит слова к их корню или словарной форме:
* бегал → бегать
* бегаю → бегать

Результат: **[«обожать», «бегать»]**



---

## **До и После (Общая картина)**

| Этап | Вывод |
| :--- | :--- |
| **Сырой текст** | «Я ОБОЖАЮ бегать!!! 😄» |
| **Очищенный** | «я обожаю бегать» |
| **Токенизированный** | [я, обожаю, бегать] |
| **Обработанный** | [обожать, бегать] |

---

## **Почему этот этап критически важен?**

Без препроцессинга:
* «бег», «бегаю», «бежал» — это три разных слова для машины.
* Данные становятся «грязными».
* Точность моделей падает.

Препроцессинг делает слова **единообразными**, удаляет лишний шум и повышает точность работы ИИ. Это не просто опция — это **фундамент**.

---

## **Заключение: От хаоса к структуре**

Препроцессинг превращает запутанный человеческий язык в нечто, с чем машина действительно может работать. Это невидимый двигатель чат-ботов, поисковых систем и ИИ-ассистентов.

---
---

## **🇹🇷 Türkçe Çeviri**

# **Bölüm 2: Makineler Metni Nasıl Okur?**

## **İlk Adım: NLP Ön İşleme (Pre-processing)**

---

## **Giriş: Yapay Zeka Anlamadan Önce Temizler**

Bir robota karmakarışık notlarla dolu bir defter verdiğinizi hayal edin.

* Bazı kelimeler TAMAMI BÜYÜK HARFLE yazılmış.
* Yazım hataları var.
* Emojiler, semboller ve rastgele noktalama işaretleri her yerde.

Siz bunu anında anlarsınız. Ama robot? Tamamen kaybolur.

Yapay zekanın dili anlayabilmesi için önce onu **temizlemesi ve düzenlemesi** gerekir.

---

## **Ön İşleme (Pre-processing) Nedir?**

**Ön işleme**, ham metnin makinelerin anlayabileceği temiz ve yapılandırılmış bir formata dönüştürüldüğü, herhangi bir NLP sisteminin **ilk adımıdır**.

Bunu yemek yapmaya benzetebilirsiniz.
Sebzeleri bütün halde tencereye atmazsınız. Önce yıkar, soyar ve doğrarsınız.
NLP de metne aynısını yapar.



---

## **Adım Adım: Makineler Metni Nasıl Temizler?**

Gerçek bir örneği ele alalım:
> “Koşmaya BAYILIYORUM!!! 😄”

Bir insan için basit; bir makine için kaos. İşte NLP bunu nasıl çözer:

### **1. Metin Temizleme (Gürültüyü Giderme)**
* Noktalama işaretlerini kaldır: !!!
* Emojileri kaldır: 😄

Sonuç: **“Koşmaya BAYILIYORUM”**

### **2. Küçük Harfe Dönüştürme (Standartlaştırma)**
* “BAYILIYORUM” → “bayılıyorum”

Sonuç: **“koşmaya bayılıyorum”**
Böylece makine, "Bayılıyorum" ve "bayılıyorum" kelimelerini aynı kelime olarak kabul eder.

### **3. Tokenizasyon (Parçalara Ayırma)**
Metni **token** adı verilen daha küçük birimlere böler.

Sonuç: **[“koşmaya”, “bayılıyorum”]**

### **4. Stopword (Etkisiz Kelime) Temizliği**
Anlam taşımayan yaygın kelimeleri çıkarır:
* “ve”, “veya”, “belki” (Bu örnekte anlamlı kelimeler kaldığı için liste aynı kalabilir).

### **5. Stemming ve Lemmatization (Kök Bulma)**
İşlerin ilginçleştiği yer burasıdır. Kelimeleri köküne indirger:
* Koşmaya → Koşmak
* Koşuyorum → Koşmak

Final Sonucu: **[“koşmak”, “bayılmak”]**

---

## **Öncesi vs. Sonrası (Genel Bakış)**

| Aşama | Çıktı |
| :--- | :--- |
| **Ham Metin** | “Koşmaya BAYILIYORUM!!! 😄” |
| **Temizlenmiş** | “koşmaya bayılıyorum” |
| **Tokenize Edilmiş** | [koşmaya, bayılıyorum] |
| **İşlenmiş** | [koşmak, bayılmak] |

---

## **Bu Adım Neden Kritik?**

Ön işleme olmadan:
* “koş”, “koşuyor”, “koştu” makine için farklı kelimelerdir.
* Veri karmaşıklaşır.
* Modellerin performansı düşer.

Ön işleme ile kelimeler **tutarlı** hale gelir, gürültü temizlenir ve doğruluk artar. Bu bir seçenek değil, bir **zorunluluktur**.

---

## **Kapanış: Kaostan Yapıya**

Ön işleme, karmaşık insan dilini makinelerin gerçekten çalışabileceği bir şeye dönüştürür. Sohbet robotlarının, arama motorlarının ve yapay zeka asistanlarının arkasındaki görünmez adımdır.

Вот профессиональный перевод третьей статьи на русский и турецкий языки. Я сохранил техническую точность терминов и адаптировал примеры для сохранения смысла в каждом языке.

---

## **🇷🇺 Перевод на русский язык**



## **🇹🇷 Türkçe Çeviri**

