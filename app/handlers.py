from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

# SQLite
# from DB.SQLite.connect import create_connection
# from DB.SQLite.insert import (
#     insert_user,
#     insert_message,
#     user_exists,
#     insert_email,
#     insert_phone,
# )


import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    email = State()
    phone = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # SQLite
    # with create_connection() as conn:
    #     if conn is not None:
    #         if not user_exists(conn, user_id):
    #             insert_user(conn, user_id, username)

    await message.answer("Hello!", reply_markup=kb.main)


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Select command", reply_markup=kb.help)


@router.callback_query(F.data == "help")
async def about(callback: CallbackQuery):
    await callback.answer("Select command", reply_markup=kb.help)


@router.message(Command("about"))
async def about(message: Message):
    await message.answer("This bot repeats your messages like an echo.")


@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer("This bot repeats your messages like an echo.")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.email)
    await message.answer("Enter your email")


@router.message(Register.email)
async def register_email(message: Message, state: FSMContext):
    user_id = message.from_user.id
    email_text = message.text

    # SQLite
    # if email_text:
    #     with create_connection() as conn:  # SQLite
    #         if conn is not None:
    #             insert_email(conn, email_text, user_id)
    #             await state.update_data(email=email_text)
    #             await state.set_state(Register.phone)
    #             await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")


@router.message(Register.phone, F.contact)
async def register_phone(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone_text = message.contact.phone_number

    # SQLite
    # if phone_text:
    #     with create_connection() as conn:
    #         if conn is not None:
    #             insert_phone(conn, phone_text, user_id)
    #             await state.update_data(phone=phone_text)
    #             await state.clear()
    #             await message.answer("Nice", reply_markup=kb.main)
    # else:
    #     await message.answer("You have not entered your phone!")


@router.message(Command("echo"))
async def echo(message: Message):
    text = message.text[len("/echo ") :]

    # SQLite
    # if text:
    #     with create_connection() as conn:
    #         if conn is not None:
    #             insert_message(conn, message.from_user.id, text)
    #             await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")


@router.message(Command("stop"))
async def stop(message: Message):
    await message.answer("Bye Bye", reply_markup=ReplyKeyboardRemove())
    await message.bot.close()


@router.message()
async def unknown_message(message: Message):
    await message.answer("I don't understand you. Type /help to learn the commands.")
