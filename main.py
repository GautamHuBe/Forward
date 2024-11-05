from plugins.web_worker import start_worker
from bot import Bot

app = Bot()
start_worker()
app.run()
