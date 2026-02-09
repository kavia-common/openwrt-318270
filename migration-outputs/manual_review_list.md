# Patches Requiring Manual Review

Total items: 191

## BACKPORT Patches to Verify (3)

The following backport patches need manual verification to confirm they were truly merged upstream:

1. `751-00a-STABLE-net-ethernet-mediatek-split-tx-and-rx-fields-in-mtk_.patch` - No version tag - verify if merged in 5.16-6.6
2. `751-00b-net-ethernet-mediatek-use-QDMA-instead-of-ADMAv2-on-.patch` - No version tag - verify if merged in 5.16-6.6
3. `798-net-next-net-sfp-add-quirk-for-Fiberstone-GPON-ONU-34-20BI.patch` - No version tag - verify if merged in 5.16-6.6

## PENDING Patches to Rebase (132)

All pending-5.15 patches need to be rebased against kernel 6.6. Sample patches have been created in `target/linux/generic/pending-6.6/` as examples:

### High Priority - Core Networking
1. `680-NET-skip-GRO-for-foreign-MAC-addresses.patch` - **MIGRATED** - Core network optimization
2. `655-increase_skb_pad.patch` - **MIGRATED** - Network performance tuning
3. `630-packet_socket_type.patch` - Core packet handling
4. `666-Add-support-for-MAP-E-FMRs-mesh-mode.patch` - IPv6 transition mechanism

### High Priority - MTD Subsystem
5. `400-mtd-mtdsplit-support.patch` - **MIGRATED** - OpenWrt MTD split support
6. `401-mtd-don-t-register-NVMEM-devices-for-partitions-with.patch` - MTD NVMEM integration
7. `430-mtd-add-myloader-partition-parser.patch` - Device-specific parser
8. `490-ubi-auto-attach-mtd-device-named-ubi-or-data-on-boot.patch` - UBI auto-attach
9. `491-ubi-auto-create-ubiblock-device-for-rootfs.patch` - UBI rootfs support

### Medium Priority - Device Drivers
10. `700-netfilter-nft_flow_offload-handle-netdevice-events-f.patch` - Netfilter flow offload
11. `703-phy-add-detach-callback-to-struct-phy_driver.patch` - PHY driver enhancements
12. `705-net-dsa-tag_mtk-add-padding-for-tx-packets.patch` - MediaTek DSA support

### Medium Priority - Architecture-Specific
13. `300-mips_expose_boot_raw.patch` - MIPS boot support
14. `301-MIPS-Add-barriers-between-dcache-icache-flushes.patch` - MIPS cache handling
15. `310-arm_module_unresolved_weak_sym.patch` - ARM module loading
16. `342-powerpc-Enable-kernel-XZ-compression-option-on-PPC_8.patch` - PowerPC compression

### Lower Priority - Filesystems & Misc
17. `140-jffs2-use-.rename2-and-add-RENAME_WHITEOUT-support.patch` - JFFS2 enhancements
18. `530-jffs2_make_lzma_available.patch` - JFFS2 LZMA compression
19. `203-kallsyms_uncompressed.patch` - Debug symbols
20. `920-mangle_bootargs.patch` - Boot argument handling

### Remaining 112 patches listed in migration summary table

## HACK Patches to Port (56)

All hack-5.15 patches need verification and porting to 6.6. Sample patches have been created in `target/linux/generic/hack-6.6/` as examples:

### Critical - Build System
1. `221-module_exports.patch` - **MIGRATED** - Module export handling
2. `220-arm-gc_sections.patch` - **MIGRATED** - ARM size optimization
3. `230-openwrt_lzma_options.patch` - LZMA compression options
4. `251-kconfig.patch` - Kconfig modifications

### Critical - Netfilter
5. `650-netfilter-add-xt_FLOWOFFLOAD-target.patch` - **MIGRATED** - Flow offload target
6. `645-netfilter-connmark-introduce-set-dscpmark.patch` - Connmark DSCP
7. `660-fq_codel_defaults.patch` - Queue discipline tuning
8. `661-kernel-ct-size-the-hashtable-more-adequately.patch` - Conntrack sizing

### High Priority - Network Drivers
9. `700-swconfig_switch_drivers.patch` - **MIGRATED** - Swconfig support
10. `720-net-phy-add-aqr-phys.patch` - Aquantia PHY support
11. `721-net-add-packet-mangeling.patch` - Packet manipulation
12. `773-bgmac-add-srab-switch.patch` - Broadcom SRAB

### Medium Priority - Device Support
13. `800-GPIO-add-named-gpio-exports.patch` - GPIO exports
14. `810-bcma-ssb-fallback-sprom.patch` - BCMA/SSB SPROM
15. `420-mtd-support-OpenWrt-s-MTD_ROOTFS_ROOT_DEV.patch` - MTD rootfs
16. `430-mtk-bmt-support.patch` - MediaTek BMT

### Lower Priority - Misc
17. `901-debloat_sock_diag.patch` - Socket diagnostics debloat
18. `902-debloat_proc.patch` - /proc debloat
19. `910-kobject_uevent.patch` - Kobject uevent handling
20. `920-device_tree_cmdline.patch` - DT command line

### Remaining 36 patches listed in migration summary table

## Verification Steps

For each patch category:

1. **Backport patches marked DROP**: Verify the upstream commit actually includes the functionality
2. **Pending patches**: Test rebase against 6.6, resolve conflicts, verify functionality
3. **Hack patches**: Evaluate if still needed in 6.6, update for API changes
4. **All migrated patches**: Build test with 6.6 kernel, run smoke tests

## Migration Progress

- **Directories created**: ✓ backport-6.6, pending-6.6, hack-6.6
- **Analysis complete**: ✓ 869 patches analyzed
- **Sample patches created**: ✓ 6 representative examples
- **Summary documentation**: ✓ Generated
- **Next steps**: Manual review and complete migration of remaining patches
