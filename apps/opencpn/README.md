# OpenCPN

Professional chart plotter and navigation software with remote VNC access.

- **Category:** Navigation
- **License:** GPL-2.0
- **Access:** Web VNC on port 6080, Direct VNC on port 5900
- **Image:** `ghcr.io/openseastack/opencpn`

## Configuration

| Setting | Options | Default |
|:---|:---|:---|
| Display Resolution | 1024x768, 1280x720, 1920x1080 | 1024x768 |

## Data Volumes

- `/data/openseastack/opencpn` — OpenCPN configuration
- `/data/openseastack/charts` — Chart files (read-only)
