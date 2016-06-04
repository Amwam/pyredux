from __future__ import absolute_import, unicode_literals

import unittest
from copy import deepcopy

from pyredux import create_store


class TestCreateStore(unittest.TestCase):

    def test_create_dispatch_and_notify(self):
        calls = {}

        def reducer(state, action):
            if action['type'] == 'MYTYPE':
                calls['reducer'] = True
                new_state = deepcopy(state)
                new_state['reducer'] = True
                return new_state
            return state

        def listener():
            calls['listener'] = True

        store = create_store(reducer, {})
        store.subscribe(listener)

        store.dispatch({'type': 'MYTYPE'})

        self.assertTrue(store.state['reducer'], 'state not changed in reducer')
        self.assertTrue(calls['reducer'], 'Not reduced')
        self.assertTrue(calls['listener'], 'not notified')


if __name__ == '__main__':
    unittest.main()
