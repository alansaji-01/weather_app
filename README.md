# weather_app
⚠️ Important Note About the Discord Bot

There is a known issue with the Discord bot in this project:  
**You may see errors like `'int' object has no attribute 'upper'` when using the `!weather` command.**  
This issue is likely caused by a dependency or the Discord API library, not by your own code.

If you encounter this error:
- Make sure your dependencies are up to date (`pip install --upgrade discord.py`).
- Check the project issues for updates or workarounds.
- The rest of the project (including the Telegram bot and Django app) should work as expected.

If you find a solution, please open a pull request or issue!

---

**Note:**  
You must create a `.env` file with your API keys (see `.gitignore` and project instructions).
