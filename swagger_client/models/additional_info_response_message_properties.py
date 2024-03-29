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

from swagger_client.models.additional_info_response_message_properties_source import AdditionalInfoResponseMessagePropertiesSource  # noqa: F401,E501


class AdditionalInfoResponseMessageProperties(object):
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
        'sms_text': 'str',
        'source': 'AdditionalInfoResponseMessagePropertiesSource'
    }

    attribute_map = {
        'sms_text': 'smsText',
        'source': 'source'
    }

    def __init__(self, sms_text=None, source=None):  # noqa: E501
        """AdditionalInfoResponseMessageProperties - a model defined in Swagger"""  # noqa: E501

        self._sms_text = None
        self._source = None
        self.discriminator = None

        if sms_text is not None:
            self.sms_text = sms_text
        if source is not None:
            self.source = source

    @property
    def sms_text(self):
        """Gets the sms_text of this AdditionalInfoResponseMessageProperties.  # noqa: E501

        This is a plaintext summary of the alert content, although note that it may contain HTML entities such as &nbsp;.   # noqa: E501

        :return: The sms_text of this AdditionalInfoResponseMessageProperties.  # noqa: E501
        :rtype: str
        """
        return self._sms_text

    @sms_text.setter
    def sms_text(self, sms_text):
        """Sets the sms_text of this AdditionalInfoResponseMessageProperties.

        This is a plaintext summary of the alert content, although note that it may contain HTML entities such as &nbsp;.   # noqa: E501

        :param sms_text: The sms_text of this AdditionalInfoResponseMessageProperties.  # noqa: E501
        :type: str
        """

        self._sms_text = sms_text

    @property
    def source(self):
        """Gets the source of this AdditionalInfoResponseMessageProperties.  # noqa: E501


        :return: The source of this AdditionalInfoResponseMessageProperties.  # noqa: E501
        :rtype: AdditionalInfoResponseMessagePropertiesSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AdditionalInfoResponseMessageProperties.


        :param source: The source of this AdditionalInfoResponseMessageProperties.  # noqa: E501
        :type: AdditionalInfoResponseMessagePropertiesSource
        """

        self._source = source

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
        if issubclass(AdditionalInfoResponseMessageProperties, dict):
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
        if not isinstance(other, AdditionalInfoResponseMessageProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
