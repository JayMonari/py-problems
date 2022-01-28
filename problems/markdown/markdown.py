import re


class Pattern:
    BOLD = r'__([^\n]+?)__'
    ITALIC = r'_([^\n]+?)_'
    LIST_ELE = r'^\* (.*?$)'
    FULL_LIST = '(<li>.*</li>)'
    NOT_START_TAG = '^(?!<[hlu])(.*?$)'

def make_tag(tag: str) -> str:
    return fr"<{tag}>\1</{tag}>"


def parse(markdown: str) -> str:
    html = markdown
    html = re.sub(Pattern.BOLD, make_tag("strong"), html)
    html = re.sub(Pattern.ITALIC, make_tag("em"), html)
    html = re.sub(Pattern.LIST_ELE, make_tag("li"), html, flags=re.M)
    html = re.sub(Pattern.FULL_LIST, make_tag("ul"), html, flags=re.S)
    for n in range(6, 0, -1):
        header_val = f"^{'#' * n} (.*?$)"
        html = re.sub(header_val, make_tag(f"h{n}"), html, flags=re.M)
    html = re.sub(Pattern.NOT_START_TAG, make_tag('p'), html, flags=re.M)
    html = re.sub(r'\n', '', html)
    return html
