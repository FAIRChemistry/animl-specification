import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .software import Software
from .category import Category
from .author import Author
from .seriesset import SeriesSet
from .device import Device
from .parameter import Parameter


@forge_signature
class Method(sdRDM.DataModel):

    """Describes how this Experiment was performed."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("methodINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Optional method name, as defined in the instrument software.",
        xml="@name",
    )

    author: Optional[Author] = Field(
        default=None,
        description=(
            "Information about a person, a device or a piece of software authoring"
            " AnIML files."
        ),
        xml="Author",
    )

    device: Optional[Device] = Field(
        default=None,
        description="Device used to perform experiment.",
        xml="Device",
    )

    software: Optional[Software] = Field(
        default=None,
        description="Software used to author this.",
        xml="Software",
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
