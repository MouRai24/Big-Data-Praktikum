import argparse, glob, yaml
from pathlib import Path
from run_experiment import dispatch

def main():
    """Run all YAML configs in a suite directory (music or wdc)."""
    p = argparse.ArgumentParser()
    p.add_argument("--suite", choices=["music","wdc"], required=True)
    args = p.parse_args()
    base = Path("configs")/args.suite
    files = sorted(glob.glob(str(base/"*.yaml")))
    for f in files:
        cfg = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
        dispatch(cfg)

if __name__ == "__main__":
    main()
