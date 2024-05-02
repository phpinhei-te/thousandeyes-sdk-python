# coding: utf-8

# flake8: noqa
"""
    OAuth2 API

    This endpoint allows clients to trade their client credentials for an Access Token that can be used on subsequent calls to our API. Example of usage:    `   curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -d 'client_id=someId&scope=someScope&client_secret=someSecret&grant_type=client_credentials' 'https://api.thousandeyes.com/v7/oauth2/token'   `

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from oauth2.models.access_token import AccessToken
from oauth2.models.error import Error
from oauth2.models.unauthorized_error import UnauthorizedError
from oauth2.models.validation_error import ValidationError
from oauth2.models.validation_error_all_of_errors import ValidationErrorAllOfErrors
