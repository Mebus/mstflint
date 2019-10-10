#######################################################
#
# InfoSegment.py
# Python implementation of the Class InfoSegment
# Generated by Enterprise Architect
# Created on:      14-Aug-2019 10:11:57 AM
# Original author: talve
#
#######################################################
from segments.Segment import Segment
from segments.SegmentFactory import SegmentFactory
from utils import constants


class InfoSegment(Segment):
    """this class is responsible for holding info segment data.
    """

    def __init__(self, data):
        """initialize the class by setting the class data.
        """
        self.raw_data = data

    def get_data(self):
        """get the general segment data.
        """
        return self.raw_data

    def get_type(self):
        """get the general segment type.
        """
        return constants.RESOURCE_DUMP_SEGMENT_TYPE_INFO


SegmentFactory.register(constants.RESOURCE_DUMP_SEGMENT_TYPE_INFO, InfoSegment)
