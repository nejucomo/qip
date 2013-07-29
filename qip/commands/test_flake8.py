from flake8.main import Flake8Command


class QipFlake8Command (Flake8Command):
    def run(self):
        try:
            Flake8Command.run(self)
        except SystemExit, e:
            if e.args != (0,):
                raise
            # Otherwise continue with other setup.py commands.
