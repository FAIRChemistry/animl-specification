import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .category import Category
from .tagset import TagSet
from .seriesset import SeriesSet
from .parameter import Parameter


@forge_signature
class Sample(sdRDM.DataModel):

    """Individual Sample, referenced from other parts of this AnIML document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    sample_id: str = Field(
        ...,
        description="None",
        xml="@sampleID",
    )

    barcode: Optional[str] = Field(
        default=None,
        description="Value of barcode label that is attached to sample container.",
        xml="@barcode",
    )

    comment: Optional[str] = Field(
        default=None,
        description="Unstructured text comment to further describe the Sample.",
        xml="@comment",
    )

    derived: Optional[str] = Field(
        default=None,
        description=(
            "Indicates whether this is a derived Sample. A derived Sample is a Sample"
            " that has been created by applying a Technique. (Sub-Sampling, Processing,"
            " ...)"
        ),
        xml="@derived",
    )

    container_type: Optional[str] = Field(
        default=None,
        description=(
            "Whether this sample is also a container for other samples. Set to 'simple'"
            " if not."
        ),
        xml="@containerType",
    )

    container_id: Optional[str] = Field(
        default=None,
        description="Sample ID of container in which this sample is located.",
        xml="@containerID",
    )

    location_in_container: Optional[str] = Field(
        default=None,
        description=(
            "Coordinates of this sample within the enclosing container. In case of"
            " microplates or trays, the row is identified by letters and the column is"
            " identified by numbers (1-based) while in landscape orientation. Examples:"
            " A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row,"
            " 2nd column."
        ),
        xml="@locationInContainer",
    )

    source_data_location: Optional[str] = Field(
        default=None,
        description=(
            "Points to the original data source. May be a file name, uri, database ID,"
            " etc."
        ),
        xml="@sourceDataLocation",
    )

    tag_set: Optional[TagSet] = Field(
        default=TagSet(),
        description="Set of Tag elements.",
        xml="TagSet",
    )

    category: List[Category] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Defines a category of Parameters and SeriesSets. Used to model"
            " hierarchies."
        ),
        xml="Category",
    )

    def add_to_category(
        self,
        name: str,
        parameter: List[Parameter] = ListPlus(),
        series_set: List[SeriesSet] = ListPlus(),
        category: List[Category] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Category' to attribute category

        Args:
            id (str): Unique identifier of the 'Category' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            parameter (): Name/Value Pair.. Defaults to ListPlus()
            series_set (): Container for n-dimensional Data.. Defaults to ListPlus()
            category (): Defines a category of Parameters and SeriesSets. Used to model hierarchies.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "parameter": parameter,
            "series_set": series_set,
            "category": category,
        }

        if id is not None:
            params["id"] = id

        self.category.append(Category(**params))

        return self.category[-1]
