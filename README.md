# Install dependencies

```
pipenv sync
```

# Update dependencies

Modify the Pipfile (NOT Pipfile.lock) to have the new library & version number (doesn't need to be exact, just whatever works for now)

Then run `pipenv lock` to generate Pipfile.lock.

# Running the server

`python flask_server.py`
