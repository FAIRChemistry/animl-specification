import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SampleInheritance(sdRDM.DataModel):

    """Indicates that a Sample was inherited from the parent ExperimentStep."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("sampleinheritanceINDEX"),
        xml="@id",
    )

    role: str = Field(
        ...,
        description="Role this sample plays within the current ExperimentStep.",
        xml="@role",
    )

    sample_purpose: str = Field(
        ...,
        description=(
            "Specifies whether the referenced sample is produced or consumed by the"
            " current ExperimentStep."
        ),
        xml="@samplePurpose",
    )
