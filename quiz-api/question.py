class Question:
    def __init__(self, title: str, text: str, image: str, position: int, _id: int) -> None:
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self._id = _id
        pass
