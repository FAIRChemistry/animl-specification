import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class EncodedValueSet(sdRDM.DataModel):

    """Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("encodedvaluesetINDEX"),
        xml="@id",
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
