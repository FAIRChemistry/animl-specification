import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SIUnit(sdRDM.DataModel):

    """Combination of SI Units used to represent Scientific unit"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("siunitINDEX"),
        xml="@id",
    )

    factor: Optional[str] = Field(
        default=None,
        description="None",
        xml="@factor",
    )

    exponent: Optional[str] = Field(
        default=None,
        description="None",
        xml="@exponent",
    )

    offset: Optional[str] = Field(
        default=None,
        description="None",
        xml="@offset",
    )
