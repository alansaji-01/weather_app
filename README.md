# weather_app
## 🚀 Quick Start

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install dependencies:**
   ```
   pip install django python-dotenv discord.py requests python-telegram-bot
   ```

3. **Create a `.env` file** in the project root (where `manage.py` is) with the following content:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   WEATHER_API_KEY=your_openweathermap_api_key
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

4. **Run database migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the Django server:**
   ```
   python manage.py runserver
   ```

6. **Run the bots (in separate terminals):**
   ```
   python manage.py runbot
   python manage.py rundiscord
   ```

---

## ⚠️ Known Issues

- **Discord Bot:**  
  There is a known issue where you may see errors like `'int' object has no attribute 'upper'` when using the `!weather` command.  
  This is likely caused by a dependency or the Discord API library, not your code.  
  If you encounter this, make sure your dependencies are up to date:
  ```
  pip install --upgrade discord.py
  ```
  The rest of the project (Telegram bot and Django app) should work as expected.

---

## .gitignore

Your `.gitignore` should include:
```
.env
*.env
__pycache__/
*.pyc
```

---

## 📄 License

[MIT](LICENSE) or your chosen license.
