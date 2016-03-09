import sublime_plugin

from . import jasmine_overview_helpers


class JasmineOverviewCommand(sublime_plugin.TextCommand):

    def run(self, edit, include_before_after=False):
        self.locations = self.get_locations(include_before_after)
        self.original_selections = [s for s in self.view.sel()]
        self.view.window().show_quick_panel(
            self.get_location_names(),
            self.on_done,
            on_highlight=self.on_highlight
        )

    def get_locations(self, include_before_after):
        locations = []

        if include_before_after:
            keywords = self.view.find_all(jasmine_overview_helpers.KEYWORD_WITH_BEFORE_AFTER_RE)
        else:
            keywords = self.view.find_all(jasmine_overview_helpers.KEYWORD_RE)

        for keyword in keywords:
            region = self.view.line(keyword)
            code = self.view.substr(region)
            name = jasmine_overview_helpers.get_name(code)

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

    def get_location_names(self):
        return [
            location['name']
            for location in self.locations
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
            # Select all the originally selected regions
            self.view.sel().clear()
            self.view.sel().add_all(self.original_selections)

            # Center on the first selection
            self.view.show_at_center(self.original_selections[0])
