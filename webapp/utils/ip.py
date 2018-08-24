import re


def is_ip(strings):
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')

    if pattern.match(strings):
        return True
    else:
        return False

