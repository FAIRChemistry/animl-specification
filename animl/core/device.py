import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Device(sdRDM.DataModel):

    """Device used to perform experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("deviceINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Common name.",
        xml="Name",
    )

    device_identifier: Optional[str] = Field(
        default=None,
        description="Unique name or identifier of the device.",
        xml="DeviceIdentifier",
    )

    manufacturer: Optional[str] = Field(
        default=None,
        description="Company name.",
        xml="Manufacturer",
    )

    firmware_version: Optional[str] = Field(
        default=None,
        description="Version identifier of firmware release.",
        xml="FirmwareVersion",
    )

    serial_number: Optional[str] = Field(
        default=None,
        description="Unique serial number of device.",
        xml="SerialNumber",
    )
