from typing import TypedDict

SourcePkg = TypedDict(
    "SourcePkg",
    {
        "id": str,
        "name": str,
        "path": int,
    },
)
