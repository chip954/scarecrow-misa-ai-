# SPDX-License-Identifier: Apache-2.0
# (c) 2025 Brian Warren

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .ledger_read import latest_ledger, pretty_print_tail
from .ledger import PromisesLedger


def _cmd_ledger_latest(args: argparse.Namespace) -> int:
    path = latest_ledger(args.dir)
    if not path:
        print("No ledger files found.", file=sys.stderr)
        return 1
    print(str(path))
    return 0


def _cmd_ledger_tail(args: argparse.Namespace) -> int:
    path = latest_ledger(args.dir) if args.path is None else Path(args.path)
    if not path or not path.exists():
        print("Ledger file not found.", file=sys.stderr)
        return 1
    n = args.n if args.n and args.n > 0 else 10
    print(pretty_print_tail(path, n=n))
    return 0


def _cmd_ledger_verify(args: argparse.Namespace) -> int:
    path = latest_ledger(args.dir) if args.path is None else Path(args.path)
    if not path or not path.exists():
        print("Ledger file not found.", file=sys.stderr)
        return 1
    # Minimal verify via PromisesLedger API:
    # Create a temp PromisesLedger pointing to the same file by “attaching” state.
    # Easiest approach: instantiate and monkey-attach file (read-only verify).
    led = PromisesLedger(base_dir=Path(args.dir))
    # attach file
    led._path = path  # type: ignore[attr-defined]
    ok, bad = led.verify_chain()
    print("True" if ok else f"False (first bad index: {bad})")
    return 0 if ok else 2


def main() -> int:
    parser = argparse.ArgumentParser(prog="scarecrow-misa", description="Scarecrow/MISA utilities")
    sub = parser.add_subparsers(dest="cmd")

    p_latest = sub.add_parser("ledger-latest", help="Print path of the most recent ledger file")
    p_latest.add_argument("--dir", default="ledger", help="Ledger directory (default: ledger)")
    p_latest.set_defaults(func=_cmd_ledger_latest)

    p_tail = sub.add_parser("ledger", help="Ledger tools")
    p_tail_sub = p_tail.add_subparsers(dest="subcmd")

    p_tail_tail = p_tail_sub.add_parser("tail", help="Show the last N entries of a ledger")
    p_tail_tail.add_argument("n", nargs="?", type=int, default=10, help="Number of entries (default 10)")
    p_tail_tail.add_argument("--dir", default="ledger", help="Ledger directory (default: ledger)")
    p_tail_tail.add_argument("--path", default=None, help="Explicit path to a ledger file")
    p_tail_tail.set_defaults(func=_cmd_ledger_tail)

    p_tail_verify = p_tail_sub.add_parser("verify", help="Verify the latest (or given) ledger chain")
    p_tail_verify.add_argument("--dir", default="ledger", help="Ledger directory (default: ledger)")
    p_tail_verify.add_argument("--path", default=None, help="Explicit path to a ledger file")
    p_tail_verify.set_defaults(func=_cmd_ledger_verify)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
