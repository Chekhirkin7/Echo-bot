from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

# SQLite
# from DB.SQLite.connect import create_connection
# from DB.SQLite.insert import (
#     insert_user,
#     insert_message,
#     user_exists,
#     insert_email,
#     insert_phone,
# )

# PostgreSQL
# from DB.PostgreSQL.connect import create_connection
# from DB.PostgreSQL.insert import (
#     insert_email,
#     insert_message,
#     insert_phone,
#     insert_user,
#     user_exists,
# )

# SQLAlchemy Core
# from DB.SQLAlchemy.sqlalchemy_core import engine, users, messages

# SQLAlchemy session v1
# from DB.SQLAlchemy.sqlalchemy_session_1 import session, User, Message

# SQLAlchemy session v2
# from DB.SQLAlchemy.sqlalchemy_session_2 import session, User, Message

# MongoDB pymongo
# from DB.mondodb.pymongo import db

# MongoDB mongoengine
# from DB.mondodb.mongoengine import User, MessageText

router = Router()


class Register(StatesGroup):
    email = State()
    phone = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # SQLite PostgreSQL
    # with create_connection() as conn:
    #     if conn is not None:
    #         if not user_exists(conn, user_id):
    #             insert_user(conn, user_id, username)

    # SQLAlchemy Core
    # with engine.connect() as conn:
    #     ins_user = users.insert().values(id=user_id, username=username)
    #     conn.execute(ins_user)
    #     conn.commit()

    # SQLAlchemy session v1, v2
    # user = session.query(User).filter_by(id=user_id).first()

    # if not user:
    #     user = User(id=user_id, username=username)
    #     session.add(user)
    #     session.commit()
    #     session.close()

    # await message.answer("Hello!", reply_markup=kb.main)

    # MongoDB pymongo
    # user = db.users.find({"id": user_id})
    # if not user:
    #     db.users.insert_one(
    #         {
    #             "id": user_id,
    #             "username": username,
    #         }
    #     )

    # await message.answer("Hello!", reply_markup=kb.main)

    # MongoDB mongoengine
    # user = User.objects(id=user_id).first()
    # if not user:
    #     user = User(id=user_id, username=username)
    #     user.save()

    # await message.answer("Hello!", reply_markup=kb.main)


@router.callback_query(F.data == "start")
async def help(callback: CallbackQuery):
    await callback.message.answer("Hello")
    await callback.answer("Hello")


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Select command", reply_markup=kb.help)


@router.callback_query(F.data == "help")
async def about(callback: CallbackQuery):
    await callback.message.answer("Select command", reply_markup=kb.help)
    await callback.answer("Select command")


@router.message(Command("about"))
async def about(message: Message):
    await message.answer("This bot repeats your messages like an echo.")


@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):
    await callback.message.answer("This bot repeats your messages like an echo.")
    await callback.answer("This bot repeats your messages like an echo.")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.email)
    await message.answer("Enter your email")


@router.message(Register.email)
async def register_email(message: Message, state: FSMContext):
    user_id = message.from_user.id
    email_text = message.text

    # SQLite PostgeSQL
    # if email_text:
    #     with create_connection() as conn:  # SQLite
    #         if conn is not None:
    #             insert_email(conn, user_id, email_text)
    #             await state.update_data(email=email_text)
    #             await state.set_state(Register.phone)
    #             await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")

    # SQLAlchemy Core
    # if email_text:
    #     with engine.connect() as conn:
    #         ins_email = users.update().where(users.c.id == user_id).values(email=email_text)
    #         conn.execute(ins_email)
    #         conn.commit()
    #         await state.update_data(email=email_text)
    #         await state.set_state(Register.phone)
    #         await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")

    # SQLAlchemy session v1, v2
    # if email_text:
    #     # session.query(User).filter_by(id=user_id).update({"email": email_text})
    #     # session.commit()
    #     # session.close()
    #     user = session.query(User).filter_by(id=user_id).first()
    #     if user:
    #         user.email = email_text
    #         session.commit()
    #         session.close()
    #         await state.update_data(email=email_text)
    #         await state.set_state(Register.phone)
    #         await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")

    # MongoDB pymongo
    # if email_text:
    #     db.users.update_one(
    #         {"id": user_id},
    #         {
    #             "$set": {
    #                 "email": email_text,
    #             }
    #         },
    #     )
    #     await state.update_data(email=email_text)
    #     await state.set_state(Register.phone)
    #     await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")

    # MongoDB mongoengine
    # if email_text:
    #     user = User.objects(id=user_id).first()
    #     user.email = email_text
    #     user.save()
    #     await state.update_data(email=email_text)
    #     await state.set_state(Register.phone)
    #     await message.answer("Enter your phone", reply_markup=kb.get_number)
    # else:
    #     await message.answer("You have not entered your email address!")


