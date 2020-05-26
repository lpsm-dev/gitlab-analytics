# -*- coding: utf-8 -*-

class ClientException(Exception):
    pass

class URLException(ClientException):
    pass

class URLTypeException(ClientException):
    pass

class InvalidURL(ClientException):
    pass

class RequestGetStatusException(ClientException):
    pass

class RequestGetException(ClientException):
    pass
