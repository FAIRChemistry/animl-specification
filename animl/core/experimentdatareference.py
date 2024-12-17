import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ExperimentDataReference(sdRDM.DataModel):

    """Reference to an Experiment Step whose data is consumed."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentdatareferenceINDEX"),
        xml="@id",
    )

    role: str = Field(
        ...,
        description="None",
        xml="@role",
    )

    data_purpose: str = Field(
        ...,
        description="None",
        xml="@dataPurpose",
    )

    experiment_step_id: str = Field(
        ...,
        description="None",
        xml="@experimentStepID",
    )
