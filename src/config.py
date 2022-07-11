from pathlib import Path

cwd = Path.cwd()


class Config:

    class Paths:
        ROOT = cwd

        class Static:
            ROOT = cwd / "static"

            class Images:
                ROOT = cwd / "static" / "images"
