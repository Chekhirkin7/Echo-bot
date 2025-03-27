from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer('Hello!', reply_markup=kb.main)

@router.message(Command('help'))
async def help(message: Message):
	await message.answer("Select command", reply_markup=kb.help)

@router.callback_query(F.data == 'help')
async def about(callback: CallbackQuery):
	await callback.answer("Select command", reply_markup=kb.help)

@router.message(Command('about'))
async def about(message: Message):
	await message.answer("This bot repeats your messages like an echo.")

@router.callback_query(F.data == 'about')
async def about(callback: CallbackQuery):
	await callback.message.answer("This bot repeats your messages like an echo.")

@router.message(Command('echo'))
async def echo(message: Message):
	text = message.text[len("/echo "):]
	if text:
		await message.answer(text)
	else:
		await message.answer("Write something after the /echo command!")

@router.message()
async def unknown_message(message: Message):
	await message.answer("I don't understand you. Type /help to learn the commands.")