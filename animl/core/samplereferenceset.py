import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .sampleinheritance import SampleInheritance
from .samplereference import SampleReference


@forge_signature
class SampleReferenceSet(sdRDM.DataModel):

    """Set of Samples used in this Experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("samplereferencesetINDEX"),
        xml="@id",
    )

    sample_reference: List[SampleReference] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Reference to a Sample used in this Experiment.",
        xml="SampleReference",
    )

    sample_inheritance: List[SampleInheritance] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Indicates that a Sample was inherited from the parent ExperimentStep."
        ),
        xml="SampleInheritance",
    )

    def add_to_sample_reference(
        self, sample_id: str, role: str, sample_purpose: str, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'SampleReference' to attribute sample_reference

        Args:
            id (str): Unique identifier of the 'SampleReference' object. Defaults to 'None'.
            sample_id (): SampleID of the Sample used in the current ExperimentStep. Refers to the sampleID within the SampleSet section of the document..
            role (): Role this sample plays within the current ExperimentStep..
            sample_purpose (): Specifies whether the referenced sample is produced or consumed by the current ExperimentStep..
        """

        params = {
            "sample_id": sample_id,
            "role": role,
            "sample_purpose": sample_purpose,
        }

        if id is not None:
            params["id"] = id

        self.sample_reference.append(SampleReference(**params))

        return self.sample_reference[-1]

    def add_to_sample_inheritance(
        self, role: str, sample_purpose: str, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'SampleInheritance' to attribute sample_inheritance

        Args:
            id (str): Unique identifier of the 'SampleInheritance' object. Defaults to 'None'.
            role (): Role this sample plays within the current ExperimentStep..
            sample_purpose (): Specifies whether the referenced sample is produced or consumed by the current ExperimentStep..
        """

        params = {
            "role": role,
            "sample_purpose": sample_purpose,
        }

        if id is not None:
            params["id"] = id

        self.sample_inheritance.append(SampleInheritance(**params))

        return self.sample_inheritance[-1]
