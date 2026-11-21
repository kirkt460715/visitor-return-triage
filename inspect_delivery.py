"""查看本次交接的原始记录。"""
import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


def read_table(name):
    """读取交接文件中的原始行。"""
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="查阅交接文件")
    parser.add_argument("file", nargs="?", choices=sorted(p.name for p in DATA.glob("*.json")))
    args = parser.parse_args()
    if args.file:
        records = read_table(args.file)
        print(json.dumps(records[0] if records else None, ensure_ascii=False, indent=2))
        return
    for file in sorted(DATA.glob("*.json")):
        print(f"{file.name}  {len(read_table(file.name))} 行")


if __name__ == "__main__":
    main()
