import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .increment import Increment
from .startvalue import StartValue


@forge_signature
class AutoIncrementedValueSet(sdRDM.DataModel):

    """Multiple values given in form of a start value and an increment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("autoincrementedvaluesetINDEX"),
        xml="@id",
    )

    start_value: StartValue = Field(
        ...,
        description="Lower boundary of an interval or ValueSet.",
        xml="StartValue",
    )

    increment: Increment = Field(
        ...,
        description="Increment value",
        xml="Increment",
    )

    start_index: Optional[str] = Field(
        default=None,
        description=(
            "Zero-based index of the first entry in this Value Set. The specification"
            " is inclusive."
        ),
        xml="@startIndex",
    )

    end_index: Optional[str] = Field(
        default=None,
        description=(
            "Zero-based index of the last entry in this Value Set. The specification is"
            " inclusive."
        ),
        xml="@endIndex",
    )
