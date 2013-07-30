import logging

from jarabe.webservice import accountsmanager
from cpsection.webaccount.web_service import WebService

class WebService(WebService):
    def __init__(self):
        logging.error('Getting mock-service account')
        self._account = accountsmanager.get_account('mock-service')
        logging.error(self._account)

    def get_icon_name(self):
        return 'mock-service'

    def config_service_cb(self, widget, event, container):
        logging.debug('config_service_cb')

        for c in container.get_children():
            container.remove(c)

        label = Gtk.Label('mock service label')
        container.add(label)
        container.show_all()
