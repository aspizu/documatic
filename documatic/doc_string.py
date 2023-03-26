class DocString:
    """A class for parsing and storing information from a docstring."""

    def __init__(self, doc: str, attributes: dict[str, str] | None = None):
        """Parse a google formatted doc-string.

        Args:
          doc: The docstring to be parsed.
          attributes: A dictionary of additional attributes. Defaults to None.
        """
        self.summary = None
        """The summary of the docstring, which is the first line of the docstring."""
        self.description = None
        """The description of the docstring, which is everything after the summary."""
        self.attributes: dict[str, str] = attributes or {}
        """A dictionary of the attributes specified in the docstring."""
        self.arguments: dict[str, str] = {}
        """A dictionary of the arguments specified in the docstring."""
        self.returns = None
        """The description of the return value specified in the docstring."""
        self.exceptions: dict[str, str] = {}
        """A dictionary of the exceptions specified in the docstring."""

        self.parse(doc)

    def parse(self, doc: str):
        codeblock = False
        collector = None
        for line in (doc + "\n\n").splitlines():
            if collector is not None:
                if line[:2] != "  ":
                    collector = None
                    continue
                if collector in ("Attributes:", "Args:", "Raises:"):
                    name, desc = line[2:].split(": ")
                    {
                        "Attributes:": self.attributes,
                        "Args:": self.arguments,
                        "Raises:": self.exceptions,
                    }[collector][name] = desc
                elif collector == "Returns:":
                    if self.returns is None:
                        self.returns = line
                    else:
                        self.returns += "\n" + line
            elif line in ("Attributes:", "Args:", "Raises:", "Returns:"):
                collector = line
            else:
                if self.description is None:
                    self.description = ""
                if line.lstrip().startswith(">>>") or line.lstrip().startswith("..."):
                    if not codeblock:
                        codeblock = True
                        self.description += "```py\n"
                else:
                    if codeblock:
                        codeblock = False
                        self.description += "```\n"
                if codeblock:
                    self.description += line.lstrip() + "\n"
                else:
                    self.description += line + "\n"
        if self.description:
            self.description = self.description[:-1]

        if self.description:
            self.summary = self.description.splitlines()[0]
            self.description = self.description[len(self.summary) :]
