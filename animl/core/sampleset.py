import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .category import Category
from .sample import Sample
from .tagset import TagSet


@forge_signature
class SampleSet(sdRDM.DataModel):

    """Container for Samples used in this AnIML document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("samplesetINDEX"),
        xml="@id",
    )

    sample: List[Sample] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Individual Sample, referenced from other parts of this AnIML document."
        ),
        xml="Sample",
    )

    def add_to_sample(
        self,
        name: str,
        sample_id: str,
        barcode: Optional[str] = None,
        comment: Optional[str] = None,
        derived: Optional[str] = None,
        container_type: Optional[str] = None,
        container_id: Optional[str] = None,
        location_in_container: Optional[str] = None,
        source_data_location: Optional[str] = None,
        tag_set: Optional[TagSet] = None,
        category: List[Category] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:
            id (str): Unique identifier of the 'Sample' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            sample_id (): None.
            barcode (): Value of barcode label that is attached to sample container.. Defaults to None
            comment (): Unstructured text comment to further describe the Sample.. Defaults to None
            derived (): Indicates whether this is a derived Sample. A derived Sample is a Sample that has been created by applying a Technique. (Sub-Sampling, Processing, ...). Defaults to None
            container_type (): Whether this sample is also a container for other samples. Set to 'simple' if not.. Defaults to None
            container_id (): Sample ID of container in which this sample is located.. Defaults to None
            location_in_container (): Coordinates of this sample within the enclosing container. In case of microplates or trays, the row is identified by letters and the column is identified by numbers (1-based) while in landscape orientation. Examples: A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd column.. Defaults to None
            source_data_location (): Points to the original data source. May be a file name, uri, database ID, etc.. Defaults to None
            tag_set (): Set of Tag elements.. Defaults to None
            category (): Defines a category of Parameters and SeriesSets. Used to model hierarchies.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "sample_id": sample_id,
            "barcode": barcode,
            "comment": comment,
            "derived": derived,
            "container_type": container_type,
            "container_id": container_id,
            "location_in_container": location_in_container,
            "source_data_location": source_data_location,
            "tag_set": tag_set,
            "category": category,
        }

        if id is not None:
            params["id"] = id

        self.sample.append(Sample(**params))

        return self.sample[-1]
