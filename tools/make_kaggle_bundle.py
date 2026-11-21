"""Build dist/broadbalk-rothc-kaggle-inputs.zip: only the inputs the notebook reads plus licences. Run from the project root."""
import zipfile
from pathlib import Path

ROTHC = Path("inputs/external/RothC_Py_bd90ce3cf616d5316042b73a3b1f09c5b6e3b361")
FILES = [
    "Broadbalk_1843-2010/01-BKSOC1843-data.xlsx", "Broadbalk_1843-2010/01-BKSOC1843.pdf",
    "inputs/external/era/01-data-1878-2023.xlsx", "inputs/external/era/01-data-rain-1853-2024.xlsx",
    "inputs/external/era/YIELD852925/crop_data.csv", "inputs/external/era/YIELD852925/notes_data.csv",
    "inputs/external/era/YIELD852925/README.txt", "inputs/external/era/YIELD852925/datapackage.json",
    "inputs/external/era/01-BKyld2667.xlsx", "inputs/external/era/01-BKyld6822.xlsx",
] + sorted(p.as_posix() for p in ROTHC.iterdir())

out = Path("dist/broadbalk-rothc-kaggle-inputs.zip")
out.parent.mkdir(exist_ok=True)
readme = Path("README.md").read_text(encoding="utf-8")
attribution = readme.split("## Sources and licences")[1].split("## Environment")[0]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for f in FILES:
        z.write(f, f)
    z.writestr("ATTRIBUTION.txt", "Sources and licences for the bundled files\n" + attribution)
print(f"{out}: {len(FILES) + 1} files, {out.stat().st_size:,} bytes")
