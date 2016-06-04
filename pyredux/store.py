from __future__ import absolute_import, unicode_literals, print_function


class Store(object):

    def __init__(self, state=None, root_reducer=None):
        self.__state = state or {}
        self.root_reducer = root_reducer
        self.listeners = []

    def dispatch(self, action):
        self.__state = self.root_reducer(self.state, action)
        self.__notify()

    def __notify(self):
        for listener in self.listeners:
            listener()

    def subscribe(self, listener):
        self.listeners.append(listener)

    @property
    def state(self):
        return self.__state
