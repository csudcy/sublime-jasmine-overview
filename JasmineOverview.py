import re

import sublime_plugin


class JasmineOverviewCommand(sublime_plugin.TextCommand):
    # To debug: view.run_command('jasmine_overview')

    KEYWORD_RE = r'(describe|it)\w*\('
    KEYWORD_WITH_BEFORE_AFTER_RE = r'(describe|beforeEach|afterEach|it)\w*\('

    def run(self, edit, include_before_after=False):
        self.locations = self.get_locations(include_before_after)
        self.original_selection = self.view.sel()
        print(self.original_selection)
        print(dir(self.original_selection))
        self.view.window().show_quick_panel(
            self.get_symbol_names(),
            self.on_done,
            on_highlight=self.on_highlight
        )

    def get_locations(self, include_before_after):
        locations = []

        if include_before_after:
            keywords = self.view.find_all(self.KEYWORD_WITH_BEFORE_AFTER_RE)
        else:
            keywords = self.view.find_all(self.KEYWORD_RE)

        for keyword in keywords:
            region = self.view.line(keyword)
            name = self.view.substr(region)

            # Remove function defs
            name = re.sub(
                r',?\s*function\s*\(\s*\)\s*{?',
                '',
                name
            )

            # Make the formatting nicer
            name = name.rstrip()
            if name[-1] == '(':
                name = name[:-1]
            else:
                name = name.replace('(', ': ')

            # Add it to the list
            locations.append({
                'region': region,
                'name': name
            })

        if not locations:
            locations.append({
                'region': None,
                'name': '<No Jasmine functions found>'
            })

        return locations

    def get_symbol_names(self):
        return [
            symbol['name']
            for symbol in self.locations
        ]

    def on_highlight(self, index):
        # Highlight the selected keyword
        location_region = self.locations[index]['region']
        if location_region:
            # Select the region
            self.view.sel().clear()
            self.view.sel().add(location_region)

            # Center on the selection
            self.view.show_at_center(location_region)

    def on_done(self, index):
        # Check if the quick panel was cancelled
        if index == -1:
            print('TODO: Reset to original_selection')
