from dataclasses import dataclass, field
from library.random_number_utils import RandomUtils

@dataclass(frozen=True,order=True)
class Book:
    title: str
    author: str
    genre: str
    available: bool = True
    id: str = field(default_factory=RandomUtils.generate_random_id)

    @property
    def search_string(self):
        return f"{self.title} {self.author} {self.genre}"

    @property
    def status(self):
        return "Available" if self.available else "Checked Out"