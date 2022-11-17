""" import regrex tools """
import re


class BaseRegEx:
    """Basic regrex replacing class"""

    regex = r""
    replace_token = "<GENERIC_TOKEN>"

    def preprocess(self, text):
        """carry out preprocess operation"""
        return re.sub(self.regex, self.replace_token, text)


class RegExRemovePunkt(BaseRegEx):
    """Replace puctuation"""

    regex = r"\W"
    replace_token = ""


class RegExReplaceNumberLike(BaseRegEx):
    """Repalce number"""

    regex = r"(?:\d+.)+"
    replace_token = " <NUMERIC_VALUE> "


class RegExReplacePhone(BaseRegEx):
    """Replace phone number"""

    regex = r"(?:\+[0-9]+)*\s*[0-9]{0,5}\s*[0-9]{3,5}\-[0-9]{3,5}"
    replace_token = " <PHONE_NUMBER> "


class RegExReplaceEMail(BaseRegEx):
    """Replace Email"""

    regex = r"\w+\@\w+(?:\.\w+)+"
    replace_token = " <EMAIL> "


class Lowercase:
    """Render text lowercase"""

    def preprocess(self, text):
        """Overwrite to make text lower case"""
        return text.lower()
