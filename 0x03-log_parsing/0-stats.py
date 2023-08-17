#!/usr/bin/python3
"""
log parsing
"""

from sys import stdin
import re

log_info = {}


def tokenize(line):
    """Tokenize the line"""
    res = line.split("-", 1)
    if len(res) < 2:
        return
    ip, line = res
    res = re.split(r"(?<=]) ", line)
    if len(res) < 2:
        return
    date, line = res
    res = re.split(r'(?<=") ', line)
    if len(res) < 2:
        return
    resource, line = res
    res = line.split(" ")
    if len(res) < 2:
        return
    code, size = res
    if is_ip(ip) and is_date(date) \
            and resource == '"GET /projects/260 HTTP/1.1"':
        check_n_add_status_code(code)
        add_size(size)


def is_ip(val) -> bool:
    """Check if the value is ip format."""
    ip_check = re.compile(r"(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})")
    if ip_check.match(val.strip()):
        return True
    return False


def is_date(val) -> bool:
    """Check pattern."""
    pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]"
    date_check = re.compile(pattern)
    if date_check.match(val.strip()):
        return True
    return False


def check_n_add_status_code(val) -> bool:
    """check status code."""
    acceptable = [200, 301, 400, 401, 403, 404, 405, 500]
    if int(val) in acceptable:
        log_info[val] = (log_info.get(val) or 0) + 1


def add_size(val) -> None:
    """add filesize code."""
    log_info['file_size'] = (log_info.get('file_size') or 0) + int(val)


def display() -> None:
    """display the info"""
    code_list = [200, 301, 400, 401, 403, 404, 405, 500]

    print(f"File size: {log_info.get('file_size')}")
    for i in code_list:
        res = log_info.get(str((i)))
        if res:
            print(f"{i}: {res}")


def main() -> None:
    """
    Entry.
    """
    i = 0
    for line in stdin:
        tokenize(line)
        if i % 10 == 0:
            display()
        i += 1


if __name__ == '__main__':
    main()
