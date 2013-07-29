from flake8.main import Flake8Command


class test_flake8 (Flake8Command):
    def run(self):
        try:
            Flake8Command.run(self)
        except SystemExit, e:
            if e.args != (0,):
                raise
            # Otherwise continue with other setup.py commands.
