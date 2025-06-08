    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes in this list are included.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary with selected instance attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                a: getattr(self, a)
                for a in attrs
                if hasattr(self, a)
            }
        return self.__dict__.copy()
