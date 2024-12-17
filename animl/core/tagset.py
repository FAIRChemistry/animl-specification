import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .tag import Tag


@forge_signature
class TagSet(sdRDM.DataModel):

    """Set of Tag elements."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("tagsetINDEX"),
        xml="@id",
    )

    tag: List[Tag] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Tag to mark related data items. When a value is given, it may also serve"
            " as a reference to an external data system."
        ),
        xml="Tag",
    )

    def add_to_tag(
        self, name: str, value: Optional[str] = None, id: Optional[str] = None
    ) -> None:
        """
        This method adds an object of type 'Tag' to attribute tag

        Args:
            id (str): Unique identifier of the 'Tag' object. Defaults to 'None'.
            name (): None.
            value (): None. Defaults to None
        """

        params = {
            "name": name,
            "value": value,
        }

        if id is not None:
            params["id"] = id

        self.tag.append(Tag(**params))

        return self.tag[-1]
