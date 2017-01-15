class View:
    def __init__(self):
        pass

    def pre_render(self):
        pass

    def on_render(self):
        self.pre_render()
        self.render()
        self.post_render()
        pass

    def render(self):
        for child in self.children:
            child.on_render()
        pass

    def post_render(self):
        pass
