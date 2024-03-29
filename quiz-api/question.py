import json


class Question:
    def __init__(self,_id: int, title: str, text: str, image: str, position: int, possibleAnswers: list) -> None:
        self.title = title
        self._id=_id
        self.text = text
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

    def to_dict(self):
        return {
            "id":self._id,
            "position": self.position,
            "title": self.title,
            "text": self.text,
            "image": self.image,
            "possibleAnswers": self.possibleAnswers
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data):
        return cls(_id=data["id"],position=data["position"], title=data["title"], text=data["text"], image=data["image"], possibleAnswers=data["possibleAnswers"])


    @classmethod
    def from_json(cls, json_data):
        return cls.from_dict(json.loads(json_data))
