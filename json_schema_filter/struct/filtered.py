from dataclasses import dataclass
from typing import Dict, List


@dataclass(kw_only=True)
class Selected:
    """
    Struct for obj that matched the schema
    """

    idx: int
    item: Dict


@dataclass(kw_only=True)
class Rejected:
    """
    Struct for obj that didn't match the schema
    """

    idx: int
    item: Dict
    reasons: List[str]

    def __repr__(self) -> str:
        return f"Filtered Item: [{self.idx}]\n\t" + "\n".join(self.reasons)


@dataclass(kw_only=True)
class FilterResult:
    """
    Struct for the result
    """

    selected: List[Selected]
    rejected: List[Rejected]

    def __repr__(self) -> str:
        return f"Total Selected: {len(self.selected)}\n" + "\n".join(
            [str(rejects) for rejects in self.rejected]
        )
