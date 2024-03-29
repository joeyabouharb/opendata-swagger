# coding: utf-8

"""
    Trip Planner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.coord_request_response_location import CoordRequestResponseLocation  # noqa: F401,E501
from swagger_client.models.error_response import ErrorResponse  # noqa: F401,E501


class CoordRequestResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version': 'str',
        'error': 'ErrorResponse',
        'locations': 'list[CoordRequestResponseLocation]'
    }

    attribute_map = {
        'version': 'version',
        'error': 'error',
        'locations': 'locations'
    }

    def __init__(self, version=None, error=None, locations=None):  # noqa: E501
        """CoordRequestResponse - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._error = None
        self._locations = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if error is not None:
            self.error = error
        if locations is not None:
            self.locations = locations

    @property
    def version(self):
        """Gets the version of this CoordRequestResponse.  # noqa: E501

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.    # noqa: E501

        :return: The version of this CoordRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CoordRequestResponse.

        The version of the API that provided the response. Note that if this value is different to above, then the returned data may be different than expected. You can set the expected version using the `version` request parameter.    # noqa: E501

        :param version: The version of this CoordRequestResponse.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def error(self):
        """Gets the error of this CoordRequestResponse.  # noqa: E501

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :return: The error of this CoordRequestResponse.  # noqa: E501
        :rtype: ErrorResponse
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CoordRequestResponse.

        If an error has occurred, this element contains information about the error.   # noqa: E501

        :param error: The error of this CoordRequestResponse.  # noqa: E501
        :type: ErrorResponse
        """

        self._error = error

    @property
    def locations(self):
        """Gets the locations of this CoordRequestResponse.  # noqa: E501

        This contains a list of all of the stops, reload points and places of interest found based on the given request.   # noqa: E501

        :return: The locations of this CoordRequestResponse.  # noqa: E501
        :rtype: list[CoordRequestResponseLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this CoordRequestResponse.

        This contains a list of all of the stops, reload points and places of interest found based on the given request.   # noqa: E501

        :param locations: The locations of this CoordRequestResponse.  # noqa: E501
        :type: list[CoordRequestResponseLocation]
        """

        self._locations = locations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CoordRequestResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoordRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
