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

from swagger_client.models.trip_request_response_journey_leg_stop_footpath_info_footpath_elem_location_location import TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation  # noqa: F401,E501


class TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation(object):
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
        'location': 'TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation',
        'area': 'int',
        'platform': 'int',
        'georef': 'str'
    }

    attribute_map = {
        'location': 'location',
        'area': 'area',
        'platform': 'platform',
        'georef': 'georef'
    }

    def __init__(self, location=None, area=None, platform=None, georef=None):  # noqa: E501
        """TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation - a model defined in Swagger"""  # noqa: E501

        self._location = None
        self._area = None
        self._platform = None
        self._georef = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if area is not None:
            self.area = area
        if platform is not None:
            self.platform = platform
        if georef is not None:
            self.georef = georef

    @property
    def location(self):
        """Gets the location of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501


        :return: The location of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :rtype: TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.


        :param location: The location of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :type: TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocationLocation
        """

        self._location = location

    @property
    def area(self):
        """Gets the area of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501

        XXX  # noqa: E501

        :return: The area of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :rtype: int
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.

        XXX  # noqa: E501

        :param area: The area of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :type: int
        """

        self._area = area

    @property
    def platform(self):
        """Gets the platform of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501

        If available, this is a platform number that relates to this instruction. It defaults to `0` if there is no such information available.   # noqa: E501

        :return: The platform of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :rtype: int
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.

        If available, this is a platform number that relates to this instruction. It defaults to `0` if there is no such information available.   # noqa: E501

        :param platform: The platform of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :type: int
        """

        self._platform = platform

    @property
    def georef(self):
        """Gets the georef of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501

        This is an identifier for this particular instruction / location, based on its location.   # noqa: E501

        :return: The georef of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :rtype: str
        """
        return self._georef

    @georef.setter
    def georef(self, georef):
        """Sets the georef of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.

        This is an identifier for this particular instruction / location, based on its location.   # noqa: E501

        :param georef: The georef of this TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation.  # noqa: E501
        :type: str
        """

        self._georef = georef

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
        if issubclass(TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation, dict):
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
        if not isinstance(other, TripRequestResponseJourneyLegStopFootpathInfoFootpathElemLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
