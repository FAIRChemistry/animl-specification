import sdRDM

from typing import Optional, Union, List
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime


@forge_signature
class IndividualValueSet(sdRDM.DataModel):

    """Multiple Values explicitly specified."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("individualvaluesetINDEX"),
        xml="@id",
    )

    values: List[Union[float, int, str, bool, Datetime, bytes]] = Field(
        multiple=True,
        description=(
            "I: Individual integer value (32 bits, signed). L: Individual long integer"
            " value (64 bits, signed). F: Individual 32-bit floating point value. D:"
            " Individual 64-bit floating point value. S: Individual string value."
            " Boolean: Individual boolean value. DateTime: Individual ISO date/time"
            " value. PNG: Base 64 encoded PNG image. EmbeddedXML: Value governed by a"
            " different XML Schema. SVG: Value governed by the SVG DTD. Used to"
            " represent vector graphic images."
        ),
        xml="{int: I, float: F, str: S, bool: Boolean, datetime: DateTime, bytes: PNG}",
        default_factory=ListPlus,
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
