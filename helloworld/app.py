#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.apps.base import AppBase

class App(AppBase):
    """
    Receive any message. Respond with 'hello world'
    """

    def handle(self, message):
        message.respond('hello world')
