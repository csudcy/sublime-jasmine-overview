# Sublime Jasmine Overview

A Sublime Text plugin to give an overview of Jasmine functions & their descriptions

## Usage

The only default shortcut is `ctrl+k, ctrl+j` to show the Jasmine Overview quick panel (ignoring `beforeEach`/`afterEach`):

`TODO: image`

If you want to include `beforeEach`/`afterEach`, you can add a shortcut like this:
```json
    { "keys": ["ctrl+k", "ctrl+j"], "command": "jasmine_overview", "args": {"include_before_after": true} }
```

You can also open the Jasmine Overview quick panel through the menu at `Preferences > Package Settings > Jasmine Overview`.


## Todo

* Improve readme
  * Add images/gifs
* Add tests
  * Check `this.find_stub.withArgs('textarea.comment').returns({val: this.val_stub});` does not get found
* Move menu entries out of preferences
* Jump back to original cursor location if quick panel is cancelled

## Installing

### Using Sublime Package Control

If you are using [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install Jasmine Overview via the `Package Control: Install Package` menu item.

1. Press `CTRL+SHIFT+p`
1. Type *"Install Package"*
1. Find `Jasmine Overview`
1. Done!

### Download Manually

You're going to have to work this out on your own (or, you know, just use package control...).
