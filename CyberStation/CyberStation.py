import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    FSInputFile,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Прайс-лист")],
        [KeyboardButton(text="📞 Забронировать")],
        [KeyboardButton(text="📰 Новости и акции")],
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="📍 Адреса")]
    ],
    resize_keyboard=True
)

# Меню выбора клуба для прайса
price_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏢 Льва Толстого 2а")],
        [KeyboardButton(text="🏢 Ленинградская 28")],
        [KeyboardButton(text="🔙 Назад")]
    ],
    resize_keyboard=True
)


# ------------------ ХЕНДЛЕРЫ ------------------ #

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в CyberStation ⚡\n"
        "Твой личный помощник по нашим клубам уже здесь.\n"
        "Выбирай раздел — и я быстро подскажу всё, что нужно.",
        reply_markup=main_menu
    )


# Прайс-лист → выбор клуба
@dp.message(F.text == "💰 Прайс-лист")
async def price_list(message: Message):
    await message.answer("Выберите клуб:", reply_markup=price_menu)


# Прайс — Льва Толстого
@dp.message(F.text == "🏢 Льва Толстого 2а")
async def price_tolstogo(message: Message):
    photo = FSInputFile("images/price_tolstogo.jpg")
    await message.answer_photo(photo, caption="Прайс клуба по адресу Льва Толстого 2а")


# Прайс — Ленинградская
@dp.message(F.text == "🏢 Ленинградская 28")
async def price_leningradskaya(message: Message):
    photo = FSInputFile("images/price_leningradskaya.jpg")
    await message.answer_photo(photo, caption="Прайс клуба по адресу Ленинградская 28")


# Забронировать
@dp.message(F.text == "📞 Забронировать")
async def booking(message: Message):
    await message.answer(
        "Выберите клуб для брони:\n\n"
        "🏢 Льва Толстого 2а — +7 924 205-18-18\n"
        "🏢 Ленинградская 28 — +7 924 229-18-18"
    )


# Назад
@dp.message(F.text == "🔙 Назад")
async def back(message: Message):
    await message.answer("Возвращаюсь в главное меню:", reply_markup=main_menu)


# 📍 Адреса — красиво оформленные ссылки на 2ГИС
@dp.message(F.text == "📍 Адреса")
async def addresses(message: Message):
    await message.answer(
        "📍 *Адреса наших клубов*\n\n"
        "🏢 *Льва Толстого 2а*\n"
        "🗺 На карте: https://2gis.ru/khabarovsk/firm/70000001051440992\n\n"
        "🏢 *Ленинградская 28 (Макси Молл)*\n"
        "🗺 На карте: https://2gis.ru/khabarovsk/firm/70000001089653170",
        parse_mode="Markdown"
    )


# Контакты — VK + телефоны
@dp.message(F.text == "📞 Контакты")
async def contacts(message: Message):

    vk_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🔗 Открыть VK",
            url="https://vk.com/cyber_station"
        )]
    ])

    await message.answer(
        "📍 Наши клубы CyberStation\n\n"
        "🏢 Льва Толстого 2а — круглосуточно\n"
        "📞 +7 924 205-18-18\n\n"
        "🏢 Ленинградская 28 (Тц:Макси Молл) — круглосуточно\n"
        "📞 +7 924 229-18-18\n\n"
        "Мы в VK:",
        reply_markup=vk_kb
    )


# Новости и акции
@dp.message(F.text == "📰 Новости и акции")
async def news(message: Message):
    await message.answer(
        "Все новости и акции публикуются в нашем канале:\n"
        "👉 https://t.me/cyberstationkhv"
    )


# ------------------ ЗАПУСК ------------------ #

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
