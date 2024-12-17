import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Extension(sdRDM.DataModel):

    """Reference to an Extension to amend the active Technique Definition."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("extensionINDEX"),
        xml="@id",
    )

    uri: str = Field(
        ...,
        description="URI where Extension file can be fetched.",
        xml="@uri",
    )

    name: str = Field(
        ...,
        description=(
            "Name of Extension to be used. Must match Name given in Extension"
            " Definition file."
        ),
        xml="@name",
    )

    sha256: Optional[str] = Field(
        default=None,
        description=(
            "SHA256 checksum of the referenced Extension. Hex encoded, lower cased."
            " Similar to the output of the sha256 unix command."
        ),
        xml="@sha256",
    )
