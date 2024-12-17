import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .siunit import SIUnit


@forge_signature
class Unit(sdRDM.DataModel):

    """Definition of a Scientific Unit."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("unitINDEX"),
        xml="@id",
    )

    label: str = Field(
        ...,
        description="Defines the visual representation of a particular Unit.",
        xml="@label",
    )

    quantity: Optional[str] = Field(
        default=None,
        description="Quantity the unit can be applied to",
        xml="@quantity",
    )

    si_unit: List[SIUnit] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Combination of SI Units used to represent Scientific unit",
        xml="SIUnit",
    )

    def add_to_si_unit(
        self,
        factor: Optional[str] = None,
        exponent: Optional[str] = None,
        offset: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'SIUnit' to attribute si_unit

        Args:
            id (str): Unique identifier of the 'SIUnit' object. Defaults to 'None'.
            factor (): None. Defaults to None
            exponent (): None. Defaults to None
            offset (): None. Defaults to None
        """

        params = {
            "factor": factor,
            "exponent": exponent,
            "offset": offset,
        }

        if id is not None:
            params["id"] = id

        self.si_unit.append(SIUnit(**params))

        return self.si_unit[-1]
