import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ContentType
from aiogram.types import Video

import moviepy.editor as mpy
from aiogram.types import FSInputFile

bot = Bot(token="7096491396:AAFSRQHELSCCRfTKCPQUarutShBIYbQyQLk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот Yarik и я умею делать видео в кружок,отправь видео!")

@dp.message(F.content_type==ContentType.VIDEO)
async def video_id(message):
    await message.answer("Пожалуйста подождите😉")
    file_id = message.video.file_id  # Get file id
    file = await bot.get_file(file_id)  # Get file path
    await bot.download_file(file.file_path, "video.mp4")
    video = mpy.VideoFileClip("video.mp4")
    video = video.resize((360, 360))
    video.write_videofile('video-cropped.mp4')
    video = FSInputFile('video-cropped.mp4')

    await bot.send_video_note(message.chat.id, video)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


