import json


class Answer:
    def __init__(self, text: str, is_correct: bool) -> None:
        self.text = text
        self.is_correct = is_correct

    @classmethod
    def from_json(cls, json_data):
        return cls.from_dict(json.loads(json_data))

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {"text": self.text, "is_correct": self.is_correct}

    @classmethod
    def from_dict(cls, data):
        return cls(text=data["text"], is_correct=data["is_correct"])
