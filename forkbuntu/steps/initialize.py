from ..step import Step
from munch import munchify
import json

class Initialize(Step):
    messages = munchify({
        'past': 'initialized',
        'present': 'initializing'
    })

    def run(self):
        s = self.app.services
        s.setup.init()
        s.gpg.setup()
        setattr(self.app, 'gpg_keys', s.gpg.get_keys())
        gpg_keys = self.app.gpg_keys

    def finish(self):
        super().finish()
        log = self.app.log
        log.debug('gpg_keys: ' + json.dumps(self.app.gpg_keys, indent=4, sort_keys=True))