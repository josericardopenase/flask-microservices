class PostSerializer:

    def __init__(self, new):
        self.new = new

    def to_json(self):
        return {
                "title" : self.new.title,
                "subtitle" : self.new.subtitle,
                "content" : self.new.content
        }
