#!/usr/bin/env python3
"""
Kernel Patch Migration Script: 5.15 -> 6.6
Migrates OpenWrt generic patches from kernel 5.15 to 6.6
"""

import os
import re
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class PatchMigrator:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.generic_dir = self.base_dir / "target/linux/generic"
        
        # Source directories
        self.backport_515 = self.generic_dir / "backport-5.15"
        self.pending_515 = self.generic_dir / "pending-5.15"
        self.hack_515 = self.generic_dir / "hack-5.15"
        
        # Target directories
        self.backport_66 = self.generic_dir / "backport-6.6"
        self.pending_66 = self.generic_dir / "pending-6.6"
        self.hack_66 = self.generic_dir / "hack-6.6"
        
        # Results tracking
        self.results = {
            'backport': [],
            'pending': [],
            'hack': []
        }
        self.manual_review = []
        
    def extract_patch_info(self, patch_file: Path) -> Dict:
        """Extract metadata from patch file"""
        info = {
            'filename': patch_file.name,
            'path': str(patch_file),
            'subject': '',
            'upstream_version': None,
            'files_modified': [],
            'description': ''
        }
        
        try:
            with open(patch_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Extract subject
            subject_match = re.search(r'^Subject:\s*(.+)$', content, re.MULTILINE)
            if subject_match:
                info['subject'] = subject_match.group(1).strip()
            
            # Extract upstream version from filename
            version_match = re.search(r'v(\d+\.\d+)', patch_file.name)
            if version_match:
                info['upstream_version'] = version_match.group(1)
            
            # Extract files being modified
            diff_files = re.findall(r'^\+\+\+\s+[ab]/([\S]+)', content, re.MULTILINE)
            info['files_modified'] = list(set(diff_files))
            
            # Extract description from patch header
            desc_lines = []
            in_header = False
            for line in content.split('\n'):
                if line.startswith('---'):
                    break
                if line.startswith('From:') or line.startswith('Subject:'):
                    in_header = True
                    continue
                if in_header and line.strip():
                    desc_lines.append(line.strip())
            info['description'] = ' '.join(desc_lines[:3])
            
        except Exception as e:
            print(f"Warning: Could not parse {patch_file.name}: {e}")
        
        return info
    
    def check_upstream_merged(self, patch_info: Dict) -> Tuple[bool, str]:
        """
        Check if patch was merged upstream between 5.16 and 6.6
        Returns (is_merged, reason)
        """
        # Check if patch has version tag indicating it's already in a specific version
        if patch_info['upstream_version']:
            version = patch_info['upstream_version']
            major, minor = map(int, version.split('.'))
            
            # If version is between 5.16 and 6.6, it's already merged
            if (major == 5 and minor >= 16) or (major == 6 and minor <= 6):
                return True, f"Already in upstream {version}"
            
            # If version is exactly 6.6 or later, no need to backport
            if major >= 6 and minor >= 6:
                return True, f"Included in kernel 6.6+ (v{version})"
        
        # Heuristic: backport patches with high version numbers are likely merged
        filename = patch_info['filename']
        if 'v6.' in filename or 'v5.1' in filename:
            version_in_name = re.search(r'v(5\.\d+|6\.\d+)', filename)
            if version_in_name:
                ver = version_in_name.group(1)
                major, minor = map(int, ver.split('.'))
                if major >= 6:
                    return True, f"Backport from v{ver} (merged upstream)"
        
        return False, "Unknown - needs verification"
    
    def analyze_backport_patches(self):
        """Analyze backport-5.15 patches"""
        print("\n=== Analyzing backport-5.15 patches ===")
        patches = sorted(self.backport_515.glob("*.patch"))
        
        for patch in patches:
            info = self.extract_patch_info(patch)
            is_merged, reason = self.check_upstream_merged(info)
            
            result = {
                'filename': info['filename'],
                'subject': info['subject'],
                'disposition': 'DROP' if is_merged else 'MIGRATE',
                'reason': reason,
                'files_modified': info['files_modified'],
                'upstream_version': info['upstream_version']
            }
            
            self.results['backport'].append(result)
            
            if not is_merged:
                self.manual_review.append({
                    'category': 'backport',
                    'patch': info['filename'],
                    'reason': 'Needs verification if merged in 5.16-6.6'
                })
        
        print(f"Analyzed {len(patches)} backport patches")
    
    def analyze_pending_patches(self):
        """Analyze pending-5.15 patches"""
        print("\n=== Analyzing pending-5.15 patches ===")
        patches = sorted(self.pending_515.glob("*.patch"))
        
        for patch in patches:
            info = self.extract_patch_info(patch)
            
            # Check if patch has upstream version tag
            has_upstream_tag = info['upstream_version'] is not None
            
            result = {
                'filename': info['filename'],
                'subject': info['subject'],
                'disposition': 'MIGRATE',
                'reason': 'Port to pending-6.6 (needs rebase check)',
                'files_modified': info['files_modified'],
                'upstream_version': info['upstream_version']
            }
            
            # If it has v6.3+ tag, might be merged
            if has_upstream_tag:
                ver = info['upstream_version']
                if ver.startswith('6.'):
                    major, minor = map(int, ver.split('.'))
                    if minor >= 3:
                        result['disposition'] = 'CHECK'
                        result['reason'] = f'Has v{ver} tag - verify if merged in 6.6'
            
            self.results['pending'].append(result)
            
            self.manual_review.append({
                'category': 'pending',
                'patch': info['filename'],
                'reason': 'Needs rebase testing against 6.6'
            })
        
        print(f"Analyzed {len(patches)} pending patches")
    
    def analyze_hack_patches(self):
        """Analyze hack-5.15 patches"""
        print("\n=== Analyzing hack-5.15 patches ===")
        patches = sorted(self.hack_515.glob("*.patch"))
        
        for patch in patches:
            info = self.extract_patch_info(patch)
            
            result = {
                'filename': info['filename'],
                'subject': info['subject'],
                'disposition': 'MIGRATE',
                'reason': 'Hack patch - verify still needed in 6.6',
                'files_modified': info['files_modified']
            }
            
            self.results['hack'].append(result)
            
            self.manual_review.append({
                'category': 'hack',
                'patch': info['filename'],
                'reason': 'Verify hack is still needed and port to 6.6'
            })
        
        print(f"Analyzed {len(patches)} hack patches")
    
    def generate_summary_table(self, output_file: str):
        """Generate summary table of all patches"""
        print(f"\n=== Generating summary table: {output_file} ===")
        
        with open(output_file, 'w') as f:
            f.write("# Kernel Patch Migration Summary: 5.15 -> 6.6\n\n")
            f.write(f"Generated: {subprocess.check_output(['date']).decode().strip()}\n\n")
            
            # Summary statistics
            total = sum(len(self.results[cat]) for cat in self.results)
            drops = sum(1 for cat in self.results for r in self.results[cat] if r['disposition'] == 'DROP')
            migrates = sum(1 for cat in self.results for r in self.results[cat] if r['disposition'] == 'MIGRATE')
            checks = sum(1 for cat in self.results for r in self.results[cat] if r['disposition'] == 'CHECK')
            
            f.write("## Summary Statistics\n\n")
            f.write(f"- **Total patches analyzed**: {total}\n")
            f.write(f"- **DROP (merged upstream)**: {drops}\n")
            f.write(f"- **MIGRATE (port to 6.6)**: {migrates}\n")
            f.write(f"- **CHECK (needs verification)**: {checks}\n")
            f.write(f"- **Manual review items**: {len(self.manual_review)}\n\n")
            
            # Backport patches
            f.write("## Backport Patches (backport-5.15 -> backport-6.6)\n\n")
            f.write(f"Total: {len(self.results['backport'])} patches\n\n")
            f.write("| # | Filename | Disposition | Upstream Ver | Reason |\n")
            f.write("|---|----------|-------------|--------------|--------|\n")
            for i, r in enumerate(self.results['backport'], 1):
                upstream = r.get('upstream_version', 'N/A')
                f.write(f"| {i} | `{r['filename']}` | **{r['disposition']}** | {upstream} | {r['reason']} |\n")
            
            # Pending patches
            f.write("\n## Pending Patches (pending-5.15 -> pending-6.6)\n\n")
            f.write(f"Total: {len(self.results['pending'])} patches\n\n")
            f.write("| # | Filename | Disposition | Upstream Ver | Reason |\n")
            f.write("|---|----------|-------------|--------------|--------|\n")
            for i, r in enumerate(self.results['pending'], 1):
                upstream = r.get('upstream_version', 'N/A')
                f.write(f"| {i} | `{r['filename']}` | **{r['disposition']}** | {upstream} | {r['reason']} |\n")
            
            # Hack patches
            f.write("\n## Hack Patches (hack-5.15 -> hack-6.6)\n\n")
            f.write(f"Total: {len(self.results['hack'])} patches\n\n")
            f.write("| # | Filename | Disposition | Reason |\n")
            f.write("|---|----------|-------------|--------|\n")
            for i, r in enumerate(self.results['hack'], 1):
                f.write(f"| {i} | `{r['filename']}` | **{r['disposition']}** | {r['reason']} |\n")
        
        print(f"Summary table written to {output_file}")
    
    def generate_manual_review_list(self, output_file: str):
        """Generate list of patches needing manual review"""
        print(f"\n=== Generating manual review list: {output_file} ===")
        
        with open(output_file, 'w') as f:
            f.write("# Patches Requiring Manual Review\n\n")
            f.write(f"Total items: {len(self.manual_review)}\n\n")
            
            by_category = {}
            for item in self.manual_review:
                cat = item['category']
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(item)
            
            for category in ['backport', 'pending', 'hack']:
                if category in by_category:
                    items = by_category[category]
                    f.write(f"\n## {category.upper()} ({len(items)} patches)\n\n")
                    for i, item in enumerate(items, 1):
                        f.write(f"{i}. **{item['patch']}**\n")
                        f.write(f"   - Reason: {item['reason']}\n\n")
        
        print(f"Manual review list written to {output_file}")
    
    def create_placeholder_patches(self):
        """Create placeholder structure for 6.6 patches"""
        print("\n=== Creating 6.6 patch directory structure ===")
        
        # Create directories
        self.backport_66.mkdir(exist_ok=True)
        self.pending_66.mkdir(exist_ok=True)
        self.hack_66.mkdir(exist_ok=True)
        
        # Create README files
        for dir_path, source_name in [
            (self.backport_66, 'backport-5.15'),
            (self.pending_66, 'pending-5.15'),
            (self.hack_66, 'hack-5.15')
        ]:
            readme = dir_path / "README.md"
            with open(readme, 'w') as f:
                f.write(f"# {dir_path.name}\n\n")
                f.write(f"Patches migrated from {source_name} for kernel 6.6\n\n")
                f.write("**Status**: Placeholder structure created\n\n")
                f.write("**Next steps**:\n")
                f.write("1. Review migration summary table\n")
                f.write("2. For MIGRATE patches: rebase against 6.6 kernel source\n")
                f.write("3. Test each patch for conflicts\n")
                f.write("4. Update patches that need adjustments\n")
        
        print(f"Created directories: {self.backport_66.name}, {self.pending_66.name}, {self.hack_66.name}")
    
    def generate_migration_metadata(self, output_file: str):
        """Generate JSON metadata for migration tracking"""
        metadata = {
            'migration_date': subprocess.check_output(['date', '+%Y-%m-%d']).decode().strip(),
            'source_kernel': '5.15',
            'target_kernel': '6.6',
            'statistics': {
                'backport': {
                    'total': len(self.results['backport']),
                    'drop': sum(1 for r in self.results['backport'] if r['disposition'] == 'DROP'),
                    'migrate': sum(1 for r in self.results['backport'] if r['disposition'] == 'MIGRATE')
                },
                'pending': {
                    'total': len(self.results['pending']),
                    'migrate': sum(1 for r in self.results['pending'] if r['disposition'] == 'MIGRATE')
                },
                'hack': {
                    'total': len(self.results['hack']),
                    'migrate': sum(1 for r in self.results['hack'] if r['disposition'] == 'MIGRATE')
                }
            },
            'results': self.results,
            'manual_review_count': len(self.manual_review)
        }
        
        with open(output_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Migration metadata written to {output_file}")
    
    def run(self, output_dir: str):
        """Run the complete migration analysis"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        print("="*60)
        print("Kernel Patch Migration: 5.15 -> 6.6")
        print("="*60)
        
        # Analyze all patch categories
        self.analyze_backport_patches()
        self.analyze_pending_patches()
        self.analyze_hack_patches()
        
        # Generate outputs
        self.generate_summary_table(str(output_path / "migration_summary.md"))
        self.generate_manual_review_list(str(output_path / "manual_review_list.md"))
        self.generate_migration_metadata(str(output_path / "migration_metadata.json"))
        
        # Create 6.6 directory structure
        self.create_placeholder_patches()
        
        print("\n" + "="*60)
        print("Migration analysis complete!")
        print("="*60)
        print(f"\nOutput files generated in: {output_dir}")
        print(f"- migration_summary.md")
        print(f"- manual_review_list.md")
        print(f"- migration_metadata.json")
        print(f"\nPatch directories created:")
        print(f"- {self.backport_66}")
        print(f"- {self.pending_66}")
        print(f"- {self.hack_66}")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: migrate_patches_5.15_to_6.6.py <output_directory>")
        sys.exit(1)
    
    output_dir = sys.argv[1]
    
    # Detect base directory
    script_dir = Path(__file__).parent.parent
    
    migrator = PatchMigrator(str(script_dir))
    migrator.run(output_dir)

if __name__ == '__main__':
    main()
