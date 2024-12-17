import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .category import Category
from .method import Method
from .tagset import TagSet
from .seriesset import SeriesSet
from .result import Result
from .technique import Technique
from .infrastructure import Infrastructure


@forge_signature
class Template(sdRDM.DataModel):

    """Represents a template for an ExperimentStep."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("templateINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    template_id: str = Field(
        ...,
        description="None",
        xml="@templateID",
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

    technique: Optional[Technique] = Field(
        default=None,
        description="Reference to Technique Definition used in this Experiment.",
        xml="Technique",
    )

    infrastructure: Optional[Infrastructure] = Field(
        default=Infrastructure(),
        description="Contains references to the context of this Experiment.",
        xml="Infrastructure",
    )

    method: Optional[Method] = Field(
        default=Method(),
        description="Describes how this Experiment was performed.",
        xml="Method",
    )

    result: List[Result] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Container for Data derived from Experiment.",
        xml="Result",
    )

    def add_to_result(
        self,
        name: str,
        series_set: Optional[SeriesSet] = None,
        category: List[Category] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Result' to attribute result

        Args:
            id (str): Unique identifier of the 'Result' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            series_set (): Container for n-dimensional Data.. Defaults to None
            category (): Defines a category of Parameters and SeriesSets. Used to model hierarchies.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "series_set": series_set,
            "category": category,
        }

        if id is not None:
            params["id"] = id

        self.result.append(Result(**params))

        return self.result[-1]
