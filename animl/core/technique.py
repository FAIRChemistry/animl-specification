import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .extension import Extension


@forge_signature
class Technique(sdRDM.DataModel):

    """Reference to Technique Definition used in this Experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("techniqueINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Plain-text name of this item.",
        xml="@name",
    )

    uri: str = Field(
        ...,
        description="URI where Technique Definition file can be fetched.",
        xml="@uri",
    )

    sha256: Optional[str] = Field(
        default=None,
        description=(
            "SHA256 checksum of the referenced Technique Definition. Hex encoded, lower"
            " cased. Similar to the output of the sha256 unix command."
        ),
        xml="@sha256",
    )

    extension: List[Extension] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Reference to an Extension to amend the active Technique Definition."
        ),
        xml="Extension",
    )

    def add_to_extension(
        self,
        uri: str,
        name: str,
        sha256: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Extension' to attribute extension

        Args:
            id (str): Unique identifier of the 'Extension' object. Defaults to 'None'.
            uri (): URI where Extension file can be fetched..
            name (): Name of Extension to be used. Must match Name given in Extension Definition file..
            sha256 (): SHA256 checksum of the referenced Extension. Hex encoded, lower cased. Similar to the output of the sha256 unix command.. Defaults to None
        """

        params = {
            "uri": uri,
            "name": name,
            "sha256": sha256,
        }

        if id is not None:
            params["id"] = id

        self.extension.append(Extension(**params))

        return self.extension[-1]
