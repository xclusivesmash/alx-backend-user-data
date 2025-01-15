#!/usr/bin/env python3
"""
module: filtered_logger
description: return a log message obfuscated.
"""
import re
from typing import List


def filter_datum(
        field: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ @description
    Args:
        field (List[str]): all fields to obfuscate.
        redaction (str): by what the field will be obfuscated.
        message (str): log line.
        separator (str): character seperator.
    Returns:
        Filtered string msg with redacted values.
    """
    for f in field:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
