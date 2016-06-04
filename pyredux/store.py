from __future__ import absolute_import, unicode_literals, print_function


class Store(object):

    def __init__(self, state=None, root_reducer=None):
        self.__state = state or {}
        self.root_reducer = root_reducer

    def dispatch(self, action):
        self.__state = self.root_reducer(self.state, action)

    @property
    def state(self):
        return self.__state
