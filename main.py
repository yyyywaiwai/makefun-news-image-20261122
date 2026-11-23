#!/usr/bin/env python3
"""News-image entry: copy the day's news image to the output directory.

The image (entry.png, beside this file) sums up the world news of
22 November 2026: the COP31 climate talks collapsing in Antalya, tanker
attacks near Hormuz, NATO's answer in Poland, the capture of
"Chapo Isidro" in Mexico, the FBI database probe and the Senate's
permitting bill, BepiColombo at Mercury, and the Seattle airport
arrests, with Alcaraz's first ATP Finals title and Verstappen's Las
Vegas win in the sport ticker. The grader runs this program with the
repository read-only and a writable output directory; outside that
container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    source = HERE / "entry.png"
    target = output_dir / "entry.png"
    shutil.copyfile(source, target)
    # The program runs twice and both runs must write the same bytes, so
    # confirm the copy landed whole before exiting.
    if source.stat().st_size != target.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")
    if sha256(source) != sha256(target):
        raise SystemExit("entry.png copy does not match the source")


if __name__ == "__main__":
    main()
