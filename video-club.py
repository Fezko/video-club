import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="7096491396:AAFSRQHELSCCRfTKCPQUarutShBIYbQyQLk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот Yarik и я умею делать видео в кружок")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


