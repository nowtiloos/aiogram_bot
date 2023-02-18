import openai
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import API_TOKEN
from config import OPENAI_TOKEN

openai.api_key = OPENAI_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message()
async def send_answer(message: Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.answer(text=response['choices'][0]['text'])


if __name__ == '__main__':
    dp.run_polling(bot)
