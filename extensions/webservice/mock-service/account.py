import os
import logging
from random import randint
from gettext import gettext as _

from sugar3.graphics.menuitem import MenuItem
from sugar3.graphics import style
from jarabe.webservice import account

ACCOUNT_NAME = _('mock-service')

class MockAccount(account.Account):
    def __init__(self):
        return

    def get_description(self):
        return ACCOUNT_NAME

    def get_shared_journal_entry(self):
        return MockSharedJournalEntry()

    def get_token_state(self):
        return self.STATE_VALID

    def get_public_id(self):
        return 'id %s' % randint(1, 100000)

    def get_latest_post(self, public_id):
        return get_post()


class MockSharedJournalEntry(account.SharedJournalEntry):
    def __init__(self):
        return

    def get_share_menu(self, metadata):
        share_menu = ShareMenu(metadata)
        return share_menu

    def get_refresh_menu(self):
        refresh_menu = RefreshMenu()
        return refresh_menu


class ShareMenu(MenuItem):
    def __init__(self, metadata):
        MenuItem.__init__(self, text_label=ACCOUNT_NAME)
        self.show()


class RefreshMenu(MenuItem):
    def __init__(self):
        MenuItem.__init__(self, text_label=ACCOUNT_NAME)
        self.show()

    def set_metadata(self, metadata):
        return


class MockWebServicePost(account.WebServicePost):
    def __init__(self, public_id):
        self._public_id = public_id

    def get_title(self):
        return "Title"

    def get_message(self):
        return ("Designed from the ground up especially for children, Sugar"
                "offers an alternative to traditional \"office-desktop\""
                "software. Id: %s" % self._public_id)

    def get_picture(self):
        """Returning webservice icon name currently"""
        return 'mock-service'

    def get_link(self):
        return "http://sugarlabs.org"


def get_account():
    return MockAccount()

def get_post():
    return MockWebServicePost()
