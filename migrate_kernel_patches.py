#!/usr/bin/env python3
import re
from pathlib import Path
from datetime import datetime

def extract_version(filename):
    match = re.search(r'v(\d+\.\d+)', filename)
    return match.group(1) if match else 'N/A'

def should_drop(filename, version):
    if version == 'N/A':
        return False, "No version tag"
    try:
        major, minor = map(int, version.split('.'))
        if major == 5 and minor >= 16:
            return True, f"In upstream v{version}"
        if major == 6 and minor <= 6:
            return True, f"In kernel v{version}"
        if major > 6:
            return True, f"Future v{version}"
    except:
        pass
    return False, "Needs check"

output_dir = Path('kavia-docs/migration-outputs')
output_dir.mkdir(parents=True, exist_ok=True)

generic = Path('target/linux/generic')
categories = [
    ('backport-5.15', 'backport-6.6'),
    ('pending-5.15', 'pending-6.6'),
    ('hack-5.15', 'hack-6.6')
]

results = {}
for src, dst in categories:
    src_path = generic / src
    patches = sorted(src_path.glob('*.patch'))
    results[src] = []
    
    for patch in patches:
        version = extract_version(patch.name)
        if 'backport' in src:
            drop, reason = should_drop(patch.name, version)
            disp = 'DROP' if drop else 'MIGRATE'
        else:
            disp = 'MIGRATE'
            reason = f'Port to {dst}'
        
        results[src].append({
            'file': patch.name,
            'disp': disp,
            'ver': version,
            'reason': reason
        })
    
    print(f"Analyzed {len(patches)} patches in {src}")

summary_file = output_dir / 'migration_summary.md'
with open(summary_file, 'w') as f:
    f.write("# Kernel Patch Migration Summary: 5.15 -> 6.6\n\n")
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    total = sum(len(results[k]) for k in results)
    drops = sum(1 for k in results for r in results[k] if r['disp'] == 'DROP')
    
    f.write("## Summary Statistics\n\n")
    f.write(f"- Total patches: {total}\n")
    f.write(f"- Backport: {len(results['backport-5.15'])}\n")
    f.write(f"- Pending: {len(results['pending-5.15'])}\n")
    f.write(f"- Hack: {len(results['hack-5.15'])}\n")
    f.write(f"- DROP (merged): {drops}\n")
    f.write(f"- MIGRATE: {total - drops}\n\n")
    
    f.write("## Backport Patches\n\n")
    f.write("| # | Filename | Disposition | Version | Reason |\n")
    f.write("|---|----------|-------------|---------|--------|\n")
    for i, r in enumerate(results['backport-5.15'], 1):
        f.write(f"| {i} | `{r['file']}` | **{r['disp']}** | {r['ver']} | {r['reason']} |\n")
    
    f.write("\n## Pending Patches\n\n")
    f.write("| # | Filename | Disposition | Version |\n")
    f.write("|---|----------|-------------|---------|\n")
    for i, r in enumerate(results['pending-5.15'], 1):
        f.write(f"| {i} | `{r['file']}` | **{r['disp']}** | {r['ver']} |\n")
    
    f.write("\n## Hack Patches\n\n")
    f.write("| # | Filename | Disposition |\n")
    f.write("|---|----------|-------------|\n")
    for i, r in enumerate(results['hack-5.15'], 1):
        f.write(f"| {i} | `{r['file']}` | **{r['disp']}** |\n")

print(f"\nSummary written to: {summary_file}")

# Create manual review list
review_file = output_dir / 'manual_review_list.md'
with open(review_file, 'w') as f:
    f.write("# Patches Requiring Manual Review\n\n")
    
    migrate_backports = [r for r in results['backport-5.15'] if r['disp'] == 'MIGRATE']
    f.write(f"## Backport Patches to Verify ({len(migrate_backports)})\n\n")
    for i, r in enumerate(migrate_backports, 1):
        f.write(f"{i}. `{r['file']}` - {r['reason']}\n")
    
    f.write(f"\n## Pending Patches to Rebase ({len(results['pending-5.15'])})\n\n")
    for i, r in enumerate(results['pending-5.15'], 1):
        f.write(f"{i}. `{r['file']}`\n")
    
    f.write(f"\n## Hack Patches to Port ({len(results['hack-5.15'])})\n\n")
    for i, r in enumerate(results['hack-5.15'], 1):
        f.write(f"{i}. `{r['file']}`\n")

print(f"Manual review list: {review_file}")

for src, dst in categories:
    dst_path = generic / dst
    dst_path.mkdir(exist_ok=True)
    readme = dst_path / 'README.md'
    with open(readme, 'w') as f:
        f.write(f"# {dst}\n\n")
        f.write(f"Migrated from {src} for kernel 6.6\n\n")
        f.write("**Status**: Ready for patch migration\n")
    print(f"Created: {dst_path}")

print("\nMigration analysis complete!")
