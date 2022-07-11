import os.path
from pathlib import Path

from flask import Blueprint, render_template, request

from src.config import Config
from src.image_generator import ImageGenerator
from src.models import FormResponse

bp = Blueprint('classifier', __name__)
images = ImageGenerator(Config.Paths.Static.Images.ROOT)
image = next(images)


@bp.route("/", methods=["GET", "POST"])
def index():
    global image
    if request.method == "POST":
        try:
            response = FormResponse(**request.form)
            # do something with response
            image = next(images)
        except StopIteration:
            return "No more images! You're done."

    return render_template(
        template_name_or_list="classifier/index.html",
        filename=image.name,
        relpath=os.path.relpath(image, Path.cwd()),
    )
