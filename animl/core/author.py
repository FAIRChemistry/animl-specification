import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Author(sdRDM.DataModel):

    """Information about a person, a device or a piece of software authoring AnIML files."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    user_type: str = Field(
        ...,
        description="Type of user (human, device, software)",
        xml="@userType",
    )

    name: str = Field(
        ...,
        description="Common name.",
        xml="Name",
    )

    affiliation: Optional[str] = Field(
        default=None,
        description="Organization the Author is affiliated with.",
        xml="Affiliation",
    )

    role: Optional[str] = Field(
        default=None,
        description="Role the Author plays within the organization.",
        xml="Role",
    )

    email: Optional[str] = Field(
        default=None,
        description="RFC822-compliant email address.",
        xml="Email",
    )

    phone: Optional[str] = Field(
        default=None,
        description="Phone number.",
        xml="Phone",
    )

    location: Optional[str] = Field(
        default=None,
        description="Location or physical address.",
        xml="Location",
    )
