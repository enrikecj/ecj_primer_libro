import os, sys
from pathlib import Path
import subprocess

# ------------------------------------------------------------
# Helper: ensure pypandoc (and pandoc) are available
# ------------------------------------------------------------
def ensure_pypandoc():
    """Install pypandoc if missing, download pandoc if not present, and return the module.
    """
    try:
        import pypandoc
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypandoc'])
        import pypandoc
    # Ensure pandoc binary is available
    try:
        pandoc_path = pypandoc.get_pandoc_path()
        if not Path(pandoc_path).exists():
            raise FileNotFoundError
    except Exception:
        # Download a bundled pandoc if not found
        print('Pandoc not found, downloading via pypandoc...', file=sys.stderr)
        pypandoc.download_pandoc()
    return pypandoc


def convert(docx_path, output_md, media_dir=None):
    """Convert a .docx file to Markdown using pandoc.

    Parameters
    ----------
    docx_path : str or Path
        Input .docx file.
    output_md : str or Path
        Destination markdown file.
    media_dir : str or Path, optional
        Directory where pandoc will extract images.
    """
    docx_path = Path(docx_path)
    if not docx_path.is_file():
        print(f'Input file {docx_path} does not exist.', file=sys.stderr)
        sys.exit(1)

    output_path = Path(output_md)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    extra_args = []
    if media_dir:
        media_path = Path(media_dir)
        media_path.mkdir(parents=True, exist_ok=True)
        extra_args = [f'--extract-media={media_path}']

    pypandoc = ensure_pypandoc()
    try:
        output = pypandoc.convert_file(str(docx_path), 'md', format='docx', extra_args=extra_args)
    except Exception as e:
        print(f'Conversion failed: {e}', file=sys.stderr)
        sys.exit(1)

    output_path.write_text(output, encoding='utf-8')
    print(f'Converted {docx_path} -> {output_md}')
    if media_dir:
        print(f'Images extracted to {media_dir}')


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        print('Usage: python convert_docx_to_md.py <input.docx> <output.md> [media_dir]')
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    media_dir = sys.argv[3] if len(sys.argv) == 4 else None
    convert(input_path, output_path, media_dir)
