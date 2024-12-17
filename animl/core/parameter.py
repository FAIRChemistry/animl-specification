import sdRDM

from typing import Optional, Union
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .unit import Unit


@forge_signature
class Parameter(sdRDM.DataModel):

    """Name/Value Pair."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parameterINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    parameter_type: str = Field(
        ...,
        description="Data type of this parameter",
        xml="@parameterType",
    )

    value: Union[int, float, str, bool, Datetime, bytes] = Field(
        ...,
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
    )

    unit: Optional[Unit] = Field(
        default=None,
        description="Unit: Definition of a Scientific Unit.",
        xml="Unit: Unit",
    )