@router.message(Register.phone, F.contact)
async def register_phone(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone_text = message.contact.phone_number

    # SQLite PostgreSQL
    # if phone_text:
    #     with create_connection() as conn:
    #         if conn is not None:
    #             insert_phone(conn, user_id, phone_text)
    #             await state.update_data(phone=phone_text)
    #             await state.clear()
    #             await message.answer("Nice", reply_markup=kb.main)
    # else:
    #     await message.answer("You have not entered your phone!")

    # SQLAlchemy Core
    # if phone_text:
    #     with engine.connect() as conn:
    #         ins_phone = users.update().where(users.c.id == user_id).values(phone=phone_text)
    #         conn.execute(ins_phone)
    #         conn.commit()
    #         await state.update_data(phone=phone_text)
    #         await state.clear()
    #         await message.answer("Nice", reply_markup=kb.main)
    # else:
    #     await message.answer("You have not entered your phone!")

    # SQLAlchemy session v1, v2
    # if phone_text:
    #     session.query(User).filter_by(id=user_id).update({"phone": phone_text})
    #     session.commit()
    #     session.close()
    #     await state.update_data(phone=phone_text)
    #     await state.clear()
    #     await message.answer("Nice", reply_markup=kb.main)
    # else:
    #     await message.answer("You have not entered your phone!")

    # MongoDB pymongo
    #     if phone_text:
    #         db.users.update_one(
    #             {"id": user_id},
    #             {
    #                 "$set": {
    #                     "phone": phone_text,
    #                 }
    #             },
    #         )
    #         await state.update_data(phone=phone_text)
    #         await state.clear()
    #         await message.answer("Nice", reply_markup=kb.main)
    #     else:
    #         await message.answer("You have not entered your phone!")

    # MongoDB mongoengine
    # if phone_text:
    #     User.objects(id=user_id).update(set__phone=phone_text)
    #     await state.update_data(phone=phone_text)
    #     await state.clear()
    #     await message.answer("Nice", reply_markup=kb.main)
    # else:
    #     await message.answer("You have not entered your phone!")


@router.message(Command("echo"))
async def echo(message: Message):
    text = message.text[len("/echo ") :]

    # SQLite PostgreSQL
    # if text:
    #     with create_connection() as conn:
    #         if conn is not None:
    #             insert_message(conn, message.from_user.id, text)
    #             await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")

    # SQLAlchemy Core
    # if text:
    #     with engine.connect() as conn:
    #         ins_message = messages.insert().values(user_id=message.from_user.id, message_text=text)
    #         conn.execute(ins_message)
    #         conn.commit()
    #         await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")

    # SQLAlchemy session v1, v2
    # if text:
    #     message_user = Message(user_id=message.from_user.id, message_text=text)
    #     session.add(message_user)
    #     session.commit()
    #     session.close()
    #     await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")

    # MongoDB pymongo
    # if text:
    #     db.messages.insert_one(
    #         {
    #             "user_id": message.from_user.id,
    #             'message_text': text,
    #         }
    #     )
    #     await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")

    # MongoDB mongoengine
    # if text:
    #     msg = MessageText(user_id=message.from_user.id, message_text=text)
    #     msg.save()
    #     await message.answer(text)
    # else:
    #     await message.answer("Write something after the /echo command!")


@router.message(Command("stop"))
async def stop(message: Message):
    await message.answer("Bye Bye", reply_markup=ReplyKeyboardRemove())
    await message.bot.close()


@router.message()
async def unknown_message(message: Message):
    await message.answer("I don't understand you. Type /help to learn the commands.")
