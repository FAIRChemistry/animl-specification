import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Tag(sdRDM.DataModel):

    """Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("tagINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="None",
        xml="@name",
    )

    value: Optional[str] = Field(
        default=None,
        description="None",
        xml="@value",
    )
