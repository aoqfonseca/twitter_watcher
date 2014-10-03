# -*- coding: utf-8 -*-
import logging

from flask.ext.script import Manager, Server
from twitter_watcher.server import api
from twitter_watcher.commands import Twitter

manager = Manager(api)

log = logging.getLogger()
log.setLevel(logging.DEBUG)

fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.\
    Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

log.addHandler(fh)
log.addHandler(ch)


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

manager.add_command('start_twitter', Twitter())

if __name__ == "__main__":
    manager.run()
