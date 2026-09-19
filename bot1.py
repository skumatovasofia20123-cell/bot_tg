import telebot
from telebot import types
import random

facts = [
    "Глобальное потепление — это устойчивый рост средней температуры на Земле.",
    "Основная причина — усиление парникового эффекта из‑за роста концентрации парниковых газов в атмосфере.",
    "Главный источник этих газов — деятельность человека: сжигание ископаемого топлива, промышленность, транспорт, вырубка лесов, сельское хозяйство.",
    "Концентрация CO₂ сейчас выше, чем когда‑либо за последние 800 000 лет.",
    "За последние 50 лет температура на планете росла быстрее, чем за любой аналогичный период за последние 2 000 лет.",
    "Около 90% избыточного тепла, вызванного глобальным потеплением, поглощается океаном.",
    "Арктика теплеет в 3–4 раза быстрее, чем другие регионы планеты.",
    "Таяние ледников и полярных льдов ведёт к повышению уровня Мирового океана, что угрожает островным государствам и прибрежным территориям.",
    "Сейчас уровень CO₂ превышает 420 ppm (частей на миллион), тогда как до промышленной революции он был около 280 ppm.",
    "С 1850 года каждое последующее десятилетие в среднем теплее предыдущего.",
    "Авиация даёт около 2–3% глобальных выбросов CO₂, но из‑за высоты и сопутствующих эффектов её климатическое влияние в разы выше.",
    "Метан (CH₄) в первые 20 лет после выброса примерно в 80 раз сильнее нагревает планету, чем CO₂.",
]

API_TOKEN = "8993911740:AAFVZH47tgq5JeAev-BAduAqiAV4q_kXxnE"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    text = (
        "Hi there, I am fact bot. Я расскажу про глобальное потепление.\n"
        "Нажми кнопку ниже или используй команды:\n"
        "/fact — случайный факт\n"
        "/link — сайт с подробностями"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_fact = types.KeyboardButton("📜 Факт")
    btn_link = types.KeyboardButton("🌐 Ссылка")
    btn_help = types.KeyboardButton("❓ Помощь")
    markup.add(btn_fact, btn_link)
    markup.add(btn_help)

    bot.reply_to(message, text, reply_markup=markup)

@bot.message_handler(commands=["link"])
def show_link(message):
    text = '<a href="https://skumatovasofia20123-cell.github.io/sait232/index.html">Больше информации про глобальное потепление здесь, на моём сайте на GitHub</a>'
    bot.reply_to(message, text, parse_mode="HTML")

@bot.message_handler(commands=["fact"])
def send_fact(message):
    fact = random.choice(facts)
    bot.reply_to(message, fact)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    user_text = message.text.strip()

    if user_text == "📜 Факт":
        fact = random.choice(facts)
        bot.reply_to(message, fact)
        return

    if user_text == "🌐 Ссылка":
        text = '<a href="https://skumatovasofia20123-cell.github.io/sait232/index.html">Больше информации здесь на моем сайте </a>'
        bot.reply_to(message, text, parse_mode="HTML")
        return

    if user_text == "❓ Помощь":
        text = (
            "Я бот про глобальное потепление.\n"
            "Нажми кнопки или используй:\n"
            "/fact — случайный факт\n"
            "/link — ссылка на сайт"
        )
        bot.reply_to(message, text)
        return

    bot.reply_to(
        message,
        "Пожалуйста, используй кнопки под строкой ввода или команды /fact и /link."
    )

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
