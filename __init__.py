try:
    from guessit import guessit
except:
    import os
    from framework import app
    os.system('{} install guessit'.format(app.config['config']['pip']))

from .plugin import blueprint, menu, plugin_load, plugin_unload, plugin_info, process_telegram_data
from .logic import Logic
from .model import ModelSetting, ModelMovieItem

