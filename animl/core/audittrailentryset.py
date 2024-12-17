import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime

from .author import Author
from .software import Software
from .audittrailentry import AuditTrailEntry
from .diff import Diff


@forge_signature
class AuditTrailEntrySet(sdRDM.DataModel):

    """Container for audit trail entries describing changes to this document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("audittrailentrysetINDEX"),
        xml="@id",
    )

    audit_trail_entry: List[AuditTrailEntry] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "Describes a set of changes made to the particular AnIML document by one"
            " user at a given time."
        ),
        xml="AuditTrailEntry",
    )

    def add_to_audit_trail_entry(
        self,
        timestamp: Datetime,
        author: Author,
        action: str,
        software: Optional[Software] = None,
        reason: Optional[str] = None,
        comment: Optional[str] = None,
        diff: List[Diff] = ListPlus(),
        reference: List[str] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'AuditTrailEntry' to attribute audit_trail_entry

        Args:
            id (str): Unique identifier of the 'AuditTrailEntry' object. Defaults to 'None'.
            timestamp (): Date and time of modification..
            author (): Information about a person, a device or a piece of software authoring AnIML files..
            action (): Type of change made (created, modified, ...).
            software (): Software used to author this.. Defaults to None
            reason (): Explanation why changes were made.. Defaults to None
            comment (): Human-readable comment further explaining the changes.. Defaults to None
            diff (): Machine-readable description of changes made.. Defaults to ListPlus()
            reference (): ID of the SignableItem that was affected. If none is specified, entire document is covered.. Defaults to ListPlus()
        """

        params = {
            "timestamp": timestamp,
            "author": author,
            "action": action,
            "software": software,
            "reason": reason,
            "comment": comment,
            "diff": diff,
            "reference": reference,
        }

        if id is not None:
            params["id"] = id

        self.audit_trail_entry.append(AuditTrailEntry(**params))

        return self.audit_trail_entry[-1]
