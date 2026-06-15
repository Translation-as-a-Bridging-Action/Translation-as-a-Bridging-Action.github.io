# Translation as a Bridging Action: Transferring Manipulation Skills from Humans to Robots

Project page for *Translation as a Bridging Action: Transferring Manipulation Skills from Humans to Robots*.

This is a static site (HTML + CSS + JS, no build step) ready to be served as a
GitHub Pages project page.

## Structure

```
.
├── index.html              # Page entry (GitHub Pages serves this at the repo root)
├── static/
│   ├── css/style.css       # Styles (color variables live in :root at the top)
│   ├── js/main.js          # Carousels and small interactions
│   └── images/             # Figures used by the page (PNG)
├── mp4/                    # Robot rollout demos
├── mp4_hand/               # Human demonstration demos
├── mp4_action_bridge_vis/  # Bridging-action visualization clips
├── build_standalone.py     # Bundle everything into one offline HTML file
├── .nojekyll               # Tell GitHub Pages to serve files as-is
└── README.md
```

## Local preview

The page loads local images/videos, so serve it over a tiny HTTP server
instead of opening `index.html` directly:

```bash
python3 -m http.server 8123
# open http://localhost:8123/index.html
```

## Deploy to GitHub Pages

1. Push this directory to a GitHub repository.
2. In **Settings → Pages**, set the source to the `main` branch, root (`/`).
3. The page will be served at `https://<user>.github.io/<repo>/`.

The included `.nojekyll` file ensures GitHub Pages serves the `static/` assets
without Jekyll processing.

## Offline single-file build

To produce a single self-contained `Cam3D_ProjectPage.html` (CSS, JS, images and
videos all inlined) that can be opened by double-clicking and shared offline:

```bash
pip3 install Pillow
python3 build_standalone.py
```

Output: `Cam3D_ProjectPage.html` in this directory. Image compression settings
(`MAX_W`, `JPEG_Q`) are at the top of `build_standalone.py`.
