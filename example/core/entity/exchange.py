from dataclasses import dataclass


@dataclass
class Exchange:
    code: str
    name: str
    post_code: str
