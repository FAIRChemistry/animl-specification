import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .startvalue import StartValue
from .endvalue import EndValue


@forge_signature
class ParentDataPointReference(sdRDM.DataModel):

    """Reference to a data point or value range in an independent Series in the parent Result."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parentdatapointreferenceINDEX"),
        xml="@id",
    )

    series_id: str = Field(
        ...,
        description="Contains the ID of the Series referenced.",
        xml="@seriesID",
    )

    start_value: StartValue = Field(
        ...,
        description="Lower boundary of an interval or ValueSet.",
        xml="StartValue",
    )

    end_value: Optional[EndValue] = Field(
        default=None,
        description="Upper boundary of an interval.",
        xml="EndValue",
    )
