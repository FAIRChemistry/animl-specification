import sdRDM

from typing import Optional, Union, List
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .series import Series
from .unit import Unit
from .parameter import Parameter
from .seriesset import SeriesSet


@forge_signature
class Category(sdRDM.DataModel):

    """Defines a category of Parameters and SeriesSets. Used to model hierarchies."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("categoryINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    parameter: List[Parameter] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Name/Value Pair.",
        xml="Parameter",
    )

    series_set: List[SeriesSet] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Container for n-dimensional Data.",
        xml="SeriesSet",
    )

    category: List["Category"] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Defines a category of Parameters and SeriesSets. Used to model"
            " hierarchies."
        ),
        xml="Category",
    )

    def add_to_parameter(
        self,
        name: str,
        parameter_type: str,
        value: Union[int, float, str, bool, Datetime, bytes],
        unit: Optional[Unit] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Parameter' to attribute parameter

        Args:
            id (str): Unique identifier of the 'Parameter' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            parameter_type (): Data type of this parameter.
            value (): I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value. DateTime: Individual ISO date/time value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a different XML Schema. SVG: Value governed by the SVG DTD. Used to represent vector graphic images..
            unit (): Unit: Definition of a Scientific Unit.. Defaults to None
        """

        params = {
            "name": name,
            "parameter_type": parameter_type,
            "value": value,
            "unit": unit,
        }

        if id is not None:
            params["id"] = id

        self.parameter.append(Parameter(**params))

        return self.parameter[-1]

    def add_to_series_set(
        self,
        name: str,
        length: str,
        series: List[Series] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SeriesSet' to attribute series_set

        Args:
            id (str): Unique identifier of the 'SeriesSet' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            length (): Number of data points each Series contains..
            series (): Container for multiple Values.. Defaults to ListPlus()
        """

        params = {
            "name": name,
            "length": length,
            "series": series,
        }

        if id is not None:
            params["id"] = id

        self.series_set.append(SeriesSet(**params))

        return self.series_set[-1]

    def add_to_category(
        self,
        name: str,
        parameter: List[Parameter] = ListPlus(),
        series_set: List[SeriesSet] = ListPlus(),
        category: List["Category"] = ListPlus(),
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
