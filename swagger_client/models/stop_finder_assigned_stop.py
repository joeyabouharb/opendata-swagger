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

from swagger_client.models.parent_location import ParentLocation  # noqa: F401,E501


class StopFinderAssignedStop(object):
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
        'duration': 'int',
        'distance': 'int',
        'coord': 'list[float]',
        'parent': 'ParentLocation',
        'type': 'str',
        'modes': 'list[int]',
        'connecting_mode': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'disassembled_name': 'disassembledName',
        'duration': 'duration',
        'distance': 'distance',
        'coord': 'coord',
        'parent': 'parent',
        'type': 'type',
        'modes': 'modes',
        'connecting_mode': 'connectingMode'
    }

    def __init__(self, id=None, name=None, disassembled_name=None, duration=None, distance=None, coord=None, parent=None, type=None, modes=None, connecting_mode=None):  # noqa: E501
        """StopFinderAssignedStop - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._disassembled_name = None
        self._duration = None
        self._distance = None
        self._coord = None
        self._parent = None
        self._type = None
        self._modes = None
        self._connecting_mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if disassembled_name is not None:
            self.disassembled_name = disassembled_name
        if duration is not None:
            self.duration = duration
        if distance is not None:
            self.distance = distance
        if coord is not None:
            self.coord = coord
        if parent is not None:
            self.parent = parent
        if type is not None:
            self.type = type
        if modes is not None:
            self.modes = modes
        if connecting_mode is not None:
            self.connecting_mode = connecting_mode

    @property
    def id(self):
        """Gets the id of this StopFinderAssignedStop.  # noqa: E501

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `XML_STOPFINDER_REQUEST`, or can be used as the origin or destination in an `XML_TRIP_REQUEST2` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :return: The id of this StopFinderAssignedStop.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StopFinderAssignedStop.

        This is a unique ID for the returned location. Certain types of ID can be used for subsequent searches performed with `XML_STOPFINDER_REQUEST`, or can be used as the origin or destination in an `XML_TRIP_REQUEST2` request. The format of a location ID differs greatly, depending on the type of location it is.   # noqa: E501

        :param id: The id of this StopFinderAssignedStop.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StopFinderAssignedStop.  # noqa: E501

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :return: The name of this StopFinderAssignedStop.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StopFinderAssignedStop.

        This is the long version of the location name, which may include the suburb or other information.   # noqa: E501

        :param name: The name of this StopFinderAssignedStop.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def disassembled_name(self):
        """Gets the disassembled_name of this StopFinderAssignedStop.  # noqa: E501

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :return: The disassembled_name of this StopFinderAssignedStop.  # noqa: E501
        :rtype: str
        """
        return self._disassembled_name

    @disassembled_name.setter
    def disassembled_name(self, disassembled_name):
        """Sets the disassembled_name of this StopFinderAssignedStop.

        This is the short version of the location name, which does not include the suburb or other information.   # noqa: E501

        :param disassembled_name: The disassembled_name of this StopFinderAssignedStop.  # noqa: E501
        :type: str
        """

        self._disassembled_name = disassembled_name

    @property
    def duration(self):
        """Gets the duration of this StopFinderAssignedStop.  # noqa: E501

        This is the number of minutes it would take to reach this stop from the location to which it is assigned.  # noqa: E501

        :return: The duration of this StopFinderAssignedStop.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this StopFinderAssignedStop.

        This is the number of minutes it would take to reach this stop from the location to which it is assigned.  # noqa: E501

        :param duration: The duration of this StopFinderAssignedStop.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def distance(self):
        """Gets the distance of this StopFinderAssignedStop.  # noqa: E501

        This is the distance in metres to this stop from the location to which it is assigned.  # noqa: E501

        :return: The distance of this StopFinderAssignedStop.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this StopFinderAssignedStop.

        This is the distance in metres to this stop from the location to which it is assigned.  # noqa: E501

        :param distance: The distance of this StopFinderAssignedStop.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def coord(self):
        """Gets the coord of this StopFinderAssignedStop.  # noqa: E501

        Contains exactly two values: the first value is the latitude, the second value is the longitude.   # noqa: E501

        :return: The coord of this StopFinderAssignedStop.  # noqa: E501
        :rtype: list[float]
        """
        return self._coord

    @coord.setter
    def coord(self, coord):
        """Sets the coord of this StopFinderAssignedStop.

        Contains exactly two values: the first value is the latitude, the second value is the longitude.   # noqa: E501

        :param coord: The coord of this StopFinderAssignedStop.  # noqa: E501
        :type: list[float]
        """

        self._coord = coord

    @property
    def parent(self):
        """Gets the parent of this StopFinderAssignedStop.  # noqa: E501

        If available, contains information about this location's parent location. For example, if the stop has a type of `platform`, then this field may contain information about the station in which the platform is located.   # noqa: E501

        :return: The parent of this StopFinderAssignedStop.  # noqa: E501
        :rtype: ParentLocation
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this StopFinderAssignedStop.

        If available, contains information about this location's parent location. For example, if the stop has a type of `platform`, then this field may contain information about the station in which the platform is located.   # noqa: E501

        :param parent: The parent of this StopFinderAssignedStop.  # noqa: E501
        :type: ParentLocation
        """

        self._parent = parent

    @property
    def type(self):
        """Gets the type of this StopFinderAssignedStop.  # noqa: E501

        A value of `unknown` likely indicates bad data. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :return: The type of this StopFinderAssignedStop.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StopFinderAssignedStop.

        A value of `unknown` likely indicates bad data. If a location is returned with this type, you can safely ignore it.   # noqa: E501

        :param type: The type of this StopFinderAssignedStop.  # noqa: E501
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
    def modes(self):
        """Gets the modes of this StopFinderAssignedStop.  # noqa: E501

        This is included only if the `type` value is set to `stop`. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * `1`: Train * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus   # noqa: E501

        :return: The modes of this StopFinderAssignedStop.  # noqa: E501
        :rtype: list[int]
        """
        return self._modes

    @modes.setter
    def modes(self, modes):
        """Sets the modes of this StopFinderAssignedStop.

        This is included only if the `type` value is set to `stop`. Contains a list of modes of transport that service this stop. This can be useful for showing relevant wayfinding icons when presenting users with a list of matching stops to choose from.  The following values may be present:  * `1`: Train * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus   # noqa: E501

        :param modes: The modes of this StopFinderAssignedStop.  # noqa: E501
        :type: list[int]
        """

        self._modes = modes

    @property
    def connecting_mode(self):
        """Gets the connecting_mode of this StopFinderAssignedStop.  # noqa: E501

        This is the mode of transport that is used to connect to this stop. The following values are available:  * `1`: Train * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus * `97`: Remain On-Board * `99`: Walking * `100`: Walking * `105`: Driving   # noqa: E501

        :return: The connecting_mode of this StopFinderAssignedStop.  # noqa: E501
        :rtype: int
        """
        return self._connecting_mode

    @connecting_mode.setter
    def connecting_mode(self, connecting_mode):
        """Sets the connecting_mode of this StopFinderAssignedStop.

        This is the mode of transport that is used to connect to this stop. The following values are available:  * `1`: Train * `4`: Light Rail * `5`: Bus * `7`: Coach * `9`: Ferry * `11`: School Bus * `97`: Remain On-Board * `99`: Walking * `100`: Walking * `105`: Driving   # noqa: E501

        :param connecting_mode: The connecting_mode of this StopFinderAssignedStop.  # noqa: E501
        :type: int
        """

        self._connecting_mode = connecting_mode

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
        if issubclass(StopFinderAssignedStop, dict):
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
        if not isinstance(other, StopFinderAssignedStop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
