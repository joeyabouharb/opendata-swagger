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

from swagger_client.models.trip_request_response_journey_leg_stop_footpath_info_footpath_elem import TripRequestResponseJourneyLegStopFootpathInfoFootpathElem  # noqa: F401,E501


class TripRequestResponseJourneyLegStopFootpathInfo(object):
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
        'position': 'str',
        'duration': 'int',
        'foot_path_elem': 'list[TripRequestResponseJourneyLegStopFootpathInfoFootpathElem]'
    }

    attribute_map = {
        'position': 'position',
        'duration': 'duration',
        'foot_path_elem': 'footPathElem'
    }

    def __init__(self, position=None, duration=None, foot_path_elem=None):  # noqa: E501
        """TripRequestResponseJourneyLegStopFootpathInfo - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._duration = None
        self._foot_path_elem = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if duration is not None:
            self.duration = duration
        if foot_path_elem is not None:
            self.foot_path_elem = foot_path_elem

    @property
    def position(self):
        """Gets the position of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501

        This indicates where in the leg the walking part of this legs occurs, since for some legs this is included with transportation on a vehicle.   # noqa: E501

        :return: The position of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TripRequestResponseJourneyLegStopFootpathInfo.

        This indicates where in the leg the walking part of this legs occurs, since for some legs this is included with transportation on a vehicle.   # noqa: E501

        :param position: The position of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["AFTER", "IDEST"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def duration(self):
        """Gets the duration of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501

        This is approximately how long in seconds the walking instructions contained in this element take to perform.   # noqa: E501

        :return: The duration of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TripRequestResponseJourneyLegStopFootpathInfo.

        This is approximately how long in seconds the walking instructions contained in this element take to perform.   # noqa: E501

        :param duration: The duration of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def foot_path_elem(self):
        """Gets the foot_path_elem of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501

        This describes the specific instructions for the walking leg.   # noqa: E501

        :return: The foot_path_elem of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :rtype: list[TripRequestResponseJourneyLegStopFootpathInfoFootpathElem]
        """
        return self._foot_path_elem

    @foot_path_elem.setter
    def foot_path_elem(self, foot_path_elem):
        """Sets the foot_path_elem of this TripRequestResponseJourneyLegStopFootpathInfo.

        This describes the specific instructions for the walking leg.   # noqa: E501

        :param foot_path_elem: The foot_path_elem of this TripRequestResponseJourneyLegStopFootpathInfo.  # noqa: E501
        :type: list[TripRequestResponseJourneyLegStopFootpathInfoFootpathElem]
        """

        self._foot_path_elem = foot_path_elem

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
        if issubclass(TripRequestResponseJourneyLegStopFootpathInfo, dict):
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
        if not isinstance(other, TripRequestResponseJourneyLegStopFootpathInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
