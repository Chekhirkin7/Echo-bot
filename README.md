# Telegram Echo Bot

A simple Telegram bot that echoes user messages and allows users to register their email and phone numbers. Built using the [aiogram](https://github.com/aiogram/aiogram) framework and supports various databases such as SQLite, PostgreSQL, and MongoDB.

## Features

- `/start` - Starts the bot and greets the user.
- `/help` - Displays available commands.
- `/about` - Provides information about the bot.
- `/register` - Starts the registration process where users provide their email and phone number.
- `/echo` - Repeats the user's message.
- `/stop` - Stops the bot and ends the session.

## Installation

### Prerequisites

- Python 3.7+
- Telegram Bot API token
- [aiogram](https://github.com/aiogram/aiogram) library
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telegram-echo-bot.git
   cd telegram-echo-bot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory with the following content:
   ```env
   TELEGRAM_BOT_API=your-telegram-bot-api-token
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Database Support

This bot supports multiple database backends. Currently, the following databases are included in the code but commented out:

- **SQLite**
- **PostgreSQL**
- **MongoDB**
- **SQLAlchemy (Core, Session v1, and Session v2)**

To enable a specific database, uncomment the relevant code and configure the connection details accordingly.

## Commands

- `/start` - Greets the user and provides a main menu.
- `/help` - Shows a list of available commands.
- `/about` - Provides information about the bot.
- `/register` - Starts the user registration process.
- `/echo` - The bot will repeat the message provided after the `/echo` command.
- `/stop` - Stops the bot.