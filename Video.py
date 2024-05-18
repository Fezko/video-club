import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ContentType

bot = Bot(token="7096491396:AAFSRQHELSCCRfTKCPQUarutShBIYbQyQLk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот Yarik и я умею делать видео в кружок,отправь видео!")

@dp.message(F.content_type==ContentType.VIDEO)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


