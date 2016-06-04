PyRedux
---


This is an experiment at implementing [Redux](https://github.com/reactjs/redux) in Python. (USE AT YOUR OWN RISK)

# Is this even useful?
Probably not, but it is interesting to see how simple/easy it is. Maybe it does have some uses 


# Example usage
```
from pyredux import create_store
from copy import deepcopy


def my_reducer(state, action):
    if action['type'] == 'MY_ACTION':
        new_state = deepcopy(state)
        new_state['action'] = action['value']
        return new_state
    return state

store = create_store(my_reducer,  {})
store.dispatch(({'type': 'MY_ACTION', 'value': 'test'}))
```
