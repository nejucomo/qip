class DescriptionFromDocProperty (property):
    def __get__(self, _, cls):
        return cls.__doc__


class QipCommandBase (Command):
    """Utility for no options and delegate description to the subclass __doc__."""

    description = DescriptionFromDocProperty()

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass



