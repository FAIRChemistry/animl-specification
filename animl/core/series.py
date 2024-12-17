import sdRDM

from typing import Optional, Union
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .unit import Unit
from .encodedvalueset import EncodedValueSet
from .autoincrementedvalueset import AutoIncrementedValueSet
from .individualvalueset import IndividualValueSet


@forge_signature
class Series(sdRDM.DataModel):

    """Container for multiple Values."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("seriesINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    dependency: str = Field(
        ...,
        description="Specified whether the Series is independent or dependent.",
        xml="@dependency",
    )

    series_id: str = Field(
        ...,
        description=(
            "Identifies the Series. Used in References from subordinate"
            " ExperimentSteps. Unique per SeriesSet."
        ),
        xml="@seriesID",
    )

    series_type: str = Field(
        ...,
        description="Data type used by all values in this Series.",
        xml="@seriesType",
    )

    visible: Optional[str] = Field(
        default=None,
        description=(
            "Specifies whether data in this Series is to be displayed to the user by"
            " default."
        ),
        xml="@visible",
    )

    plot_scale: Optional[str] = Field(
        default=None,
        description=(
            "Specifies whether the data in this Series is typically plotted on a linear"
            " or logarithmic scale."
        ),
        xml="@plotScale",
    )

    value_set: Union[
        IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet, None
    ] = Field(
        default=None,
        description=(
            "IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet:"
            " Multiple numeric values encoded as a base64 binary string. Uses"
            " little-endian byte order. AutoIncrementedValueSet: Multiple values given"
            " in form of a start value and an increment."
        ),
        xml=(
            "{IndividualValueSet: IndividualValueSet, EncodedValueSet: EncodedValueSet,"
            " AutoIncrementedValueSet: AutoIncrementedValueSet}"
        ),
    )

    unit: Optional[Unit] = Field(
        default=None,
        description="Definition of a Scientific Unit.",
        xml="Unit",
    )
