from pathlib import Path

from pydantic import BaseModel


class FormResponse(BaseModel):
    response: int
    img_path: Path
