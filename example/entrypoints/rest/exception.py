from typing import Dict, Any

from werkzeug.exceptions import HTTPException


class _BaseFlaskException(Exception):
    status_code = None

    def __init__(
        self, message: str, status_code: int = None, payload: Dict[str, Any] = None
    ) -> None:
        super().__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


class NotFoundException(HTTPException):
    code = 404
    description = "Not Found"
