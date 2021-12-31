import logging
from urllib.parse import urlparse

from rich.prompt import Prompt
from utils.module_loading import cached_import


def confirm(question, color="cyan"):
    response = Prompt.ask(f"[{color}]{question} (y/N)#[/{color}]")
    return response.lower() in ["y", "yes"]


def basic_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())
    return logger


class URL:
    url = None

    def __init__(self, url):
        if isinstance(url, URL):
            self.url = url.url
            return
        try:
            parsed = urlparse(url)
            self.url = url
            assert all([parsed.scheme, parsed.netloc])
        except (ValueError, AssertionError):
            raise ValueError(f"{url} could not be parsed as a valid url")

    def __str__(self):
        return str(self.url)


class LogLevel:
    level = "DEBUG"

    def __init__(self, level):
        if isinstance(level, LogLevel):
            self.level = level.level
            return
        try:
            cached_import("logging", level)
            self.level = level
        except AttributeError:
            raise ValueError(f"{level} could not be parsed as a valid log level.")

    def __str__(self):
        return str(self.level)