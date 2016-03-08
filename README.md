# Sublime Jasmine Overview

A Sublime Text plugin to give an overview of Jasmine functions & their descriptions

The default shortcut is `ctrl+k, ctrl+j` and `beforeEach`/`afterEach` are not shown.

To show `beforeEach` and `afterEach` you can add a shortcut like this:
```json
    { "keys": ["ctrl+k", "ctrl+j"], "command": "jasmine_overview", "args": {"include_before_after": true} }
```

These can also be accessed through the menu at `Preferences > Package Settings > Jasmine Overview`.

## Todo

* Improve readme
  * [ ] Better summary text
  * [ ] Add images/gifs
  * [ ] Add install instructions
* [ ] Add tests
  * Check `this.find_stub.withArgs('textarea.comment').returns({val: this.val_stub});` does not get found
* [ ] Move menu entries out of preferences
* [ ] Jump back to original cursor location if quick panel is cancelled
