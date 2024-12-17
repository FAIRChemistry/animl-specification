import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Diff(sdRDM.DataModel):

    """Machine-readable description of changes made."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("diffINDEX"),
        xml="@id",
    )

    scope: str = Field(
        ...,
        description="Scope of diff. May be 'element' or 'attribute'.",
        xml="@scope",
    )

    changed_item: str = Field(
        ...,
        description="ID of the SignableItem that was changed",
        xml="@changedItem",
    )

    old_value: str = Field(
        ...,
        description="No descripiton provided",
        xml="OldValue",
    )

    new_value: str = Field(
        ...,
        description="No descripiton provided",
        xml="NewValue",
    )
