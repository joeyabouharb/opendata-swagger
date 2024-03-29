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


class ParentLocation(object):
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
        'id': 'str',
        'name': 'str',
        'disassembled_name': 'str',
        'type': 'str',
        'parent': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disassembled_name': 'disassembledName',
        'type': 'type',
        'parent': 'parent'
    }

    def __init__(self, id=None, name=None, disassembled_name=None, type=None, parent=None):  # noqa: E501
        """ParentLocation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._disassembled_name = None
        self._type = None
        self._parent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disassembled_name is not None:
            self.disassembled_name = disassembled_name
        if type is not None:
            self.type = type
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this ParentLocation.  # noqa: E501

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `XML_STOPFINDER_REQUEST`, or can be used as the origin or destination in an `XML_TRIP_REQUEST2` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :return: The id of this ParentLocation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParentLocation.

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `XML_STOPFINDER_REQUEST`, or can be used as the origin or destination in an `XML_TRIP_REQUEST2` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :param id: The id of this ParentLocation.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ParentLocation.  # noqa: E501

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :return: The name of this ParentLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParentLocation.

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :param name: The name of this ParentLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def disassembled_name(self):
        """Gets the disassembled_name of this ParentLocation.  # noqa: E501

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :return: The disassembled_name of this ParentLocation.  # noqa: E501
        :rtype: str
        """
        return self._disassembled_name

    @disassembled_name.setter
    def disassembled_name(self, disassembled_name):
        """Sets the disassembled_name of this ParentLocation.

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :param disassembled_name: The disassembled_name of this ParentLocation.  # noqa: E501
        :type: str
        """

        self._disassembled_name = disassembled_name

    @property
    def type(self):
        """Gets the type of this ParentLocation.  # noqa: E501

        This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody's house. A value of `unknown` likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :return: The type of this ParentLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ParentLocation.

        This is the type of location being returned. It may represent a stop or platform that a public transport service physically stops at for passenger boarding, or it may represent somebody's house. A value of `unknown` likely indicates bad data coming from the server. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :param type: The type of this ParentLocation.  # noqa: E501
        :type: str
        """
        allowed_values = ["poi", "singlehouse", "stop", "platform", "street", "locality", "location", "unknown"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def parent(self):
        """Gets the parent of this ParentLocation.  # noqa: E501

        In some cases, a parent location will also contain its parent (in other words, the grandparent of the initial location)   # noqa: E501

        :return: The parent of this ParentLocation.  # noqa: E501
        :rtype: object
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ParentLocation.

        In some cases, a parent location will also contain its parent (in other words, the grandparent of the initial location)   # noqa: E501

        :param parent: The parent of this ParentLocation.  # noqa: E501
        :type: object
        """

        self._parent = parent

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
        if issubclass(ParentLocation, dict):
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
        if not isinstance(other, ParentLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
