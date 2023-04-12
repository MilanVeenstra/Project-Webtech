class PostValidator:
    def __init__(self, data):
        self.data = data

    def validate_title(self):
        title = self.data.get('title')
        if title and title[0].islower():
            self.data['title'] = title.capitalize()
        return self.data['title']
