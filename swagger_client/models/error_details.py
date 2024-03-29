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


class ErrorDetails(object):
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
        'transaction_id': 'str',
        'error_date_time': 'str',
        'message': 'str',
        'requested_url': 'str',
        'requested_method': 'str'
    }

    attribute_map = {
        'transaction_id': 'TransactionId',
        'error_date_time': 'ErrorDateTime',
        'message': 'Message',
        'requested_url': 'RequestedUrl',
        'requested_method': 'RequestedMethod'
    }

    def __init__(self, transaction_id=None, error_date_time=None, message=None, requested_url=None, requested_method=None):  # noqa: E501
        """ErrorDetails - a model defined in Swagger"""  # noqa: E501

        self._transaction_id = None
        self._error_date_time = None
        self._message = None
        self._requested_url = None
        self._requested_method = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.error_date_time = error_date_time
        self.message = message
        self.requested_url = requested_url
        self.requested_method = requested_method

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ErrorDetails.  # noqa: E501


        :return: The transaction_id of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ErrorDetails.


        :param transaction_id: The transaction_id of this ErrorDetails.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def error_date_time(self):
        """Gets the error_date_time of this ErrorDetails.  # noqa: E501


        :return: The error_date_time of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._error_date_time

    @error_date_time.setter
    def error_date_time(self, error_date_time):
        """Sets the error_date_time of this ErrorDetails.


        :param error_date_time: The error_date_time of this ErrorDetails.  # noqa: E501
        :type: str
        """
        if error_date_time is None:
            raise ValueError("Invalid value for `error_date_time`, must not be `None`")  # noqa: E501

        self._error_date_time = error_date_time

    @property
    def message(self):
        """Gets the message of this ErrorDetails.  # noqa: E501


        :return: The message of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetails.


        :param message: The message of this ErrorDetails.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def requested_url(self):
        """Gets the requested_url of this ErrorDetails.  # noqa: E501


        :return: The requested_url of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._requested_url

    @requested_url.setter
    def requested_url(self, requested_url):
        """Sets the requested_url of this ErrorDetails.


        :param requested_url: The requested_url of this ErrorDetails.  # noqa: E501
        :type: str
        """
        if requested_url is None:
            raise ValueError("Invalid value for `requested_url`, must not be `None`")  # noqa: E501

        self._requested_url = requested_url

    @property
    def requested_method(self):
        """Gets the requested_method of this ErrorDetails.  # noqa: E501


        :return: The requested_method of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._requested_method

    @requested_method.setter
    def requested_method(self, requested_method):
        """Sets the requested_method of this ErrorDetails.


        :param requested_method: The requested_method of this ErrorDetails.  # noqa: E501
        :type: str
        """
        if requested_method is None:
            raise ValueError("Invalid value for `requested_method`, must not be `None`")  # noqa: E501

        self._requested_method = requested_method

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
        if issubclass(ErrorDetails, dict):
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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
