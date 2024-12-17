import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class SampleReference(sdRDM.DataModel):

    """Reference to a Sample used in this Experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("samplereferenceINDEX"),
        xml="@id",
    )

    sample_id: str = Field(
        ...,
        description=(
            "SampleID of the Sample used in the current ExperimentStep. Refers to the"
            " sampleID within the SampleSet section of the document."
        ),
        xml="@sampleID",
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
