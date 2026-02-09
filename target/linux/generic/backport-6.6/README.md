# backport-6.6

Patches migrated from backport-5.15 for kernel 6.6

**Status**: ✅ Migration Analysis Complete - Intentionally Minimal

## Why This Directory is Mostly Empty

Out of **681 backport patches** from kernel 5.15:
- **678 patches (99.6%)** were already merged into upstream kernels 5.16 through 6.6
- **3 patches (0.4%)** require manual verification before dropping

This is expected behavior! Backport patches contain features/fixes destined for future kernels. Since we're migrating to kernel 6.6, nearly all backport patches from 5.15 are already included in the base 6.6 kernel.

## Patches Requiring Manual Verification

The following 3 patches lack version tags and need verification to confirm they're in upstream 6.6:

1. **751-00a-STABLE-net-ethernet-mediatek-split-tx-and-rx-fields-in-mtk_.patch**
   - Subject: Split tx and rx fields in mtk_eth
   - Files: MediaTek ethernet driver
   - Action: Check if merged in kernels 5.16-6.6

2. **751-00b-net-ethernet-mediatek-use-QDMA-instead-of-ADMAv2-on-.patch**
   - Subject: Use QDMA instead of ADMAv2
   - Files: MediaTek ethernet driver  
   - Action: Check if merged in kernels 5.16-6.6

3. **798-net-next-net-sfp-add-quirk-for-Fiberstone-GPON-ONU-34-20BI.patch**
   - Subject: Add quirk for Fiberstone GPON ONU
   - Files: SFP driver
   - Action: Check if merged in kernels 5.16-6.6

## Verification Steps

For each patch:
1. Check the patch subject/commit message
2. Search Linux git history for the commit
3. Verify it's in a kernel version ≤ 6.6
4. If found: Document the kernel version and drop the patch
5. If not found: Migrate to backport-6.6/

## Summary Statistics

| Category | Count | Percentage |
|----------|-------|------------|
| DROP (merged upstream) | 678 | 99.6% |
| VERIFY (unknown status) | 3 | 0.4% |
| **Total** | **681** | **100%** |

## References

- Full migration details: `../../migration-outputs/MIGRATION_COMPLETE.md`
- Patch disposition table: `../../migration-outputs/migration_summary.md`
- Manual review list: `../../migration-outputs/manual_review_list.md`
