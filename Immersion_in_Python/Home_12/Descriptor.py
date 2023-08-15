class DescriptorName:
    """
    Descriptor to check name for first capital letter and
    the presence of only letters.
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value: str):
        if value.istitle() and value.isalpha():
            instance.__dict__[self.name] = value
        else:
            if not value.istitle():
                raise ValueError('You have to use capital letter first of all')
            elif not value.isalpha():
                raise ValueError('You have to use only letters')
