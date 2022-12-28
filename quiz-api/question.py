import json


class Question:
    def __init__(self, title: str, text: str, image: str, position: int) -> None:
        self.title = title
        self.text = text
        self.image = image
        self.position = position


    def to_dict(self):
        return {
            "position": self.position,
            "title": self.title,
            "text": self.text,
            "image": self.image,
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        return cls(position=data["position"], title=data["title"], text=data["text"], image=data["image"])

    @classmethod
    def from_json(cls, json_data):
        return cls.from_dict(json.loads(json_data))
