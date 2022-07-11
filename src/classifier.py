from pathlib import Path

from flask import Blueprint, render_template, request
from pydantic import BaseModel

bp = Blueprint('classifier', __name__)


class FormResponse(BaseModel):
    response: int
    img_path: Path


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(FormResponse(**request.form))
    return render_template(
        template_name_or_list="classifier/index.html",
        img_path="babayaga"
    )
