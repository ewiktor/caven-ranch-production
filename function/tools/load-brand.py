#!/usr/bin/env python3
"""Load a DRAPER app brand export into a template repo — deterministic file placement.

Usage:  python3 "function/tools/load-brand.py" <export-dir> [template-dir=.]

Run from the template repo root (or pass the template dir as the 2nd arg). This does the
mechanical half of `load brand.md` — every file placed the same way every time, nothing
skipped. It does NOT download assets: the .md files carry CDN links (that's the asset of
record); local asset files are copied when the export bundled them. After it runs, do the
judgment half from `load brand.md`: fill 00 brand.md's brand section from the strategy,
and ask whether there's an exploration board.
"""
import sys, os, re, shutil, glob

def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.strip().lower()).strip('-')

def ensure(d):
    os.makedirs(d, exist_ok=True)

def copy_md_and_assets(src_folder, dst_folder, skip=("context.md",)):
    ensure(dst_folder); ensure(os.path.join(dst_folder, "assets"))
    nmd = nas = 0
    for p in glob.glob(os.path.join(src_folder, "*.md")):
        if os.path.basename(p).lower() in skip:
            continue
        shutil.copy2(p, dst_folder); nmd += 1
    for p in glob.glob(os.path.join(src_folder, "assets", "*")):
        if os.path.isfile(p):
            shutil.copy2(p, os.path.join(dst_folder, "assets")); nas += 1
    return nmd, nas

def parse_commentary(context_path):
    """references/context.md and explorations/context.md hold per-item user commentary.
    Returns {slug(title): commentary-text-before-the-CDN-link}."""
    out = {}
    if not os.path.exists(context_path):
        return out
    text = open(context_path, encoding="utf-8").read()
    for block in re.split(r'^###\s+', text, flags=re.M)[1:]:
        lines = block.splitlines()
        title = lines[0].strip().strip('*').strip()
        body = "\n".join(lines[1:])
        m = re.search(r'\n\s*\[|\n\s*https?://', body)   # first markdown link / bare URL
        comment = (body[:m.start()] if m else body).strip()
        if title:
            out[slug(title)] = comment
    return out

def merge_commentary(doc_path, commentary):
    txt = open(doc_path, encoding="utf-8").read()
    if "## User context" in txt:
        return
    m = re.search(r'^#\s+(.+)$', txt, flags=re.M)
    key = slug(m.group(1)) if m else slug(os.path.splitext(os.path.basename(doc_path))[0])
    com = commentary.get(key)
    if not com:
        return
    block = f"## User context\n\n{com}\n\n"
    if "## Assets" in txt:
        txt = txt.replace("## Assets", block + "## Assets", 1)
    else:
        txt = txt.rstrip() + "\n\n" + block
    open(doc_path, "w", encoding="utf-8").write(txt)

def main():
    if len(sys.argv) < 2:
        print("usage: load-brand.py <export-dir> [template-dir]"); sys.exit(1)
    src = os.path.abspath(sys.argv[1])
    dst = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.getcwd()
    report = []

    # strategy overview -> input/01 brief (strategy).md
    pn = glob.glob(os.path.join(src, "production-notes", "*.md"))
    strat = next((p for p in pn if "strategy" in os.path.basename(p).lower()), pn[0] if pn else None)
    if strat:
        txt = open(strat, encoding="utf-8").read()
        txt = re.sub(r'^\s*\*\*Source type:\*\*.*\n', '', txt, flags=re.M)
        ensure(os.path.join(dst, "input"))
        open(os.path.join(dst, "input", "01 brief (strategy).md"), "w", encoding="utf-8").write(txt)
        report.append("strategy      -> input/01 brief (strategy).md")
    else:
        report.append("!! strategy    NOT FOUND in production-notes/")

    # knowledge
    kdst = os.path.join(dst, "06 knowledge"); ensure(kdst); n = 0
    for p in glob.glob(os.path.join(src, "knowledge", "*.md")):
        shutil.copy2(p, kdst); n += 1
    report.append(f"knowledge     {n} docs -> 06 knowledge/")

    # media
    nmd, nas = copy_md_and_assets(os.path.join(src, "media"), os.path.join(dst, "03 media"))
    report.append(f"media         {nmd} docs -> 03 media/, {nas} local assets (rest CDN-only in the docs)")

    # references + merge commentary
    rdst = os.path.join(dst, "04 references")
    nmd, nas = copy_md_and_assets(os.path.join(src, "references"), rdst)
    commentary = parse_commentary(os.path.join(src, "references", "context.md"))
    merged = 0
    for p in glob.glob(os.path.join(rdst, "*.md")):
        if os.path.basename(p).startswith("_"):
            continue
        before = open(p, encoding="utf-8").read()
        merge_commentary(p, commentary)
        if open(p, encoding="utf-8").read() != before:
            merged += 1
    report.append(f"references    {nmd} docs -> 04 references/ ({merged} got commentary merged), {nas} assets")

    # explorations -> input/explorations/ (staging for the board pass)
    nmd, nas = copy_md_and_assets(os.path.join(src, "explorations"), os.path.join(dst, "input", "explorations"))
    report.append(f"explorations  {nmd} staged -> input/explorations/, {nas} assets")

    print("LOAD COMPLETE\n" + "\n".join("  " + r for r in report))
    print("\nNext (judgment half, per load brand.md):")
    print("  1. Fill 00 brand.md's brand section from input/01 brief (strategy).md")
    print("  2. Ask the user if there's an exploration board (Figma/whiteboard) — record it in 00 brand.md")
    print("  3. Run the board pass to form expressions")

if __name__ == "__main__":
    main()
