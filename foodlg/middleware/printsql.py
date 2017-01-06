"""
"""
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings
from django.db import connection


class SQLPrintingMiddleware(object):
    """
    https://gist.github.com/vstoykov/1390853
    Middleware which prints out a list of all SQL queries done
    for each view that is processed. This is only useful for debugging.
    """
    def __init__(self):
        if not settings.DEBUG:
            raise MiddlewareNotUsed

    def process_response(self, request, response):
        if (len(connection.queries) == 0 or
            request.path_info.startswith('/favicon.ico') or
            request.path_info.startswith(settings.STATIC_URL)):
            return response
        indentation = 2
        print "\n%s\033[SQL Queries for]\033 %s\033\n" % (" " * indentation, request.path_info)
        total_time = 0.0
        for query in connection.queries:
            nice_sql = query['sql'].replace('"', '').replace(',', ', ')
            sql = "\033[%s]\033 %s" % (query['time'], nice_sql)
            total_time = total_time + float(query['time'])
            print "%s%s" % (" " * indentation, sql)
        replace_tuple = (" " * indentation, str(total_time), str(len(connection.queries)))
        print "\n%s\033[TOTAL TIME: %s seconds (%s queries)]\033" % replace_tuple
        return response