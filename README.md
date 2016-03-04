# Sublime Jasmine Overview

A Sublime Text 3 plugin to give an overview of Jasmine functions

The default shortcut is `ctrl+k, ctrl+j` and `beforeEach`/`afterEach` are not shown.

To show `beforeEach` and `afterEach` you can add a shortcut like this:
```json
    { "keys": ["ctrl+k", "ctrl+j"], "command": "jasmine_overview", "args": {"include_before_after": true} }
```

These can also be accessed through the menu at `Preferences > Package Settings > Jasmine Overview`.
