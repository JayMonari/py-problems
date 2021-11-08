import re


def abbreviate(words: str) -> str:
    acronym = ''
    for word in filter(lambda s: s != '', re.split("[^a-zA-Z0-9']", words)):
        acronym += word[0].capitalize()
    return acronym
