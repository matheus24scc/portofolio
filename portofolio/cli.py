import argparse, json, os
from portofolio import core

def main(argv=None):
    p = argparse.ArgumentParser(prog="portofolio", description="Gera/sobe portfofolio estatico.")
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build"); b.add_argument("data"); b.add_argument("--out", default="index.html")
    sv = sub.add_parser("serve"); sv.add_argument("--port", type=int, default=8000); sv.add_argument("--dir", default=".")
    args = p.parse_args(argv)
    if args.cmd == "build":
        data = json.load(open(args.data))
        print("gerado:", core.build(data, args.out))
    else:
        core.serve(args.dir, args.port)
    return 0
