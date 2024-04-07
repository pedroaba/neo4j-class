from typing import Literal

from labels import Label
from relations import Relation


class Person:
    def __init__(self, name: str, gender: Literal["mulher", "homem"], age: int):
        self.name = name
        self.gender = gender
        self.age = age

        self._label: Label = Label.NOT_SET
        self._relation: Relation = Relation.NO_RELATION

        self._extra_information: dict = {}

    def to_dict(self) -> dict[str, str | int]:
        return {
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            **self._extra_information
        }

    def add_new_attr(self, attr_name: str, attr_value: str) -> None:
        if attr_name in ["age", "gender", "name"]:
            raise ValueError("Cannot add default attributes!!")

        self._extra_information[attr_name] = attr_value

    @property
    def label(self) -> Label:
        if self._label == Label.NOT_SET:
            raise ValueError("Label not set")

        return self._label

    @label.setter
    def label(self, label: Label) -> None:
        self._label = label

    @property
    def relation(self) -> Relation:
        if self._relation == Relation.NO_RELATION:
            raise ValueError("Label not set")

        return self._relation

    @relation.setter
    def relation(self, relation: Relation) -> None:
        self._relation = relation

