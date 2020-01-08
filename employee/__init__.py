def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user')
    super(SnippetSerializer, self).__init__(*args, **kwargs)