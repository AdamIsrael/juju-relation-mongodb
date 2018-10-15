# Overview

This interface layer handles communication between Mongodb and its clients.

## Usage

### Provides

```python
@when('mongo.available')
def mongo_available(mongo):
    for unit in mongo:
        add_mongo(unit['hostname'], unit['port'])
```
