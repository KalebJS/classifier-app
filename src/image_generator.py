from pathlib import Path


class ImageGenerator:
    def __init__(self, image_folder: Path, image_suffix: str = ".jpg"):
        self.dir = image_folder
        self.images = self.dir.glob(f"*{image_suffix}")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.images)
        except StopIteration as e:
            raise StopIteration("No more images") from e
