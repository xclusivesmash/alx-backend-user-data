#!/usr/bin/env python3
"""
module: filtered_logger
description: return a log message obfuscated.
"""
import re
from typing import List
import logging
from os import environ
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(field: List[str], redaction: str,
                 message: str, separator: str) -> str:
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


def get_logger() -> logging.Logger:
    """ Implements a logger object.
    Returns:
        a logger in the required format.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connects to a mysql database securely.
    """
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")
    connection = mysql.connector.connection.MySQLConnection(
            user=username,
            password=password,
            host=host,
            database=db_name)
    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize
        Args:
            fields (List[str]): fields to replace.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Returns a log messages parsed in the req. fmt.
        Args:
            record (logging.LogRecord): log record to parse.
        Returns:
            log message in the required format.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
