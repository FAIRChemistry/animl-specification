import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class ExperimentDataBulkReference(sdRDM.DataModel):

    """Prefix-based reference to a set of Experiment Steps whose data are consumed."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentdatabulkreferenceINDEX"),
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

    experiment_step_id_prefix: str = Field(
        ...,
        description="None",
        xml="@experimentStepIDPrefix",
    )
