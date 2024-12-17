import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .experimentstepset import ExperimentStepSet
from .sampleset import SampleSet
from .audittrailentryset import AuditTrailEntrySet


@forge_signature
class AnIML(sdRDM.DataModel):

    """ComplexType for the root element of an AnIML document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("animlINDEX"),
        xml="@id",
    )

    version: str = Field(
        description=(
            "Version number of the AnIML Core Schema used in this document. Must be"
            " '0.90'."
        ),
        default=0.90,
        xml="@version",
    )

    sample_set: Optional[SampleSet] = Field(
        default=SampleSet(),
        description="Container for Samples used in this AnIML document.",
        xml="SampleSet",
    )

    experiment_step_set: Optional[ExperimentStepSet] = Field(
        default=ExperimentStepSet(),
        description=(
            "Container for multiple ExperimentSteps that describe the process and"
            " results."
        ),
        xml="ExperimentStepSet",
    )

    audit_trail_entry_set: Optional[AuditTrailEntrySet] = Field(
        default=AuditTrailEntrySet(),
        description=(
            "Container for audit trail entries describing changes to this document."
        ),
        xml="AuditTrailEntrySet",
    )
