# Echo Bot

## Overview
Echo Bot is a Telegram bot built with Aiogram that echoes user messages. It features command handling, keyboard support, database integration, and user authentication.

## Features
- **Start Command (`/start`)**: Greets the user.
- **Help Command (`/help`)**: Displays a list of available commands.
- **About Command (`/about`)**: Provides information about the bot.
- **Echo Command (`/echo <text>`)**: Repeats the provided text.
- **Unknown Message Handling**: Informs the user when an unrecognized command is entered.
- **Keyboard Menu**: Supports both inline and reply keyboards.
- **User Authentication**: Registers users in the database.
- **Database Storage**: Stores user data and bot interactions.

## Technologies Used
- **Python**
- **Aiogram** (Telegram bot framework)
- **SQLite / PostgreSQL** (Database for storing user data)
- **SQLAlchemy** (ORM for database management)
- **Docker** (For containerized deployment)
- **Redis** (Optional: For caching and session management)
- **Asyncio** (For asynchronous execution)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Chekhirkin7/Echo-bot.git
   cd Echo-bot
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Set up the `.env` file with your Telegram Bot Token and database credentials:
   ```ini
   BOT_TOKEN=your_bot_token
   DATABASE_URL=sqlite:///database.db  # Or use PostgreSQL
   ```

4. Run the bot:
   ```sh
   poetry run python main.py
   ```

## Database Setup
If using PostgreSQL, ensure the database is created and update `DATABASE_URL` accordingly.

## Deployment
- Use **Docker** for deployment:
  ```sh
  docker-compose up --build -d
  ```
- Alternatively, deploy on a **VPS** with a system service.

## Future Enhancements
- Logging and monitoring
- User statistics and analytics
- WebSockets integration for real-time updates

## License
This project is licensed under the MIT License.
