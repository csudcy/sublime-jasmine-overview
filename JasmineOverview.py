import sublime, sublime_plugin

class JasmineOverviewCommand(sublime_plugin.TextCommand):
    # To debug: view.run_command('jasmine_overview')

    def run(self, edit):
        self.symbols = self.view.get_symbols()
        self.view.window().show_quick_panel(
            self.get_symbol_names(),
            self.on_done,
            #None,
            #None,
            on_highlight=self.on_highlight
        )

    def get_symbol_names(self):
        return [
            symbol[1]
            for symbol in self.symbols
        ]

    def on_highlight(self, index):
        print('Highlight')
        print(index)

    def on_done(self, index):
        print('Done')
        print(index)
