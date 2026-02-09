# pending-6.6

Patches migrated from pending-5.15 for kernel 6.6

**Status**: 🔄 Sample Patches Created - Full Migration Pending

## Current State

Out of **132 pending patches** from kernel 5.15:
- **3 sample patches** have been migrated as examples ✅
- **126 patches** need to be rebased and migrated ⏳
- **6 patches** may have been merged upstream (need verification) ⚠️

## Sample Patches in This Directory

The following patches demonstrate successful migration:

1. ✅ **400-mtd-mtdsplit-support.patch**
   - OpenWrt MTD split support
   - Critical for device partitioning
   
2. ✅ **655-increase_skb_pad.patch**
   - Network performance tuning
   - Increases SKB padding for optimization

3. ✅ **680-NET-skip-GRO-for-foreign-MAC-addresses.patch**
   - Core network optimization
   - Prevents GRO issues with foreign MACs

## Patches Needing Verification (v6.3/v6.4 tags)

These 6 patches have version tags suggesting they may already be in 6.6:

1. `110-v6.3-0002-spidev-Add-Silicon-Labs-SI3210-device-compatible.patch`
2. `704-01-v6.4-net-mvneta-fix-transmit-path-dma-unmapping-on-error.patch`
3. `704-02-v6.4-net-mvneta-mark-mapped-and-tso-buffers-separately.patch`
4. `704-03-v6.4-net-mvneta-use-buf-type-to-determine-whether-to-dma-.patch`
5. `704-04-v6.4-net-mvneta-move-tso_build_hdr-into-mvneta_tso_put_hd.patch`
6. `704-05-v6.4-net-mvneta-allocate-TSO-header-DMA-memory-in-chunks.patch`

## Migration Priority

**High Priority** (core functionality):
- Networking patches (680, 655, 630, 666)
- MTD/Flash patches (400, 401, 430, 490, 491)
- Netfilter patches (700, 701)

**Medium Priority** (device drivers):
- PHY driver patches (703, 705)
- Architecture-specific patches (300-series, 310, 342)

**Lower Priority** (misc/debug):
- Filesystem patches (140, 530, 532)
- Debug/build patches (203, 920)

## Next Steps

1. Verify the 6 patches with v6.3/v6.4 tags
2. Rebase remaining 126 patches against kernel 6.6 source
3. Test each patch for conflicts
4. Update patches that need API adjustments
5. Build test with patches applied incrementally

## References

- Migration roadmap: `../../migration-outputs/MIGRATION_COMPLETE.md`
- Complete disposition table: `../../migration-outputs/migration_summary.md`
- Prioritized review list: `../../migration-outputs/manual_review_list.md`
