import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .author import Author
from .software import Software
from .diff import Diff


@forge_signature
class AuditTrailEntry(sdRDM.DataModel):

    """Describes a set of changes made to the particular AnIML document by one user at a given time."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("audittrailentryINDEX"),
        xml="@id",
    )

    timestamp: Datetime = Field(
        ...,
        description="Date and time of modification.",
        xml="Timestamp",
    )

    author: Author = Field(
        ...,
        description=(
            "Information about a person, a device or a piece of software authoring"
            " AnIML files."
        ),
        xml="Author",
    )

    action: str = Field(
        ...,
        description="Type of change made (created, modified, ...)",
        xml="Action",
    )

    software: Optional[Software] = Field(
        default=None,
        description="Software used to author this.",
        xml="Software",
    )

    reason: Optional[str] = Field(
        default=None,
        description="Explanation why changes were made.",
        xml="Reason",
    )

    comment: Optional[str] = Field(
        default=None,
        description="Human-readable comment further explaining the changes.",
        xml="Comment",
    )

    diff: List[Diff] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Machine-readable description of changes made.",
        xml="Diff",
    )

    reference: List[str] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "ID of the SignableItem that was affected. If none is specified, entire"
            " document is covered."
        ),
        xml="Reference",
    )

    def add_to_diff(
        self,
        scope: str,
        changed_item: str,
        old_value: str,
        new_value: str,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Diff' to attribute diff

        Args:
            id (str): Unique identifier of the 'Diff' object. Defaults to 'None'.
            scope (): Scope of diff. May be 'element' or 'attribute'..
            changed_item (): ID of the SignableItem that was changed.
            old_value (): No descripiton provided.
            new_value (): No descripiton provided.
        """

        params = {
            "scope": scope,
            "changed_item": changed_item,
            "old_value": old_value,
            "new_value": new_value,
        }

        if id is not None:
            params["id"] = id

        self.diff.append(Diff(**params))

        return self.diff[-1]
