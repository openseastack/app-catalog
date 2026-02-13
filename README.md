# OpenSeaStack App Catalog

The official catalog of applications for [OpenSeaStack](https://openseastack.org). Apps listed here are available for installation via the Admin Interface's App Store.

## Structure

```
apps/
  opencpn/
    manifest.json     # App manifest (required)
    icon.png          # App icon, max 100KB (optional)
    README.md         # App documentation (optional)
  nodered/
    manifest.json
    ...
```

Each app lives in its own directory under `apps/`. The directory name **must** match the `id` field in `manifest.json`.

## Contributing an App

1. **Fork** this repository
2. **Create** a new directory under `apps/` with your app's ID (lowercase, hyphens only)
3. **Write** a `manifest.json` following the schema in [catalog.schema.json](catalog.schema.json)
4. **Add** an icon (PNG, max 100KB) and set the `icon` field in your manifest
5. **Submit** a Pull Request

### Manifest Requirements

| Field | Required | Description |
|:---|:---:|:---|
| `id` | ✅ | Unique identifier (`^[a-z0-9-]+$`) |
| `name` | ✅ | Display name (max 64 chars) |
| `version` | ✅ | Semantic version (`X.Y.Z`) |
| `description` | ✅ | Short description (max 256 chars) |
| `container` | ✅ | Container config (`image`, `tag` required) |
| `author` | | Author name and optional URL |
| `license` | | SPDX license identifier |
| `category` | | One of: `navigation`, `monitoring`, `automation`, `ai`, `tools`, `media`, `communication` |
| `icon` | | Relative path to icon file |
| `access` | | Web/VNC access URLs |
| `requirements` | | Architecture, RAM, OS version constraints |
| `config_schema` | | User-configurable settings |

See [catalog.schema.json](catalog.schema.json) for the full JSON Schema specification.

## CI/CD

On every push to `main`:
1. All manifests are validated against `catalog.schema.json`
2. Icons are checked for existence and size limits
3. An aggregated `index.json` is built and deployed to GitHub Pages

The live catalog is served at: `https://openseastack.github.io/app-catalog/index.json`

## Adding Custom Sources

Users can add third-party catalogs via the Admin Interface. Any repo following this same structure can serve its own `index.json` and be added as a custom source on the device.
