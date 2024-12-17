import sdRDM

from typing import Optional, Union
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Increment(sdRDM.DataModel):

    """Increment value"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("incrementINDEX"),
        xml="@id",
    )

    value: Union[int, float] = Field(
        ...,
        description=(
            "I: Individual integer value (32 bits, signed). L: Individual long integer"
            " value (64 bits, signed). F: Individual 32-bit floating point value. D:"
            " Individual 64-bit floating point value."
        ),
        xml="{int: I, float: F}",
    )
