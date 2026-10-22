"""Bundle the Switchback application into one self-contained HTML file."""
from pathlib import Path
import argparse
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / 'dist'


def module_bundle(name, exports):
    source = (GAME / name).read_text()
    source = re.sub(r'^export ', '', source, flags=re.MULTILINE)
    names = ', '.join(exports)
    return f'const {{ {names} }} = (() => {{\n{source}\nreturn {{ {names} }};\n}})();\n'


def build():
    html = (GAME / 'index.html').read_text()
    for name in ['base.css', 'switchback.css']:
        html = re.sub(r'<link rel="stylesheet" href="\./' + re.escape(name) + r'(?:\?[^\"]*)?">',
                      lambda _: '<style>\n' + (GAME / name).read_text() + '\n</style>', html)
    html = html.replace('<script type="module" src="./theme.mjs"></script>',
                        '<script type="module">\n' + (GAME / 'theme.mjs').read_text() + '\n</script>')
    app = re.sub(r'^import .*?;\n', '', (GAME / 'app.mjs').read_text(), flags=re.MULTILINE)
    code = module_bundle('model.mjs', ['transition', 'solve', 'isExit', 'editPuzzle'])
    code += module_bundle('puzzle.mjs', ['PUZZLE', 'PROPERTIES']) + app
    html = re.sub(r'<script type="module" src="\./app\.mjs(?:\?[^\"]*)?"></script>',
                  lambda _: '<script type="module">\n' + code + '\n</script>', html)
    favicon = quote((GAME / 'favicon.svg').read_text(), safe='')
    html = html.replace('href="./favicon.svg"', f'href="data:image/svg+xml,{favicon}"')
    assert 'src="./' not in html and 'import ' not in code
    return html


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(build())
    print(f'Wrote {args.output} ({args.output.stat().st_size:,} bytes)')
