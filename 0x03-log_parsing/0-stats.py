#!/usr/bin/python3
"""
log parsing
"""

from sys import stdin
import re
import sys

log_info = {"200": 0, "301": 0, "400": 0, "401": 0,
            "403": 0, "404": 0, "405": 0, "500": 0, "size": 0}


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
    if resource == '"GET /projects/260 HTTP/1.1"':
        check_n_add_status_code(code)
        add_size(size)


# def is_ip(val) -> bool:
#     """Check if the value is ip format."""
#     ip_check = re.compile(r"(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})")
#     if ip_check.match(val.strip()):
#         return True
#     return False


# def is_date(val) -> bool:
#     """Check pattern."""
#     pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]"
#     date_check = re.compile(pattern)
#     if date_check.match(val.strip()):
#         return True
#     return False


def check_n_add_status_code(val) -> bool:
    """check status code."""
    if log_info.get(val):
        log_info[val] = log_info.get(val) + 1
    else:
        log_info[val] = log_info.get(val) + 1


def add_size(val) -> None:
    """add filesize code."""
    log_info['size'] = log_info.get('size') + int(val)


def display() -> None:
    """display the info"""
    code_list = ["200", "301", "400", "401", "403", "404", "405", "500"]

    print(f"File size: {log_info.get('size')}")
    for i in code_list:
        res = log_info.get(i)
        if res:
            print(f"{i}: {res}")


def main() -> None:
    """
    Entry.
    """
    i = 0
    try:
        for line in stdin:
            tokenize(line)
            if i == 10:
                i = 0
                display()
            i += 1

    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        display()


if __name__ == '__main__':
    main()
