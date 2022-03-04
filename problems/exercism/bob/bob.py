def response(msg: str) -> str:
    def isyelling(s: str):
        return any(l for l in s if l.isalpha()) and s.upper() == s

    def isquestion(s: str): return s.strip()[-1] == '?'

    if not msg or msg.isspace():
        return "Fine. Be that way!"
    elif isyelling(msg) and isquestion(msg):
        return "Calm down, I know what I'm doing!"
    elif isyelling(msg):
        return "Whoa, chill out!"
    elif isquestion(msg):
        return "Sure."
    return "Whatever."
