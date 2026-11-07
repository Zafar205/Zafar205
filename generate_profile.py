"""Build the light and dark GitHub profile cards from ascii-art.png."""

from base64 import b64encode
from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
PORTRAIT = b64encode((ROOT / "ascii-art.png").read_bytes()).decode("ascii")


def card(dark: bool) -> str:
    background, text, muted, accent, label, border = (
        ("#0d1117", "#e6edf3", "#8b949e", "#58a6ff", "#ffa657", "#30363d")
        if dark else
        ("#f6f8fa", "#24292f", "#57606a", "#0969da", "#9a6700", "#d0d7de")
    )

    def line(y: int, name: str, value: str) -> str:
        return (
            f'<text x="566" y="{y}" class="label">{escape(name)}</text>'
            f'<text x="720" y="{y}" class="value">{escape(value)}</text>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1317" height="728" viewBox="0 0 1317 728" role="img" aria-labelledby="title desc">
  <title id="title">Muhammad Zafar's GitHub profile</title>
  <desc id="desc">ASCII portrait beside details about Muhammad Zafar, a computer engineering student and full stack developer in Karachi.</desc>
  <style>
    .heading {{ fill: {accent}; font-size: 24px; font-weight: 700; }}
    .section {{ fill: {accent}; font-size: 21px; font-weight: 700; }}
    .label {{ fill: {label}; font-size: 18px; font-weight: 600; }}
    .value {{ fill: {text}; font-size: 18px; }}
    .muted {{ fill: {muted}; font-size: 17px; }}
    text {{ font-family: Consolas, Menlo, 'DejaVu Sans Mono', monospace; }}
  </style>
  <defs>
    <clipPath id="portrait"><rect x="0" y="0" width="527" height="728" /></clipPath>
    <filter id="invert"><feComponentTransfer><feFuncR type="table" tableValues="1 0" /><feFuncG type="table" tableValues="1 0" /><feFuncB type="table" tableValues="1 0" /></feComponentTransfer></filter>
  </defs>
  <rect width="1317" height="728" rx="8" fill="{background}" />
  <g clip-path="url(#portrait)">
    <image href="data:image/png;base64,{PORTRAIT}" x="0" y="0" width="527" height="728" preserveAspectRatio="xMidYMid slice"{' filter="url(#invert)"' if not dark else ''} />
  </g>
  <path d="M527 0v728" stroke="{border}" />
  <text x="566" y="49" class="heading">Zafar205@github</text>
  <path d="M566 70h711" stroke="{border}" />
  {line(113, 'Name', 'Muhammad Zafar')}
  {line(155, 'Location', 'Karachi, Pakistan')}
  {line(197, 'Role', 'Full Stack Developer')}
  {line(239, 'Education', 'Computer Engineering')}
  <text x="720" y="268" class="muted">Habib University</text>
  {line(310, 'Focus', 'ERP, FinTech, SaaS')}
  {line(352, 'Stack', 'TypeScript, Python, React, Next.js')}
  <text x="720" y="381" class="muted">Node.js, PostgreSQL, Docker</text>
  <text x="566" y="428" class="section">Contact</text>
  <path d="M566 444h711" stroke="{border}" />
  {line(480, 'Website', 'zafar.business')}
  {line(523, 'LinkedIn', 'linkedin.com/in/zafar2062005')}
  {line(566, 'X', '@Zafar205')}
  {line(609, 'Phone', '+92 326 5908446')}
  {line(652, 'WhatsApp', '+92 326 5908446')}
  {line(695, 'GitHub', 'github.com/Zafar205')}
  <rect x="0.5" y="0.5" width="1316" height="727" rx="8" fill="none" stroke="{border}" />
</svg>
'''


for filename, dark in (("dark_mode.svg", True), ("light_mode.svg", False)):
    (ROOT / filename).write_text(card(dark), encoding="utf-8")
