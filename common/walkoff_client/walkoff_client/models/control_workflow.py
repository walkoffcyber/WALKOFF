# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ControlWorkflow(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'trigger_data': 'str',
        'trigger_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'trigger_data': 'trigger_data',
        'trigger_id': 'trigger_id'
    }

    def __init__(self, status=None, trigger_data=None, trigger_id=None):  # noqa: E501
        """ControlWorkflow - a model defined in OpenAPI"""  # noqa: E501

        self._status = None
        self._trigger_data = None
        self._trigger_id = None
        self.discriminator = None

        self.status = status
        if trigger_data is not None:
            self.trigger_data = trigger_data
        if trigger_id is not None:
            self.trigger_id = trigger_id

    @property
    def status(self):
        """Gets the status of this ControlWorkflow.  # noqa: E501

        The action to take on the executing workflow  # noqa: E501

        :return: The status of this ControlWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ControlWorkflow.

        The action to take on the executing workflow  # noqa: E501

        :param status: The status of this ControlWorkflow.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["trigger", "abort"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def trigger_data(self):
        """Gets the trigger_data of this ControlWorkflow.  # noqa: E501

        The data that will be sent to the trigger  # noqa: E501

        :return: The trigger_data of this ControlWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._trigger_data

    @trigger_data.setter
    def trigger_data(self, trigger_data):
        """Sets the trigger_data of this ControlWorkflow.

        The data that will be sent to the trigger  # noqa: E501

        :param trigger_data: The trigger_data of this ControlWorkflow.  # noqa: E501
        :type: str
        """

        self._trigger_data = trigger_data

    @property
    def trigger_id(self):
        """Gets the trigger_id of this ControlWorkflow.  # noqa: E501

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :return: The trigger_id of this ControlWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """Sets the trigger_id of this ControlWorkflow.

        A 32-bit hexadecimal string representing a globally unique identifier  # noqa: E501

        :param trigger_id: The trigger_id of this ControlWorkflow.  # noqa: E501
        :type: str
        """

        self._trigger_id = trigger_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ControlWorkflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
