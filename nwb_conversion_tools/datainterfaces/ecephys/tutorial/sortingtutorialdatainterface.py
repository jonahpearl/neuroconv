"""Authors: Cody Baker and Ben Dichter."""
import spikeextractors as se

from ....utils.json_schema import get_schema_from_method_signature
from ..basesortingextractorinterface import BaseSortingExtractorInterface


class SortingTutorialInterface(BaseSortingExtractorInterface):
    """Sorting data interface for demonstrating NWB Conversion Tools usage in tutorials."""

    SX = se.NumpySortingExtractor

    @classmethod
    def get_source_schema(cls):
        source_schema = get_schema_from_method_signature(se.example_datasets.toy_example)
        source_schema["additionalProperties"] = True
        return source_schema

    def __init__(self, **source_data):
        self.sorting_extractor = se.example_datasets.toy_example(**source_data)[1]
        
        # Set manual group names at the recording extractor level
        for channel_id in self.recording_extractor.get_channel_ids():
            self.recording_extractor.set_channel_property(
                channel_id=channel_id,
                property_name="group_name",
                value="ElectrodeGroup"
            )

    def get_metadata(self):
        metadata = dict(
            UnitProperties=[
                dict(
                    name="custom_unit_column",
                    description="Custom column in the spiking unit table for the NWB Conversion Tools tutorial.",
                    data=[x for x in range(len(self.sorting_extractor.get_unit_ids()))],
                )
            ]
        )
        return metadata
