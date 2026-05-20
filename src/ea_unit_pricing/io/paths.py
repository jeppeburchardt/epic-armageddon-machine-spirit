"""IO utilities — output directory resolution and path helpers."""

from __future__ import annotations

import os
from pathlib import Path

__all__ = ["resolve_output_dir"]

_ENV_VAR = "EAUP_OUTPUT_DIR"
_DEFAULT = Path("output")


def resolve_output_dir(override: Path | None = None) -> Path:
    """Return the effective output directory.

    Resolution order:
    1. *override* (e.g. from a ``--output-dir`` CLI flag)
    2. ``EAUP_OUTPUT_DIR`` environment variable
    3. ``./output/`` (default)
    """
    if override is not None:
        return override
    env = os.environ.get(_ENV_VAR)
    if env:
        return Path(env)
    return _DEFAULT
