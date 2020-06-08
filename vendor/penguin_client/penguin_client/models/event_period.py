# coding: utf-8

"""
    Penguin Statistics - REST APIs

    Backend APIs for Arknights drop rate statistics website 'Penguin Statistics': https://penguin-stats.io/  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: alvissreimu@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventPeriod(object):
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
        'conditions': 'ExistConditions',
        'end': 'int',
        'existence': 'dict(str, Existence)',
        'label_i18n': 'dict(str, str)',
        'start': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'end': 'end',
        'existence': 'existence',
        'label_i18n': 'label_i18n',
        'start': 'start'
    }

    def __init__(self, conditions=None, end=None, existence=None, label_i18n=None, start=None):  # noqa: E501
        """EventPeriod - a model defined in Swagger"""  # noqa: E501

        self._conditions = None
        self._end = None
        self._existence = None
        self._label_i18n = None
        self._start = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if end is not None:
            self.end = end
        if existence is not None:
            self.existence = existence
        if label_i18n is not None:
            self.label_i18n = label_i18n
        if start is not None:
            self.start = start

    @property
    def conditions(self):
        """Gets the conditions of this EventPeriod.  # noqa: E501


        :return: The conditions of this EventPeriod.  # noqa: E501
        :rtype: ExistConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this EventPeriod.


        :param conditions: The conditions of this EventPeriod.  # noqa: E501
        :type: ExistConditions
        """

        self._conditions = conditions

    @property
    def end(self):
        """Gets the end of this EventPeriod.  # noqa: E501


        :return: The end of this EventPeriod.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EventPeriod.


        :param end: The end of this EventPeriod.  # noqa: E501
        :type: int
        """

        self._end = end

    @property
    def existence(self):
        """Gets the existence of this EventPeriod.  # noqa: E501


        :return: The existence of this EventPeriod.  # noqa: E501
        :rtype: dict(str, Existence)
        """
        return self._existence

    @existence.setter
    def existence(self, existence):
        """Sets the existence of this EventPeriod.


        :param existence: The existence of this EventPeriod.  # noqa: E501
        :type: dict(str, Existence)
        """

        self._existence = existence

    @property
    def label_i18n(self):
        """Gets the label_i18n of this EventPeriod.  # noqa: E501


        :return: The label_i18n of this EventPeriod.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._label_i18n

    @label_i18n.setter
    def label_i18n(self, label_i18n):
        """Sets the label_i18n of this EventPeriod.


        :param label_i18n: The label_i18n of this EventPeriod.  # noqa: E501
        :type: dict(str, str)
        """

        self._label_i18n = label_i18n

    @property
    def start(self):
        """Gets the start of this EventPeriod.  # noqa: E501


        :return: The start of this EventPeriod.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventPeriod.


        :param start: The start of this EventPeriod.  # noqa: E501
        :type: int
        """

        self._start = start

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
        if issubclass(EventPeriod, dict):
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
        if not isinstance(other, EventPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other