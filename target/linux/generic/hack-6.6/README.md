# hack-6.6

Patches migrated from hack-5.15 for kernel 6.6

**Status**: 🔄 Sample Patches Created - Full Migration Pending

## Current State

Out of **56 hack patches** from kernel 5.15:
- **4 sample patches** have been migrated as examples ✅
- **52 patches** need evaluation and migration ⏳

## What Are "Hack" Patches?

Hack patches implement OpenWrt-specific features and optimizations that are not suitable for upstream Linux. These include:
- Build system modifications
- Kernel debloating
- Hardware-specific workarounds
- Non-standard network features

## Sample Patches in This Directory

The following patches demonstrate successful migration:

1. ✅ **220-arm-gc_sections.patch**
   - ARM linker optimization
   - Reduces kernel size via garbage collection

2. ✅ **221-module_exports.patch**
   - Module export handling
   - Required for OpenWrt module system

3. ✅ **650-netfilter-add-xt_FLOWOFFLOAD-target.patch**
   - Netfilter flow offload target
   - Critical for hardware NAT acceleration

4. ✅ **700-swconfig_switch_drivers.patch**
   - Switch configuration support
   - Required for managed switch functionality

## Migration Priority

**Critical** (build system & core features):
- 221-module_exports.patch ✅
- 220-arm-gc_sections.patch ✅
- 230-openwrt_lzma_options.patch
- 251-kconfig.patch

**Critical** (networking):
- 650-netfilter-add-xt_FLOWOFFLOAD-target.patch ✅
- 700-swconfig_switch_drivers.patch ✅
- 645-netfilter-connmark-introduce-set-dscpmark.patch
- 660-fq_codel_defaults.patch
- 661-kernel-ct-size-the-hashtable-more-adequately.patch

**High Priority** (device support):
- 720-net-phy-add-aqr-phys.patch
- 721-net-add-packet-mangeling.patch
- 800-GPIO-add-named-gpio-exports.patch
- 810-bcma-ssb-fallback-sprom.patch

**Medium Priority** (MTD & storage):
- 420-mtd-support-OpenWrt-s-MTD_ROOTFS_ROOT_DEV.patch
- 430-mtk-bmt-support.patch
- 402-mtd-blktrans-call-add-disks-after-mtd-device.patch
- 410-block-fit-partition-parser.patch

**Lower Priority** (debloat & misc):
- 901-debloat_sock_diag.patch
- 902-debloat_proc.patch
- 904-debloat_dma_buf.patch
- 910-kobject_uevent.patch
- 920-device_tree_cmdline.patch

## Evaluation Steps for Each Patch

1. **Check if still needed**: Has upstream solved the problem differently?
2. **Check API changes**: Do function signatures still match?
3. **Test functionality**: Does the hack still achieve its purpose?
4. **Update if needed**: Adjust for kernel 6.6 changes

## Next Steps

1. Evaluate remaining 52 patches for relevance in 6.6
2. Update patches for 6.6 API changes
3. Test critical patches first (build system, netfilter)
4. Verify hardware-specific features still work
5. Document any patches that can be dropped

## References

- Migration roadmap: `../../migration-outputs/MIGRATION_COMPLETE.md`
- Complete disposition table: `../../migration-outputs/migration_summary.md`
- Prioritized review list: `../../migration-outputs/manual_review_list.md`
