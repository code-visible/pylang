from typing import TypedDict

SourceAbstract = TypedDict(
    "SourceAbstract ",
    {
        "id": str,
        "pos": str,
        "name": str,
        "file": str,
        "comment": str,
        "fields": list[str],
    },
)
