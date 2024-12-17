import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .experimentdatareference import ExperimentDataReference
from .experimentdatabulkreference import ExperimentDataBulkReference


@forge_signature
class ExperimentDataReferenceSet(sdRDM.DataModel):

    """Set of Experiment Steps consumed by this Experiment Step."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("experimentdatareferencesetINDEX"),
        xml="@id",
    )

    experiment_data_reference: List[ExperimentDataReference] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Reference to an Experiment Step whose data is consumed.",
        xml="ExperimentDataReference",
    )

    experiment_data_bulk_reference: List[ExperimentDataBulkReference] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Prefix-based reference to a set of Experiment Steps whose data are"
            " consumed."
        ),
        xml="ExperimentDataBulkReference",
    )

    def add_to_experiment_data_reference(
        self,
        role: str,
        data_purpose: str,
        experiment_step_id: str,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ExperimentDataReference' to attribute experiment_data_reference

        Args:
            id (str): Unique identifier of the 'ExperimentDataReference' object. Defaults to 'None'.
            role (): None.
            data_purpose (): None.
            experiment_step_id (): None.
        """

        params = {
            "role": role,
            "data_purpose": data_purpose,
            "experiment_step_id": experiment_step_id,
        }

        if id is not None:
            params["id"] = id

        self.experiment_data_reference.append(ExperimentDataReference(**params))

        return self.experiment_data_reference[-1]

    def add_to_experiment_data_bulk_reference(
        self,
        role: str,
        data_purpose: str,
        experiment_step_id_prefix: str,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ExperimentDataBulkReference' to attribute experiment_data_bulk_reference

        Args:
            id (str): Unique identifier of the 'ExperimentDataBulkReference' object. Defaults to 'None'.
            role (): None.
            data_purpose (): None.
            experiment_step_id_prefix (): None.
        """

        params = {
            "role": role,
            "data_purpose": data_purpose,
            "experiment_step_id_prefix": experiment_step_id_prefix,
        }

        if id is not None:
            params["id"] = id

        self.experiment_data_bulk_reference.append(
            ExperimentDataBulkReference(**params)
        )

        return self.experiment_data_bulk_reference[-1]
