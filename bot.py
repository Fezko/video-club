import asyncio
import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="7096491396:AAFSRQHELSCCRfTKCPQUarutShBIYbQyQLk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот Yarik и я умею делать видео в кружок,отправь видео!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


@dp.message(content_types=['video'])
def send_text(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('video.mp4', 'wb') as video:
        video.write(downloaded_file)
    bot.send_video_note(message.chat.id, open('video.mp4', 'rb'))