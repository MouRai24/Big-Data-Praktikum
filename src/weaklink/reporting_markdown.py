from pathlib import Path
from typing import Dict

class MDWriter:
    """Minimal helper to write experiment results into a Markdown file."""
    def __init__(self, path: str):
        self.path = Path(path)
        self.buf = []

    def title(self, text: str):
        """Add a level-1 title to the report."""
        self.buf.append(f"# {text}\n")

    def section(self, text: str):
        """Add a level-2 section."""
        self.buf.append(f"## {text}\n")

    def bullets(self, kv: Dict[str, str]):
        """Add key-value bullets."""
        for k,v in kv.items():
            self.buf.append(f"- {k}: {v}\n")
        self.buf.append("\n")

    def codeblock(self, text: str):
        """Add a fenced code block."""
        self.buf.append("```\n")
        self.buf.append(text.strip() + "\n")
        self.buf.append("```\n\n")

    def line(self, text: str):
        """Add a single line."""
        self.buf.append(text + "\n")

    def save(self):
        """Write buffer to disk."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("".join(self.buf), encoding="utf-8")
