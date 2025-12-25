import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

BOT_TOKEN = "8049372220:AAGcKaZLCr2HMhOaSIdgpKvNqpEDpk0I4eM"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message):
    await message.answer("Бот не для тебя.")

@dp.inline_query()
async def inline_handler(inline_query: InlineQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Портфолио", url="https://t.me/portfolio5667681149"),
                InlineKeyboardButton(text="Отзывы", url="https://t.me/reviews5667681149")
            ],
            
        ]
    )

    result = InlineQueryResultArticle(
        id="default",
        title="Краткая информация",
        input_message_content=InputTextMessageContent(
            message_text="<b>Краткая информация:</b>",
            parse_mode="HTML"
        
        ),
        reply_markup=keyboard
    )
    
    await inline_query.answer(results=[result], cache_time=1)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
