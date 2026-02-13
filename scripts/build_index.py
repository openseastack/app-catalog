#!/usr/bin/env python3
"""Build index.json from all apps/*/manifest.json files."""
import json
import base64
import sys
from pathlib import Path

def build_index(catalog_root: Path) -> list:
    apps_dir = catalog_root / "apps"
    index = []

    for app_dir in sorted(apps_dir.iterdir()):
        if not app_dir.is_dir():
            continue

        manifest_path = app_dir / "manifest.json"
        if not manifest_path.exists():
            print(f"WARN: {app_dir.name}/ has no manifest.json, skipping")
            continue

        with open(manifest_path) as f:
            manifest = json.load(f)

        # Embed icon as base64 data URI if present
        icon_file = manifest.get("icon")
        if icon_file:
            icon_path = app_dir / icon_file
            if icon_path.exists():
                with open(icon_path, "rb") as img:
                    b64 = base64.b64encode(img.read()).decode()
                    manifest["icon_data"] = f"data:image/png;base64,{b64}"
            else:
                print(f"WARN: {app_dir.name}/icon not found at {icon_file}")

        manifest["_source_dir"] = app_dir.name
        index.append(manifest)

    return index


if __name__ == "__main__":
    catalog_root = Path(__file__).parent.parent
    index = build_index(catalog_root)

    output_path = catalog_root / "index.json"
    with open(output_path, "w") as f:
        json.dump(index, f, indent=2)

    print(f"Built index.json with {len(index)} apps")
    sys.exit(0)
