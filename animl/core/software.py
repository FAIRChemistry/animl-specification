import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Software(sdRDM.DataModel):

    """Software used to author this."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("softwareINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Common name.",
        xml="Name",
    )

    manufacturer: Optional[str] = Field(
        default=None,
        description="Company name.",
        xml="Manufacturer",
    )

    version: Optional[str] = Field(
        default=None,
        description="Version identifier of software release.",
        xml="Version",
    )

    operating_system: Optional[str] = Field(
        default=None,
        description="Operating system the software was running on.",
        xml="OperatingSystem",
    )
