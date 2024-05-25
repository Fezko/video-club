import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ContentType
from aiogram.types import Video

bot = Bot(token="7096491396:AAFSRQHELSCCRfTKCPQUarutShBIYbQyQLk")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот Yarik и я умею делать видео в кружок,отправь видео!")

@dp.message(F.content_type==ContentType.VIDEO)
async def video_id(message):
  document_id = message.video.file_id
  file_info = await bot.get_file(document_id)
  print(document_id)
  # video = Video(file_unique_id=document_id, width=300, height=300)
  await bot.send_message(message.chat.id, document_id)
  await bot.send_video_note(message.chat.id, document_id, )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


