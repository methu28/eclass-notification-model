"""Fetch and preserve the complete original Mesa example WITHOUT modifying it.

Run on an internet-connected computer with git installed:
    python scripts/fetch_source_example.py

This is intentionally not executed in the provided archive because the build
sandbox cannot reach GitHub. Never claim the example has been included until
this script succeeds and you commit its output to the shared repository.
"""
from __future__ import annotations

import argparse
import datetime as dt
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/projectmesa/mesa.git"
UPSTREAM_WEB = "https://github.com/projectmesa/mesa"
CANDIDATES = (
    "mesa/examples/basic/boltzmann_wealth_model",
    "examples/basic/boltzmann_wealth_model",
    "mesa/examples/boltzmann_wealth_model",
)


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="main", help="Upstream branch or tag; default main")
    args = parser.parse_args()
    destination = ROOT / "src" / "mesa_source" / "boltzmann_wealth_model"
    if destination.exists():
        raise SystemExit(f"Source folder already exists: {destination}. Refusing to overwrite.")
    with tempfile.TemporaryDirectory(prefix="mesa_source_") as temp:
        checkout = Path(temp) / "mesa"
        print(f"Cloning Mesa from {UPSTREAM} (ref={args.ref})...")
        subprocess.run(["git", "clone", "--depth", "1", "--branch", args.ref, UPSTREAM, str(checkout)], check=True)
        commit = run("git", "rev-parse", "HEAD", cwd=checkout)
        src = next((checkout / rel for rel in CANDIDATES if (checkout / rel).is_dir()), None)
        if src is None:
            raise SystemExit("Could not find the Boltzmann example. Check upstream layout and update CANDIDATES.")
        shutil.copytree(src, destination)  # byte-for-byte copy of all example files
        upstream_license = checkout / "LICENSE"
        if upstream_license.exists():
            shutil.copy2(upstream_license, ROOT / "src" / "mesa_source" / "UPSTREAM_LICENSE")
        source_note = ROOT / "src" / "mesa_source" / "SOURCE.md"
        source_note.write_text(
            "# Mesa source example provenance\n\n"
            f"- Project: Mesa, Boltzmann Wealth Model example\n"
            f"- Repository: {UPSTREAM_WEB}\n"
            f"- Copied source path: `{src.relative_to(checkout).as_posix()}`\n"
            f"- Git commit: `{commit}`\n"
            f"- Ref requested: `{args.ref}`\n"
            f"- Retrieved (UTC): {dt.datetime.now(dt.timezone.utc).isoformat()}\n"
            "- Original source directory copied unchanged into `boltzmann_wealth_model/`.\n"
            "- Upstream license copied to `UPSTREAM_LICENSE` when available.\n"
            "- Before submission: verify the original example's run command against its own README.\n",
            encoding="utf-8",
        )
        print(f"Copied complete example to {destination}")
        print(f"Recorded commit {commit} in {source_note}")
        print("Review the original example README and run it before submission.")


if __name__ == "__main__":
    main()
