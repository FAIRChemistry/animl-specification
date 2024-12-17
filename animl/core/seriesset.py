import sdRDM

from typing import Optional, Union, List
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .series import Series
from .unit import Unit
from .encodedvalueset import EncodedValueSet
from .autoincrementedvalueset import AutoIncrementedValueSet
from .individualvalueset import IndividualValueSet


@forge_signature
class SeriesSet(sdRDM.DataModel):

    """Container for n-dimensional Data."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seriessetINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    length: str = Field(
        ...,
        description="Number of data points each Series contains.",
        xml="@length",
    )

    series: List[Series] = Field(
        multiple=True,
        description="Container for multiple Values.",
        xml="Series",
        default_factory=ListPlus,
    )

    def add_to_series(
        self,
        name: str,
        dependency: str,
        series_id: str,
        series_type: str,
        visible: Optional[str] = None,
        plot_scale: Optional[str] = None,
        value_set: Union[
            IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet, None
        ] = None,
        unit: Optional[Unit] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Series' to attribute series

        Args:
            id (str): Unique identifier of the 'Series' object. Defaults to 'None'.
            name (): Plain-text name of this item..
            dependency (): Specified whether the Series is independent or dependent..
            series_id (): Identifies the Series. Used in References from subordinate ExperimentSteps. Unique per SeriesSet..
            series_type (): Data type used by all values in this Series..
            visible (): Specifies whether data in this Series is to be displayed to the user by default.. Defaults to None
            plot_scale (): Specifies whether the data in this Series is typically plotted on a linear or logarithmic scale.. Defaults to None
            value_set (): IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet: Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. AutoIncrementedValueSet: Multiple values given in form of a start value and an increment.. Defaults to None
            unit (): Definition of a Scientific Unit.. Defaults to None
        """

        params = {
            "name": name,
            "dependency": dependency,
            "series_id": series_id,
            "series_type": series_type,
            "visible": visible,
            "plot_scale": plot_scale,
            "value_set": value_set,
            "unit": unit,
        }

        if id is not None:
            params["id"] = id

        self.series.append(Series(**params))

        return self.series[-1]
