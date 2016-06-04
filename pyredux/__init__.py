from __future__ import absolute_import, unicode_literals, print_function

from pyredux.store import Store


def create_store(root_reducer, initial_state=None):
    return Store(initial_state, root_reducer)
