from pathlib import Path
import sys
import traceback

from weasyprint import HTML
from scripts.table_render import render_tools_html

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BASE_DIR = ROOT
OUTPUT = BASE_DIR / "pdf_table" / "tools-map.pdf"


def main() -> None:
    html_content = render_tools_html()

    css = """
    @page {
        size: A4 landscape;
        margin: 2mm 10mm 12mm 2mm;
        @bottom-right {
            content: element(page-footer);
        }
        @bottom-left {
            content: element(page-footer_copyright);
        }
    }

    html, body {
        font-family: Montserrat;
        font-size: 6.5pt;
        font-kerning: normal;
        line-height: 1.1;
        transform-origin: top left;
        text-rendering: optimizeLegibility;
        letter-spacing: 0;
        word-spacing: 0;
        margin: 0;
        padding: 0;
    }

    table.tools-table {
        border-collapse: collapse;
        border: 1px solid #1953ff;
        margin-bottom: 0;
        width: 100%;
    }

    th, td {
        border: 1px solid #1953ff;
        padding: 1px 2px;
        word-wrap: break-word;
        overflow-wrap: auto;
    }

    th {
        background: #1953ff;
        color: #ffffff;
        font-weight: bold;
    }

    tbody {
        page-break-before: auto;
        page-break-after: auto;
    }

    td.auto-section-name {
        font-weight: 700;
        color: #1953ff;
        white-space: nowrap;
    }

    .page-footer {
        position: running(page-footer);
        display: flex;
        align-items: center;
        gap: 2mm;
        padding: 0;
    }

    .page-footer_copyright {
        position: running(page-footer_copyright);
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 2mm;
        font-size: 7pt;
        padding: 0;
    }

    .footer-logos {
        display: flex;
        align-items: center;
        gap: 2mm;
        margin-left: auto;
    }

    .footer-logo {
        height: 10mm;
    }

    .footer-copyright {
        font-size: 7pt;
        color: black;
        white-space: nowrap;
        margin-right: auto;
    }
    """

    full_html = f"""
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>{css}</style>
  </head>
  <body>
      <div class="page-footer">
        <div class="footer-logos">
          <img src="docs/assets/logotype/site/logo_pdf.png" class="footer-logo" />
          <img src="docs/assets/logotype/site/FDSO_logo.png" class="footer-logo" />
          <img src="docs/assets/logotype/site/LANIT_logo.png" class="footer-logo" />
        </div>
      </div>
      <div class="page-footer_copyright">
        <div class="footer-copyright">© AppSecTA &amp; FinDevSecOps</div>
      </div>

      {html_content}
  </body>
</html>
"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(str(OUTPUT))
    print(f"PDF saved to {OUTPUT}")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
