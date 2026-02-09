# Kernel Patch Migration Summary: 5.15 -> 6.6

Generated: Mon Feb  9 09:38:02 PM UTC 2026

## Summary Statistics

- **Total patches analyzed**: 869
- **DROP (merged upstream)**: 678
- **MIGRATE (port to 6.6)**: 185
- **CHECK (needs verification)**: 6
- **Manual review items**: 191

## Backport Patches (backport-5.15 -> backport-6.6)

Total: 681 patches

| # | Filename | Disposition | Upstream Ver | Reason |
|---|----------|-------------|--------------|--------|
| 1 | `005-v5.17-01-Kbuild-use-Wdeclaration-after-statement.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 2 | `005-v5.17-02-Kbuild-move-to-std-gnu11.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 3 | `005-v5.17-03-Kbuild-use-std-gnu11-for-KBUILD_USERCFLAGS.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 4 | `020-v6.1-01-mm-x86-arm64-add-arch_has_hw_pte_young.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 5 | `020-v6.1-02-mm-x86-add-CONFIG_ARCH_HAS_NONLEAF_PMD_YOUNG.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 6 | `020-v6.1-03-mm-vmscan.c-refactor-shrink_node.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 7 | `020-v6.1-04-Revert-include-linux-mm_inline.h-fold-__update_lru_s.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 8 | `020-v6.1-05-mm-multi-gen-LRU-groundwork.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 9 | `020-v6.1-06-mm-multi-gen-LRU-minimal-implementation.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 10 | `020-v6.1-07-mm-multi-gen-LRU-exploit-locality-in-rmap.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 11 | `020-v6.1-08-mm-multi-gen-LRU-support-page-table-walks.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 12 | `020-v6.1-09-mm-multi-gen-LRU-optimize-multiple-memcgs.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 13 | `020-v6.1-10-mm-multi-gen-LRU-kill-switch.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 14 | `020-v6.1-11-mm-multi-gen-LRU-thrashing-prevention.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 15 | `020-v6.1-12-mm-multi-gen-LRU-debugfs-interface.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 16 | `020-v6.1-13-mm-mglru-don-t-sync-disk-for-each-aging-cycle.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 17 | `020-v6.1-14-mm-multi-gen-LRU-retry-pages-written-back-while-isol.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 18 | `020-v6.1-15-mm-multi-gen-LRU-move-lru_gen_add_mm-out-of-IRQ-off-.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 19 | `020-v6.1-17-mm-add-dummy-pmd_young-for-architectures-not-having-.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 20 | `020-v6.1-18-mm-introduce-arch_has_hw_nonleaf_pmd_young.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 21 | `020-v6.2-16-mm-multi-gen-LRU-fix-crash-during-cgroup-migration.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 22 | `020-v6.3-19-mm-add-vma_has_recency.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 23 | `020-v6.3-20-mm-support-POSIX_FADV_NOREUSE.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 24 | `020-v6.3-21-mm-multi-gen-LRU-rename-lru_gen_struct-to-lru_gen_pa.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 25 | `020-v6.3-22-mm-multi-gen-LRU-rename-lrugen-lists-to-lrugen-pages.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 26 | `020-v6.3-23-mm-multi-gen-LRU-remove-eviction-fairness-safeguard.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 27 | `020-v6.3-24-mm-multi-gen-LRU-remove-aging-fairness-safeguard.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 28 | `020-v6.3-25-mm-multi-gen-LRU-shuffle-should_run_aging.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 29 | `020-v6.3-26-mm-multi-gen-LRU-per-node-lru_gen_page-lists.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 30 | `020-v6.3-27-mm-multi-gen-LRU-clarify-scan_control-flags.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 31 | `020-v6.3-28-mm-multi-gen-LRU-simplify-arch_has_hw_pte_young-chec.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 32 | `020-v6.3-29-mm-multi-gen-LRU-avoid-futile-retries.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 33 | `050-v5.16-00-MIPS-uasm-Enable-muhu-opcode-for-MIPS-R6.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 34 | `050-v5.16-01-mips-uasm-Add-workaround-for-Loongson-2F-nop-CPU-err.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 35 | `050-v5.16-02-mips-bpf-Add-eBPF-JIT-for-32-bit-MIPS.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 36 | `050-v5.16-03-mips-bpf-Add-new-eBPF-JIT-for-64-bit-MIPS.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 37 | `050-v5.16-04-mips-bpf-Add-JIT-workarounds-for-CPU-errata.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 38 | `050-v5.16-05-mips-bpf-Enable-eBPF-JITs.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 39 | `050-v5.16-06-mips-bpf-Remove-old-BPF-JIT-implementations.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 40 | `060-v5.18-01-bpf-selftests-Add-helpers-to-directly-use-the-capget.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 41 | `060-v5.18-02-bpf-selftests-Remove-libcap-usage-from-test_verifier.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 42 | `060-v5.18-03-bpf-selftests-Remove-libcap-usage-from-test_progs.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 43 | `080-v5.17-clk-gate-Add-devm_clk_hw_register_gate.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 44 | `100-v5.18-tty-serial-bcm63xx-use-more-precise-Kconfig-symbol.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 45 | `200-v5.18-tools-resolve_btfids-Build-with-host-flags.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 46 | `201-v5.16-scripts-dtc-Update-to-upstream-version-v1.6.1-19-g0a.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 47 | `300-v5.18-pinctrl-qcom-Return--EINVAL-for-setting-affinity-if-no-IRQ-parent.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 48 | `301-v5.16-soc-qcom-smem-Support-reserved-memory-description.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 49 | `302-v5.16-watchdog-bcm63xx_wdt-fix-fallthrough-warning.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 50 | `330-v5.16-01-MIPS-kernel-proc-add-CPU-option-reporting.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 51 | `330-v5.16-02-MIPS-Fix-using-smp_processor_id-in-preemptible-in-sh.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 52 | `331-v5.19-mtd-spinand-Add-support-for-XTX-XT26G0xA.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 53 | `344-v5.18-01-phy-marvell-phy-mvebu-a3700-comphy-Remove-port-from-.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 54 | `344-v5.18-02-phy-marvell-phy-mvebu-a3700-comphy-Add-native-kernel.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 55 | `345-v5.17-arm64-dts-marvell-armada-37xx-Add-xtal-clock-to-comp.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 56 | `346-v5.18-01-Revert-ata-ahci-mvebu-Make-SATA-PHY-optional-for-Arm.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 57 | `346-v5.18-02-Revert-usb-host-xhci-mvebu-make-USB-3.0-PHY-optional.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 58 | `346-v5.18-03-Revert-PCI-aardvark-Fix-initialization-with-old-Marv.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 59 | `347-v6.0-phy-marvell-phy-mvebu-a3700-comphy-Remove-broken-res.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 60 | `350-v5.18-regmap-add-configurable-downshift-for-addresses.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 61 | `351-v5.18-regmap-allow-a-defined-reg_base-to-be-added-to-every.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 62 | `352-v6.3-regmap-apply-reg_base-and-reg_downshift-for-single-r.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 63 | `400-v5.19-mtd-call-of_platform_populate-for-MTD-partitions.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 64 | `401-v6.0-mtd-parsers-add-support-for-Sercomm-partitions.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 65 | `402-v6.0-mtd-next-mtd-core-introduce-of-support-for-dynamic-partitions.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 66 | `403-v6.1-mtd-allow-getting-MTD-device-associated-with-a-speci.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 67 | `404-v6.0-mtd-core-check-partition-before-dereference.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 68 | `405-v6.1-mtd-core-add-missing-of_node_get-in-dynamic-partitio.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 69 | `406-v6.2-0001-mtd-core-simplify-a-bit-code-find-partition-matching.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 70 | `406-v6.2-0002-mtd-core-try-to-find-OF-node-for-every-MTD-partition.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 71 | `407-v5.17-mtd-parsers-qcom-Don-t-print-error-message-on-EPROBE.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 72 | `408-v6.2-mtd-core-set-ROOT_DEV-for-partitions-marked-as-rootf.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 73 | `410-v5.18-mtd-parsers-trx-allow-to-use-on-MediaTek-MIPS-SoCs.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 74 | `420-v5.19-02-mtd-spinand-gigadevice-add-support-for-GD5FxGQ4xExxG.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 75 | `420-v5.19-03-mtd-spinand-gigadevice-add-support-for-GD5F1GQ5RExxG.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 76 | `420-v5.19-04-mtd-spinand-gigadevice-add-support-for-GD5F-2-4-GQ5x.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 77 | `420-v5.19-05-mtd-spinand-gigadevice-add-support-for-GD5FxGM7xExxG.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 78 | `421-v6.2-mtd-parsers-add-TP-Link-SafeLoader-partitions-table-.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 79 | `422-v5.19-mtd-spi-nor-support-eon-en25qh256a.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 80 | `423-v6.1-0001-mtd-track-maximum-number-of-bitflips-for-each-read-r.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 81 | `423-v6.1-0002-mtd-always-initialize-stats-in-struct-mtd_oob_ops.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 82 | `423-v6.1-0003-mtd-add-ECC-error-accounting-for-each-read-request.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 83 | `423-v6.1-0004-mtdchar-add-MEMREAD-ioctl.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 84 | `423-v6.3-mtd-spinand-macronix-use-scratch-buffer-for-DMA-oper.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 85 | `424-v6.4-0004-mtd-core-prepare-mtd_otp_nvmem_add-to-handle-EPROBE_.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 86 | `600-v5.18-page_pool-Add-allocation-stats.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 87 | `601-v5.18-page_pool-Add-recycle-stats.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 88 | `602-v5.18-page_pool-Add-function-to-batch-and-return-stats.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 89 | `603-v5.19-page_pool-Add-recycle-stats-to-page_pool_put_page_bu.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 90 | `604-v5.19-net-page_pool-introduce-ethtool-stats.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 91 | `605-v5.18-xdp-introduce-flags-field-in-xdp_buff-xdp_frame.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 92 | `606-v5.18-xdp-add-frags-support-to-xdp_return_-buff-frame.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 93 | `607-v5.18-net-skbuff-add-size-metadata-to-skb_shared_info-for-.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 94 | `608-v5.18-net-veth-Account-total-xdp_frame-len-running-ndo_xdp.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 95 | `609-v5.18-veth-Allow-jumbo-frames-in-xdp-mode.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 96 | `611-v6.3-net-add-helper-eth_addr_add.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 97 | `700-v5.17-net-dsa-introduce-tagger-owned-storage-for-private.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 98 | `701-v5.17-dsa-make-tagging-protocols-connect-to-individual-switches.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 99 | `702-v5.19-00-net-ethernet-mtk_eth_soc-add-support-for-coherent-DM.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 100 | `702-v5.19-02-net-ethernet-mtk_eth_soc-add-support-for-Wireless-Et.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 101 | `702-v5.19-03-net-ethernet-mtk_eth_soc-implement-flow-offloading-t.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 102 | `702-v5.19-05-net-ethernet-mtk_eth_soc-add-ipv6-flow-offload-suppo.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 103 | `702-v5.19-06-net-ethernet-mtk_eth_soc-support-TC_SETUP_BLOCK-for-.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 104 | `702-v5.19-07-net-ethernet-mtk_eth_soc-allocate-struct-mtk_ppe-sep.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 105 | `702-v5.19-08-net-ethernet-mtk_eth_soc-rework-hardware-flow-table-.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 106 | `702-v5.19-09-net-ethernet-mtk_eth_soc-remove-bridge-flow-offload-.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 107 | `702-v5.19-10-net-ethernet-mtk_eth_soc-support-creating-mac-addres.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 108 | `702-v5.19-11-net-ethernet-mtk_eth_soc-wed-fix-sparse-endian-warni.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 109 | `702-v5.19-12-net-ethernet-mtk_eth_soc-fix-return-value-check-in-m.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 110 | `702-v5.19-13-net-ethernet-mtk_eth_soc-use-standard-property-for-c.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 111 | `702-v5.19-14-net-ethernet-mtk_eth_soc-use-after-free-in-__mtk_ppe.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 112 | `702-v5.19-15-net-ethernet-mtk_eth_soc-add-check-for-allocation-fa.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 113 | `702-v5.19-16-eth-mtk_eth_soc-silence-the-GCC-12-array-bounds-warn.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 114 | `702-v5.19-17-net-ethernet-mtk_eth_soc-rely-on-GFP_KERNEL-for-dma_.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 115 | `702-v5.19-18-net-ethernet-mtk_eth_soc-move-tx-dma-desc-configurat.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 116 | `702-v5.19-19-net-ethernet-mtk_eth_soc-add-txd_size-to-mtk_soc_dat.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 117 | `702-v5.19-20-net-ethernet-mtk_eth_soc-rely-on-txd_size-in-mtk_tx_.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 118 | `702-v5.19-21-net-ethernet-mtk_eth_soc-rely-on-txd_size-in-mtk_des.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 119 | `702-v5.19-22-net-ethernet-mtk_eth_soc-rely-on-txd_size-in-txd_to_.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 120 | `702-v5.19-23-net-ethernet-mtk_eth_soc-add-rxd_size-to-mtk_soc_dat.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 121 | `702-v5.19-24-net-ethernet-mtk_eth_soc-rely-on-txd_size-field-in-m.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 122 | `702-v5.19-25-net-ethernet-mtk_eth_soc-rely-on-rxd_size-field-in-m.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 123 | `702-v5.19-26-net-ethernet-mtk_eth_soc-introduce-device-register-m.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 124 | `702-v5.19-27-net-ethernet-mtk_eth_soc-introduce-MTK_NETSYS_V2-sup.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 125 | `702-v5.19-28-net-ethernet-mtk_eth_soc-convert-ring-dma-pointer-to.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 126 | `702-v5.19-29-net-ethernet-mtk_eth_soc-convert-scratch_ring-pointe.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 127 | `702-v5.19-30-net-ethernet-mtk_eth_soc-introduce-support-for-mt798.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 128 | `702-v5.19-31-net-ethernet-mtk_eth_soc-fix-error-code-in-mtk_flow_.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 129 | `702-v5.19-33-net-ethernet-mtk_eth_soc-enable-rx-cksum-offload-for.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 130 | `702-v5.19-34-eth-mtk_ppe-fix-up-after-merge.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 131 | `703-00-v5.16-net-convert-users-of-bitmap_foo-to-linkmode_foo.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 132 | `703-01-v5.16-net-phylink-add-MAC-phy_interface_t-bitmap.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 133 | `703-02-v5.16-net-phylink-use-supported_interfaces-for-phylink-val.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 134 | `703-03-v5.16-net-dsa-populate-supported_interfaces-member.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 135 | `703-04-v5.17-net-dsa-consolidate-phylink-creation.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 136 | `703-05-v5.17-net-dsa-replace-phylink_get_interfaces-with-phylink_.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 137 | `703-06-v5.18-net-dsa-add-support-for-phylink-mac_select_pcs.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 138 | `703-07-v5.16-net-phy-add-phy_interface_t-bitmap-support.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 139 | `703-08-v5.17-net-phylink-add-mac_select_pcs-method-to-phylink_mac.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 140 | `703-09-v5.17-net-phylink-add-generic-validate-implementation.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 141 | `703-11-v5.17-net-phylink-add-pcs_validate-method.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 142 | `703-12-v5.17-net-phylink-add-legacy_pre_march2020-indicator.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 143 | `703-13-v5.17-net-dsa-mark-DSA-phylink-as-legacy_pre_march2020.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 144 | `703-14-v5.17-net-phylink-use-legacy_pre_march2020.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 145 | `703-15-v5.18-net-phy-phylink-fix-DSA-mac_select_pcs-introduction.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 146 | `703-16-v5.16-net-mvneta-populate-supported_interfaces-member.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 147 | `703-17-v5.16-net-mvneta-remove-interface-checks-in-mvneta_validat.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 148 | `703-18-v5.16-net-mvneta-drop-use-of-phylink_helper_basex_speed.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 149 | `703-19-v5.17-net-mvneta-use-phylink_generic_validate.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 150 | `703-20-v5.17-net-mvneta-mark-as-a-legacy_pre_march2020-driver.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 151 | `704-01-v5.17-net-mtk_eth_soc-populate-supported_interfaces-member.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 152 | `704-02-v5.17-net-mtk_eth_soc-remove-interface-checks-in-mtk_valid.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 153 | `704-03-v5.17-net-mtk_eth_soc-drop-use-of-phylink_helper_basex_spe.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 154 | `704-04-v5.17-net-mtk_eth_soc-use-phylink_generic_validate.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 155 | `704-05-v5.17-net-mtk_eth_soc-mark-as-a-legacy_pre_march2020-drive.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 156 | `704-06-v5.19-eth-mtk_eth_soc-remove-a-copy-of-the-NAPI_POLL_WEIGH.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 157 | `704-07-v5.19-mtk_eth_soc-remove-unused-mac-mode.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 158 | `704-08-v5.19-net-mtk_eth_soc-remove-unused-sgmii-flags.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 159 | `704-09-v5.19-net-mtk_eth_soc-add-mask-and-update-PCS-speed-defini.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 160 | `704-10-v5.19-net-mtk_eth_soc-correct-802.3z-speed-setting.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 161 | `704-11-v5.19-net-mtk_eth_soc-correct-802.3z-duplex-setting.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 162 | `704-12-v5.19-net-mtk_eth_soc-stop-passing-phylink-state-to-sgmii-.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 163 | `704-13-v5.19-net-mtk_eth_soc-provide-mtk_sgmii_config.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 164 | `704-14-v5.19-net-mtk_eth_soc-add-fixme-comment-for-state-speed-us.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 165 | `704-16-v5.19-net-mtk_eth_soc-move-restoration-of-SYSCFG0-to-mac_f.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 166 | `704-17-v5.19-net-mtk_eth_soc-convert-code-structure-to-suit-split.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 167 | `704-18-v5.19-net-mtk_eth_soc-partially-convert-to-phylink_pcs.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 168 | `705-01-v5.17-net-dsa-mt7530-iterate-using-dsa_switch_for_each_use.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 169 | `705-02-v5.19-net-dsa-mt7530-populate-supported_interfaces-and-mac.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 170 | `705-03-v5.19-net-dsa-mt7530-remove-interface-checks.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 171 | `705-04-v5.19-net-dsa-mt7530-drop-use-of-phylink_helper_basex_spee.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 172 | `705-05-v5.19-net-dsa-mt7530-only-indicate-linkmodes-that-can-be-s.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 173 | `705-06-v5.19-net-dsa-mt7530-switch-to-use-phylink_get_linkmodes.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 174 | `705-07-v5.19-net-dsa-mt7530-partially-convert-to-phylink_pcs.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 175 | `705-08-v5.19-net-dsa-mt7530-move-autoneg-handling-to-PCS-validati.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 176 | `705-09-v5.19-net-dsa-mt7530-mark-as-non-legacy.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 177 | `705-10-v5.19-net-dsa-mt753x-fix-pcs-conversion-regression.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 178 | `705-11-v6.0-net-dsa-mt7530-rework-mt7530_hw_vlan_-add-del.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 179 | `705-13-v6.0-net-dsa-mt7530-get-cpu-port-via-dp-cpu_dp-instead-of.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 180 | `706-00-v6.0-net-ethernet-mtk_eth_soc-rely-on-page_pool-for-singl.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 181 | `706-01-v6.0-net-ethernet-mtk_eth_soc-add-basic-XDP-support.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 182 | `706-02-v6.0-net-ethernet-mtk_eth_soc-introduce-xdp-ethtool-count.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 183 | `706-03-v6.0-net-ethernet-mtk_eth_soc-add-xmit-XDP-support.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 184 | `706-04-v6.0-net-ethernet-mtk_eth_soc-add-support-for-page_pool_g.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 185 | `706-05-v6.0-net-ethernet-mtk_eth_soc-introduce-mtk_xdp_frame_map.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 186 | `706-06-v6.0-net-ethernet-mtk_eth_soc-introduce-xdp-multi-frag-su.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 187 | `707-v6.3-net-pcs-add-driver-for-MediaTek-SGMII-PCS.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 188 | `708-01-v5.16-net-mvneta-Delete-unused-variable.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 189 | `708-02-v6.3-net-mvneta-fix-potential-double-frees-in-mvneta_txq_.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 190 | `710-v6.0-net-ethernet-mtk_eth_soc-fix-hw-hash-reporting-for-M.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 191 | `711-v6.0-01-net-ethernet-mtk_eth_soc-fix-off-by-one-check-of-ARR.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 192 | `711-v6.0-02-net-ethernet-mtk_ppe-fix-possible-NULL-pointer-deref.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 193 | `711-v6.0-03-net-ethernet-mtk-ppe-fix-traffic-offload-with-bridge.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 194 | `711-v6.0-04-net-ethernet-mtk_eth_soc-remove-mtk_foe_entry_timest.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 195 | `712-v6.0-net-ethernet-mtk_eth_soc-enable-XDP-support-just-for.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 196 | `713-v6.0-net-ethernet-mtk_eth_soc-move-gdma_to_ppe-and-ppe_ba.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 197 | `714-v6.0-net-ethernet-mtk_eth_soc-move-ppe-table-hash-offset-.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 198 | `715-v6.0-net-ethernet-mtk_eth_soc-add-the-capability-to-run-m.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 199 | `716-v6.0-net-ethernet-mtk_eth_soc-move-wdma_base-definitions-.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 200 | `717-v6.0-net-ethernet-mtk_eth_soc-add-foe_entry_size-to-mtk_e.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 201 | `718-v6.0-net-ethernet-mtk_eth_soc-fix-typo-in-__mtk_foe_entry.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 202 | `719-v6.0-net-ethernet-mtk_eth_soc-check-max-allowed-value-in-.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 203 | `720-v6.0-net-ethernet-mtk_eth_wed-add-mtk_wed_configure_irq-a.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 204 | `721-v6.0-net-ethernet-mtk_eth_wed-add-wed-support-for-mt7986-.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 205 | `722-v6.0-net-ethernet-mtk_eth_wed-add-axi-bus-support.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 206 | `723-v6.0-net-ethernet-mtk_eth_soc-introduce-flow-offloading-s.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 207 | `724-v6.0-net-ethernet-mtk_eth_soc-enable-flow-offloading-supp.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 208 | `724-v6.0-net-ethernet-mtk_eth_soc-fix-wrong-use-of-new-helper.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 209 | `725-v6.0-net-ethernet-mtk_eth_soc-fix-usage-of-foe_entry_size.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 210 | `726-v6.0-net-ethernet-mtk_eth_soc-fix-mask-of-RX_DMA_GET_SPOR.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 211 | `727-v6.1-net-ethernet-mtk_eth_soc-fix-state-in-__mtk_foe_entr.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 212 | `728-v6.1-01-net-ethernet-mtk_eth_soc-fix-possible-memory-leak-in.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 213 | `728-v6.1-02-net-ethernet-mtk_eth_wed-add-missing-put_device-in-m.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 214 | `728-v6.1-03-net-ethernet-mtk_eth_wed-add-missing-of_node_put.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 215 | `728-v6.1-04-net-ethernet-mtk_eth_soc-fix-resource-leak-in-error-.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 216 | `728-v6.1-05-net-ethernet-mtk_eth_soc-fix-memory-leak-in-error-pa.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 217 | `729-01-v6.1-net-ethernet-mtk_wed-introduce-wed-mcu-support.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 218 | `729-02-v6.1-net-ethernet-mtk_wed-introduce-wed-wo-support.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 219 | `729-03-v6.1-net-ethernet-mtk_wed-rename-tx_wdma-array-in-rx_wdma.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 220 | `729-04-v6.1-net-ethernet-mtk_wed-add-configure-wed-wo-support.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 221 | `729-05-v6.1-net-ethernet-mtk_wed-add-rx-mib-counters.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 222 | `729-06-v6.1-net-ethernet-mtk_eth_soc-do-not-overwrite-mtu-config.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 223 | `729-07-v6.1-net-ethernet-mtk_eth_soc-remove-cpu_relax-in-mtk_pen.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 224 | `729-08-v6.2-net-ethernet-mtk_eth_soc-fix-RSTCTRL_PPE-0-1-definit.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 225 | `729-09-v6.2-net-ethernet-mtk_wed-add-wcid-overwritten-support-fo.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 226 | `729-10-v6.2-net-ethernet-mtk_wed-return-status-value-in-mtk_wdma.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 227 | `729-11-v6.2-net-ethernet-mtk_wed-move-MTK_WDMA_RESET_IDX_TX-conf.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 228 | `729-12-v6.2-net-ethernet-mtk_wed-update-mtk_wed_stop.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 229 | `729-13-v6.2-net-ethernet-mtk_wed-add-mtk_wed_rx_reset-routine.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 230 | `729-14-v6.2-net-ethernet-mtk_wed-add-reset-to-tx_ring_setup-call.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 231 | `729-15-v6.2-net-ethernet-mtk_wed-fix-sleep-while-atomic-in-mtk_w.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 232 | `729-16-v6.3-net-ethernet-mtk_wed-get-rid-of-queue-lock-for-rx-qu.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 233 | `729-17-v6.3-net-ethernet-mtk_wed-get-rid-of-queue-lock-for-tx-qu.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 234 | `729-18-v6.3-net-ethernet-mtk_eth_soc-introduce-mtk_hw_reset-util.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 235 | `729-19-v6.3-net-ethernet-mtk_eth_soc-introduce-mtk_hw_warm_reset.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 236 | `729-20-v6.3-net-ethernet-mtk_eth_soc-align-reset-procedure-to-ve.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 237 | `729-21-v6.3-net-ethernet-mtk_eth_soc-add-dma-checks-to-mtk_hw_re.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 238 | `729-22-v6.3-net-ethernet-mtk_wed-add-reset-reset_complete-callba.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 239 | `729-23-v6.3-net-ethernet-mtk_wed-add-reset-to-rx_ring_setup-call.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 240 | `730-01-v6.3-net-ethernet-mtk_eth_soc-account-for-vlan-in-rx-head.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 241 | `730-02-v6.3-net-ethernet-mtk_eth_soc-increase-tx-ring-side-for-Q.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 242 | `730-03-v6.3-net-ethernet-mtk_eth_soc-avoid-port_mg-assignment-on.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 243 | `730-04-v6.3-net-ethernet-mtk_eth_soc-implement-multi-queue-suppo.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 244 | `730-05-v6.3-net-dsa-tag_mtk-assign-per-port-queues.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 245 | `730-06-v6.3-net-ethernet-mediatek-ppe-assign-per-port-queues-for.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 246 | `730-08-v6.3-net-dsa-add-support-for-DSA-rx-offloading-via-metada.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 247 | `730-09-v6.3-net-ethernet-mtk_eth_soc-fix-VLAN-rx-hardware-accele.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 248 | `730-10-v6.3-net-ethernet-mtk_eth_soc-drop-packets-to-WDMA-if-the.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 249 | `730-12-v6.3-net-ethernet-mtk_eth_soc-disable-hardware-DSA-untagg.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 250 | `730-13-v6.3-net-ethernet-mtk_eth_soc-enable-special-tag-when-any.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 251 | `730-14-v6.3-net-ethernet-mtk_eth_soc-fix-DSA-TX-tag-hwaccel-for-.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 252 | `730-15-v6.3-net-ethernet-mtk_wed-No-need-to-clear-memory-after-a.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 253 | `730-16-v6.3-net-ethernet-mtk_wed-fix-some-possible-NULL-pointer-.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 254 | `730-17-v6.3-net-ethernet-mtk_wed-fix-possible-deadlock-if-mtk_we.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 255 | `730-18-v6.3-net-ethernet-mtk_eth_soc-fix-tx-throughput-regressio.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 256 | `731-v6.1-0001-net-phy-Introduce-QUSGMII-PHY-mode.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 257 | `731-v6.1-0002-net-phy-Add-helper-to-derive-the-number-of-ports-fro.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 258 | `731-v6.1-0003-net-phy-Add-1000BASE-KX-interface-mode.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 259 | `731-v6.1-0004-net-phy-Add-support-for-rate-matching.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 260 | `733-v6.2-01-net-ethernet-mtk_eth_soc-Avoid-truncating-allocation.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 261 | `733-v6.2-02-net-mtk_eth_soc-add-definitions-for-PCS.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 262 | `733-v6.2-03-net-mtk_eth_soc-eliminate-unnecessary-error-handling.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 263 | `733-v6.2-04-net-mtk_eth_soc-add-pcs_get_state-implementation.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 264 | `733-v6.2-05-net-mtk_eth_soc-convert-mtk_sgmii-to-use-regmap_upda.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 265 | `733-v6.2-06-net-mtk_eth_soc-add-out-of-band-forcing-of-speed-and.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 266 | `733-v6.2-07-net-mtk_eth_soc-move-PHY-power-up.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 267 | `733-v6.2-08-net-mtk_eth_soc-move-interface-speed-selection.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 268 | `733-v6.2-09-net-mtk_eth_soc-add-advertisement-programming.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 269 | `733-v6.2-10-net-mtk_eth_soc-move-and-correct-link-timer-programm.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 270 | `733-v6.2-11-net-mtk_eth_soc-add-support-for-in-band-802.3z-negot.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 271 | `733-v6.2-12-net-mediatek-sgmii-ensure-the-SGMII-PHY-is-powered-d.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 272 | `733-v6.2-13-net-mediatek-sgmii-fix-duplex-configuration.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 273 | `733-v6.2-14-mtk_sgmii-enable-PCS-polling-to-allow-SFP-work.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 274 | `733-v6.3-15-net-ethernet-mtk_eth_soc-reset-PCS-state.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 275 | `733-v6.3-16-net-ethernet-mtk_eth_soc-only-write-values-if-needed.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 276 | `733-v6.3-18-net-ethernet-mtk_eth_soc-add-support-for-MT7981.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 277 | `733-v6.3-19-net-ethernet-mtk_eth_soc-set-MDIO-bus-clock-frequenc.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 278 | `733-v6.3-20-net-ethernet-mtk_eth_soc-switch-to-external-PCS-driv.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 279 | `733-v6.3-21-net-ethernet-mtk_eth_soc-add-missing-ppe-cache-flush.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 280 | `733-v6.4-22-net-mtk_eth_soc-use-WO-firmware-for-MT7981.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 281 | `733-v6.4-23-net-ethernet-mtk_eth_soc-fix-NULL-pointer-dereferenc.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 282 | `733-v6.4-24-net-ethernet-mtk_eth_soc-ppe-add-support-for-flow-ac.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 283 | `733-v6.4-25-net-ethernet-mediatek-fix-ppe-flow-accounting-for-v1.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 284 | `733-v6.4-26-net-ethernet-mtk_eth_soc-drop-generic-vlan-rx-offloa.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 285 | `733-v6.5-27-net-ethernet-mtk_eth_soc-always-mtk_get_ib1_pkt_type.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 286 | `734-v5.16-0001-net-bgmac-improve-handling-PHY.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 287 | `734-v5.16-0002-net-bgmac-support-MDIO-described-in-DT.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 288 | `734-v6.8-net-phy-bcm54612e-add-suspend-resume.patch` | **DROP** | 6.8 | Included in kernel 6.6+ (v6.8) |
| 289 | `735-v6.0-0001-net-phy-Add-support-for-AQR113C-EPHY.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 290 | `736-v6.1-0001-net-phy-aquantia-Add-some-additional-phy-interfaces.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 291 | `736-v6.1-0002-net-phy-aquantia-Add-support-for-rate-matching.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 292 | `737-01-v6.7-net-phy-aquantia-move-to-separate-directory.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 293 | `737-02-v6.7-net-phy-aquantia-move-MMD_VEND-define-to-header.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 294 | `737-03-v6.7-net-phy-aquantia-add-firmware-load-support.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 295 | `742-v5.16-net-phy-at803x-add-support-for-qca-8327-internal-phy.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 296 | `743-v5.16-0001-net-dsa-b53-Include-all-ports-in-enabled_ports.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 297 | `743-v5.16-0002-net-dsa-b53-Drop-BCM5301x-workaround-for-a-wrong-CPU.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 298 | `743-v5.16-0003-net-dsa-b53-Improve-flow-control-setup-on-BCM5301x.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 299 | `743-v5.16-0004-net-dsa-b53-Drop-unused-cpu_port-field.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 300 | `745-v5.16-01-net-phy-at803x-add-support-for-qca-8327-A-variant.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 301 | `745-v5.16-02-net-phy-at803x-add-resume-suspend-function-to-qca83x.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 302 | `745-v5.16-03-net-phy-at803x-fix-spacing-and-improve-name-for-83xx.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 303 | `746-v5.16-01-net-phy-at803x-fix-resume-for-QCA8327-phy.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 304 | `746-v5.16-02-net-phy-at803x-add-DAC-amplitude-fix-for-8327-phy.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 305 | `746-v5.16-03-net-phy-at803x-enable-prefer-master-for-83xx-interna.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 306 | `746-v5.16-04-net-phy-at803x-better-describe-debug-regs.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 307 | `747-v5.16-01-dsa-qca8k-add-mac-power-sel-support.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 308 | `747-v5.16-02-dt-bindings-net-dsa-qca8k-Add-SGMII-clock-phase-prop.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 309 | `747-v5.16-03-net-dsa-qca8k-add-support-for-sgmii-falling-edge.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 310 | `747-v5.16-04-dt-bindings-net-dsa-qca8k-Document-support-for-CPU-p.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 311 | `747-v5.16-05-net-dsa-qca8k-add-support-for-cpu-port-6.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 312 | `747-v5.16-06-net-dsa-qca8k-rework-rgmii-delay-logic-and-scan-for-.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 313 | `747-v5.16-07-dt-bindings-net-dsa-qca8k-Document-qca-sgmii-enable-.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 314 | `747-v5.16-08-net-dsa-qca8k-add-explicit-SGMII-PLL-enable.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 315 | `747-v5.16-09-dt-bindings-net-dsa-qca8k-Document-qca-led-open-drai.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 316 | `747-v5.16-10-net-dsa-qca8k-add-support-for-pws-config-reg.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 317 | `747-v5.16-11-dt-bindings-net-dsa-qca8k-document-support-for-qca83.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 318 | `747-v5.16-12-net-dsa-qca8k-add-support-for-QCA8328.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 319 | `747-v5.16-13-net-dsa-qca8k-set-internal-delay-also-for-sgmii.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 320 | `747-v5.16-14-net-dsa-qca8k-move-port-config-to-dedicated-struct.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 321 | `747-v5.16-15-dt-bindings-net-ipq8064-mdio-fix-warning-with-new-qc.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 322 | `747-v5.16-16-dt-bindings-net-dsa-qca8k-convert-to-YAML-schema.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 323 | `748-v5.16-net-dsa-qca8k-fix-delay-applied-to-wrong-cpu-in-parse-p.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 324 | `749-v5.16-net-dsa-qca8k-tidy-for-loop-in-setup-and-add-cpu-port-c.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 325 | `750-v5.16-net-dsa-qca8k-make-sure-pad0-mac06-exchange-is-disabled.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 326 | `750-v6.5-01-net-ethernet-mtk_ppe-add-MTK_FOE_ENTRY_V-1-2-_SIZE-m.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 327 | `750-v6.5-02-net-ethernet-mtk_eth_soc-remove-incorrect-PLL-config.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 328 | `750-v6.5-03-net-ethernet-mtk_eth_soc-remove-mac_pcs_get_state-an.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 329 | `750-v6.5-05-net-ethernet-mtk_eth_soc-add-version-in-mtk_soc_data.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 330 | `750-v6.5-06-net-ethernet-mtk_eth_soc-increase-MAX_DEVS-to-3.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 331 | `750-v6.5-07-net-ethernet-mtk_eth_soc-rely-on-MTK_MAX_DEVS-and-re.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 332 | `750-v6.5-08-net-ethernet-mtk_eth_soc-add-NETSYS_V3-version-suppo.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 333 | `750-v6.5-09-net-ethernet-mtk_eth_soc-convert-caps-in-mtk_soc_dat.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 334 | `750-v6.5-10-net-ethernet-mtk_eth_soc-convert-clock-bitmap-to-u64.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 335 | `750-v6.5-11-net-ethernet-mtk_eth_soc-add-basic-support-for-MT798.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 336 | `750-v6.5-12-net-ethernet-mtk_eth_soc-enable-page_pool-support-fo.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 337 | `750-v6.5-13-net-ethernet-mtk_eth_soc-enable-nft-hw-flowtable_off.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 338 | `750-v6.5-14-net-ethernet-mtk_eth_soc-support-per-flow-accounting.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 339 | `750-v6.5-15-net-ethernet-mtk_eth_soc-fix-NULL-pointer-on-hw-rese.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 340 | `750-v6.5-16-net-ethernet-mtk_eth_soc-fix-register-definitions-fo.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 341 | `750-v6.5-17-net-ethernet-mtk_eth_soc-add-reset-bits-for-MT7988.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 342 | `750-v6.5-18-net-ethernet-mtk_eth_soc-add-support-for-in-SoC-SRAM.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 343 | `750-v6.5-19-net-ethernet-mtk_eth_soc-support-36-bit-DMA-addressi.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 344 | `751-00a-STABLE-net-ethernet-mediatek-split-tx-and-rx-fields-in-mtk_.patch` | **MIGRATE** | None | Unknown - needs verification |
| 345 | `751-00b-net-ethernet-mediatek-use-QDMA-instead-of-ADMAv2-on-.patch` | **MIGRATE** | None | Unknown - needs verification |
| 346 | `751-01-v6.4-net-ethernet-mtk_eth_soc-add-code-for-offloading-flo.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 347 | `751-02-v6.4-net-ethernet-mediatek-mtk_ppe-prefer-newly-added-l2-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 348 | `751-03-v6.4-net-ethernet-mtk_eth_soc-improve-keeping-track-of-of.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 349 | `751-04-v6.4-net-ethernet-mediatek-fix-ppe-flow-accounting-for-L2.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 350 | `752-01-v6.6-net-ethernet-mtk_wed-add-some-more-info-in-wed_txinf.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 351 | `752-02-v6.6-net-ethernet-mtk_wed-minor-change-in-wed_-tx-rx-info.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 352 | `752-03-v6.6-net-ethernet-mtk_eth_soc-rely-on-mtk_pse_port-defini.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 353 | `752-04-v6.6-net-ethernet-mtk_wed-check-update_wo_rx_stats-in-mtk.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 354 | `752-05-v6.7-net-ethernet-mtk_wed-do-not-assume-offload-callbacks.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 355 | `752-06-v6.7-net-ethernet-mtk_wed-introduce-versioning-utility-ro.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 356 | `752-07-v6.7-net-ethernet-mtk_wed-do-not-configure-rx-offload-if-.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 357 | `752-08-v6.7-net-ethernet-mtk_wed-rename-mtk_rxbm_desc-in-mtk_wed.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 358 | `752-09-v6.7-net-ethernet-mtk_wed-introduce-mtk_wed_buf-structure.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 359 | `752-10-v6.7-net-ethernet-mtk_wed-move-mem_region-array-out-of-mt.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 360 | `752-11-v6.7-net-ethernet-mtk_wed-make-memory-region-optional.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 361 | `752-12-v6.7-net-ethernet-mtk_wed-fix-EXT_INT_STATUS_RX_FBUF-defi.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 362 | `752-13-v6.7-net-ethernet-mtk_wed-add-mtk_wed_soc_data-structure.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 363 | `752-14-v6.7-net-ethernet-mtk_wed-introduce-WED-support-for-MT798.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 364 | `752-15-v6.7-net-ethernet-mtk_wed-refactor-mtk_wed_check_wfdma_rx.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 365 | `752-16-v6.7-net-ethernet-mtk_wed-introduce-partial-AMSDU-offload.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 366 | `752-17-v6.7-net-ethernet-mtk_wed-introduce-hw_rro-support-for-MT.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 367 | `752-18-v6.7-net-ethernet-mtk_wed-debugfs-move-wed_v2-specific-re.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 368 | `752-19-v6.7-net-ethernet-mtk_wed-debugfs-add-WED-3.0-debugfs-ent.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 369 | `752-20-v6.7-net-ethernet-mtk_wed-add-wed-3.0-reset-support.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 370 | `752-24-v6.8-net-ethernet-mtk_wed-add-support-for-devices-with-mo.patch` | **DROP** | 6.8 | Included in kernel 6.6+ (v6.8) |
| 371 | `753-v6.9-net-ethernet-mtk_eth_soc-fix-WED-wifi-reset.patch` | **DROP** | 6.9 | Included in kernel 6.6+ (v6.9) |
| 372 | `754-25-v6.10-net-ethernet-mtk_eth_soc-handle-dma-buffer-size-soc-.patch` | **DROP** | 6.10 | Included in kernel 6.6+ (v6.10) |
| 373 | `754-29-v6.10-net-ethernet-mtk_ppe-Change-PPE-entries-number-to-16.patch` | **DROP** | 6.10 | Included in kernel 6.6+ (v6.10) |
| 374 | `754-30-v6.10-net-ethernet-mtk_eth_soc-implement-.-get-set-_pausep.patch` | **DROP** | 6.10 | Included in kernel 6.6+ (v6.10) |
| 375 | `764-01-v5.16-net-dsa-qca8k-fix-internal-delay-applied-to-the-wrong-PAD.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 376 | `764-02-v5.16-net-dsa-qca8k-fix-MTU-calculation.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 377 | `764-03-v5.17-net-next-net-dsa-qca8k-remove-redundant-check-in-parse_port_config.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 378 | `764-04-v5.17-net-next-net-dsa-qca8k-convert-to-GENMASK_FIELD_PREP_FIELD_GET.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 379 | `764-05-v5.17-net-next-net-dsa-qca8k-remove-extra-mutex_init-in-qca8k_setup.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 380 | `764-06-v5.17-net-next-net-dsa-qca8k-move-regmap-init-in-probe-and-set-it.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 381 | `764-07-v5.17-net-next-net-dsa-qca8k-initial-conversion-to-regmap-heper.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 382 | `764-08-v5.17-net-next-net-dsa-qca8k-add-additional-MIB-counter-and-.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 383 | `764-09-v5.17-net-next-net-dsa-qca8k-add-support-for-port-fast-aging.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 384 | `764-10-v5.17-net-next-net-dsa-qca8k-add-set_ageing_time-support.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 385 | `764-11-v5.17-net-next-net-dsa-qca8k-add-support-for-mdb_add-del.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 386 | `764-12-v5.17-net-next-net-dsa-qca8k-add-support-for-mirror-mode.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 387 | `764-13-v5.17-net-next-net-dsa-qca8k-add-LAG-support.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 388 | `764-14-v5.17-net-next-net-dsa-qca8k-fix-warning-in-LAG-feature.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 389 | `765-v5.17-01-net-next-net-dsa-reorder-PHY-initialization-with-MTU-setup-in.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 390 | `765-v5.17-02-net-next-net-dsa-merge-rtnl_lock-sections-in-dsa_slave_create.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 391 | `765-v5.17-03-net-next-net-dsa-stop-updating-master-MTU-from-master.c.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 392 | `765-v5.17-04-net-next-net-dsa-hold-rtnl_mutex-when-calling-dsa_master_-set.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 393 | `765-v5.17-05-net-next-net-dsa-first-set-up-shared-ports-then-non-shared-po.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 394 | `765-v5.17-06-net-next-net-dsa-setup-master-before-ports.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 395 | `766-v5.18-01-net-dsa-provide-switch-operations-for-tracking-the-m.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 396 | `766-v5.18-02-net-dsa-replay-master-state-events-in-dsa_tree_-setu.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 397 | `766-v5.18-03-net-dsa-tag_qca-convert-to-FIELD-macro.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 398 | `766-v5.18-04-net-dsa-tag_qca-move-define-to-include-linux-dsa.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 399 | `766-v5.18-05-net-dsa-tag_qca-enable-promisc_on_master-flag.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 400 | `766-v5.18-06-net-dsa-tag_qca-add-define-for-handling-mgmt-Etherne.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 401 | `766-v5.18-07-net-dsa-tag_qca-add-define-for-handling-MIB-packet.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 402 | `766-v5.18-08-net-dsa-tag_qca-add-support-for-handling-mgmt-and-MI.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 403 | `766-v5.18-09-net-dsa-qca8k-add-tracking-state-of-master-port.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 404 | `766-v5.18-10-net-dsa-qca8k-add-support-for-mgmt-read-write-in-Eth.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 405 | `766-v5.18-11-net-dsa-qca8k-add-support-for-mib-autocast-in-Ethern.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 406 | `766-v5.18-12-net-dsa-qca8k-add-support-for-phy-read-write-with-mg.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 407 | `766-v5.18-13-net-dsa-qca8k-move-page-cache-to-driver-priv.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 408 | `766-v5.18-14-net-dsa-qca8k-cache-lo-and-hi-for-mdio-write.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 409 | `766-v5.18-15-net-dsa-qca8k-add-support-for-larger-read-write-size.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 410 | `766-v5.18-16-net-dsa-qca8k-introduce-qca8k_bulk_read-write-functi.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 411 | `767-v5.18-net-dsa-qca8k-check-correct-variable-in-qca8k_phy_et.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 412 | `768-v5.18-net-dsa-qca8k-fix-noderef.cocci-warnings.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 413 | `769-v5.19-01-net-dsa-qca8k-drop-MTU-tracking-from-qca8k_priv.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 414 | `769-v5.19-02-net-dsa-qca8k-drop-port_sts-from-qca8k_priv.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 415 | `769-v5.19-03-net-dsa-qca8k-rework-and-simplify-mdiobus-logic.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 416 | `769-v5.19-04-net-dsa-qca8k-drop-dsa_switch_ops-from-qca8k_priv.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 417 | `769-v5.19-05-net-dsa-qca8k-correctly-handle-mdio-read-error.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 418 | `769-v5.19-06-net-dsa-qca8k-unify-bus-id-naming-with-legacy-and-OF.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 419 | `770-v6.0-net-dsa-qca8k-move-driver-to-qca-dir.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 420 | `771-v6.0-01-net-dsa-qca8k-cache-match-data-to-speed-up-access.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 421 | `771-v6.0-02-net-dsa-qca8k-make-mib-autocast-feature-optional.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 422 | `771-v6.0-03-net-dsa-qca8k-move-mib-struct-to-common-code.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 423 | `771-v6.0-04-net-dsa-qca8k-move-qca8k-read-write-rmw-and-reg-tabl.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 424 | `771-v6.0-05-net-dsa-qca8k-move-qca8k-bulk-read-write-helper-to-c.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 425 | `771-v6.0-06-net-dsa-qca8k-move-mib-init-function-to-common-code.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 426 | `771-v6.0-07-net-dsa-qca8k-move-port-set-status-eee-ethtool-stats.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 427 | `771-v6.0-08-net-dsa-qca8k-move-bridge-functions-to-common-code.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 428 | `771-v6.0-09-net-dsa-qca8k-move-set-age-MTU-port-enable-disable-f.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 429 | `771-v6.0-10-net-dsa-qca8k-move-port-FDB-MDB-function-to-common-c.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 430 | `771-v6.0-11-net-dsa-qca8k-move-port-mirror-functions-to-common-c.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 431 | `771-v6.0-12-net-dsa-qca8k-move-port-VLAN-functions-to-common-cod.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 432 | `771-v6.0-13-net-dsa-qca8k-move-port-LAG-functions-to-common-code.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 433 | `771-v6.0-14-net-dsa-qca8k-move-read_switch_id-function-to-common.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 434 | `772-v6.0-net-dsa-qca8k-fix-NULL-pointer-dereference-for-of_de.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 435 | `773-v5.18-1-net-dsa-Move-VLAN-filtering-syncing-out-of-dsa_switc.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 436 | `773-v5.18-2-net-dsa-Avoid-cross-chip-syncing-of-VLAN-filtering.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 437 | `774-v5.16-01-net-dsa-rtl8366rb-Support-bridge-offloading.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 438 | `774-v5.16-02-net-dsa-rtl8366-Drop-custom-VLAN-set-up.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 439 | `774-v5.16-03-net-dsa-rtl8366rb-Rewrite-weird-VLAN-filering-enable.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 440 | `774-v5.16-06-net-dsa-rtl8366-Drop-and-depromote-pointless-prints.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 441 | `774-v5.16-07-net-dsa-rtl8366rb-Use-core-filtering-tracking.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 442 | `774-v5.16-08-net-dsa-rtl8366rb-Support-disabling-learning.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 443 | `774-v5.16-09-net-dsa-rtl8366rb-Support-fast-aging.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 444 | `774-v5.16-10-net-dsa-rtl8366rb-Support-setting-STP-state.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 445 | `775-v6.0-01-net-ethernet-stmicro-stmmac-move-queue-reset-to-dedi.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 446 | `775-v6.0-02-net-ethernet-stmicro-stmmac-first-disable-all-queues.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 447 | `775-v6.0-03-net-ethernet-stmicro-stmmac-move-dma-conf-to-dedicat.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 448 | `775-v6.0-04-net-ethernet-stmicro-stmmac-generate-stmmac-dma-conf.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 449 | `775-v6.0-05-net-ethernet-stmicro-stmmac-permit-MTU-change-with-i.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 450 | `776-v6.1-01-net-dsa-qca8k-fix-inband-mgmt-for-big-endian-systems.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 451 | `776-v6.1-02-net-dsa-qca8k-fix-ethtool-autocast-mib-for-big-endia.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 452 | `777-v6.2-01-net-dsa-qca8k-fix-wrong-length-value-for-mgmt-eth-pa.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 453 | `777-v6.2-02-net-dsa-tag_qca-fix-wrong-MGMT_DATA2-size.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 454 | `777-v6.2-03-Revert-net-dsa-qca8k-cache-lo-and-hi-for-mdio-write.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 455 | `777-v6.2-04-net-dsa-qca8k-introduce-single-mii-read-write-lo-hi.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 456 | `777-v6.2-05-net-dsa-qca8k-improve-mdio-master-read-write-by-usin.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 457 | `778-v5.18-01-net-phy-at803x-add-fiber-support.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 458 | `778-v5.18-02-net-phy-at803x-support-downstream-SFP-cage.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 459 | `778-v5.18-03-net-phy-at803x-fix-NULL-pointer-dereference-on-AR9331-PHY.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 460 | `778-v5.18-04-net-phy-at803x-fix-error-return-code-in-at803x_probe.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 461 | `780-v5.16-bus-mhi-pci_generic-Introduce-Sierra-EM919X-support.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 462 | `781-v6.1-bus-mhi-host-always-print-detected-modem-name.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 463 | `782-v6.1-net-dsa-mt7530-add-support-for-in-band-link-status.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 464 | `783-v6.1-net-sfp-re-implement-soft-state-polling-setup.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 465 | `784-v6.1-net-sfp-move-quirk-handling-into-sfp.c.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 466 | `785-v6.1-net-sfp-move-Alcatel-Lucent-3FE46541AA-fixup.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 467 | `786-v6.1-net-sfp-move-Huawei-MA5671A-fixup.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 468 | `787-v6.1-net-sfp-add-support-for-HALNy-GPON-SFP.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 469 | `788-v6.3-net-dsa-mt7530-use-external-PCS-driver.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 470 | `789-v6.3-net-sfp-add-quirk-enabling-2500Base-x-for-HG-MXPD-48.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 471 | `790-v6.0-net-mii-add-mii_bmcr_encode_fixed.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 472 | `790-v6.4-0001-net-dsa-mt7530-make-some-noise-if-register-read-fail.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 473 | `790-v6.4-0002-net-dsa-mt7530-refactor-SGMII-PCS-creation.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 474 | `790-v6.4-0003-net-dsa-mt7530-use-unlocked-regmap-accessors.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 475 | `790-v6.4-0004-net-dsa-mt7530-use-regmap-to-access-switch-register-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 476 | `790-v6.4-0005-net-dsa-mt7530-move-SGMII-PCS-creation-to-mt7530_pro.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 477 | `790-v6.4-0006-net-dsa-mt7530-introduce-mutex-helpers.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 478 | `790-v6.4-0007-net-dsa-mt7530-move-p5_intf_modes-function-to-mt7530.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 479 | `790-v6.4-0008-net-dsa-mt7530-introduce-mt7530_probe_common-helper-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 480 | `790-v6.4-0009-net-dsa-mt7530-introduce-mt7530_remove_common-helper.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 481 | `790-v6.4-0011-net-dsa-mt7530-introduce-separate-MDIO-driver.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 482 | `790-v6.4-0012-net-dsa-mt7530-skip-locking-if-MDIO-bus-isn-t-presen.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 483 | `790-v6.4-0013-net-dsa-mt7530-introduce-driver-for-MT7988-built-in-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 484 | `790-v6.4-0014-net-dsa-mt7530-fix-support-for-MT7531BE.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 485 | `791-v6.2-01-net-phy-Add-driver-for-Motorcomm-yt8521-gigabit-ethernet.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 486 | `791-v6.2-02-net-phy-fix-yt8521-duplicated-argument-to-or.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 487 | `791-v6.2-03-net-phy-add-Motorcomm-YT8531S-phy-id.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 488 | `791-v6.3-04-net-phy-fix-the-spelling-problem-of-Sentinel.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 489 | `791-v6.3-05-net-phy-motorcomm-change-the-phy-id-of-yt8521-and-yt8531s.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 490 | `791-v6.3-06-net-phy-Add-BIT-macro-for-Motorcomm-yt8521-yt8531-gigabit.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 491 | `791-v6.3-07-net-phy-Add-dts-support-for-Motorcomm-yt8521-gigabit.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 492 | `791-v6.3-08-net-phy-Add-dts-support-for-Motorcomm-yt8531s-gigabit.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 493 | `791-v6.3-09-net-phy-Add-driver-for-Motorcomm-yt8531-gigabit-ethernet.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 494 | `791-v6.3-10-net-phy-motorcomm-uninitialized-variables-in.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 495 | `791-v6.6-11-net-phy-motorcomm-Add-pad-drive-strength-cfg-support.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 496 | `792-01-v6.0-net-phylink-disable-PCS-polling-over-major-configura.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 497 | `792-02-v6.0-net-phylink-fix-NULL-pl-pcs-dereference-during-phyli.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 498 | `792-03-v6.6-net-phylink-add-pcs_enable-pcs_disable-methods.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 499 | `792-v5.16-net-dpaa2-mac-add-support-for-more-10G-modes.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 500 | `793-v6.6-net-pcs-lynxi-implement-pcs_disable-op.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 501 | `794-v6.2-net-core-Allow-live-renaming-when-an-interface-is-up.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 502 | `796-v6.5-01-usbnet-ipheth-fix-risk-of-NULL-pointer-deallocation.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 503 | `796-v6.5-02-usbnet-ipheth-transmit-URBs-without-trailing-padding.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 504 | `796-v6.5-03-usbnet-ipheth-add-CDC-NCM-support.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 505 | `796-v6.5-04-usbnet-ipheth-update-Kconfig-description.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 506 | `797-v5.17-net-usb-ax88179_178a-add-TSO-feature.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 507 | `798-net-next-net-sfp-add-quirk-for-Fiberstone-GPON-ONU-34-20BI.patch` | **MIGRATE** | None | Unknown - needs verification |
| 508 | `800-v6.0-0001-dt-bindings-leds-add-Broadcom-s-BCM63138-controller.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 509 | `800-v6.0-0002-leds-bcm63138-add-support-for-BCM63138-controller.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 510 | `801-v6.0-0001-dt-bindings-leds-leds-bcm63138-unify-full-stops-in-d.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 511 | `801-v6.0-0002-leds-add-help-info-about-BCM63138-module-name.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 512 | `801-v6.0-0003-leds-leds-bcm63138-get-rid-of-LED_OFF.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 513 | `802-v5.16-0001-nvmem-core-rework-nvmem-cell-instance-creation.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 514 | `802-v5.16-0002-nvmem-core-add-nvmem-cell-post-processing-callback.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 515 | `802-v5.16-0003-nvmem-imx-ocotp-add-support-for-post-processing.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 516 | `803-v5.17-0002-nvmem-mtk-efuse-support-minimum-one-byte-access-stri.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 517 | `804-v5.18-0001-nvmem-core-Remove-unused-devm_nvmem_unregister.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 518 | `804-v5.18-0002-nvmem-core-Use-devm_add_action_or_reset.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 519 | `804-v5.18-0003-nvmem-core-Check-input-parameter-for-NULL-in-nvmem_u.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 520 | `804-v5.18-0004-nvmem-qfprom-fix-kerneldoc-warning.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 521 | `804-v5.18-0005-nvmem-sunxi_sid-Add-support-for-D1-variant.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 522 | `804-v5.18-0006-nvmem-meson-mx-efuse-replace-unnecessary-devm_kstrdu.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 523 | `804-v5.18-0007-nvmem-add-driver-for-Layerscape-SFP-Security-Fuse-Pr.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 524 | `804-v5.18-0008-nvmem-qfprom-Increase-fuse-blow-timeout-to-prevent-w.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 525 | `804-v5.18-0009-nvmem-Add-driver-for-OCOTP-in-Sunplus-SP7021.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 526 | `804-v5.18-0010-nvmem-brcm_nvram-parse-NVRAM-content-into-NVMEM-cell.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 527 | `805-v5.19-0001-nvmem-bcm-ocotp-mark-ACPI-device-ID-table-as-maybe-u.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 528 | `805-v5.19-0002-nvmem-sunplus-ocotp-staticize-sp_otp_v0.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 529 | `805-v5.19-0003-nvmem-sunplus-ocotp-drop-useless-probe-confirmation.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 530 | `805-v5.19-0004-nvmem-core-support-passing-DT-node-in-cell-info.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 531 | `805-v5.19-0005-nvmem-brcm_nvram-find-Device-Tree-nodes-for-NVMEM-ce.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 532 | `805-v5.19-0006-nvmem-Add-Apple-eFuse-driver.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 533 | `805-v5.19-0007-nvmem-qfprom-using-pm_runtime_resume_and_get-instead.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 534 | `805-v5.19-0008-nvmem-sfp-Use-regmap.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 535 | `805-v5.19-0009-nvmem-sfp-Add-support-for-TA-2.1-devices.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 536 | `806-v6.0-0001-nvmem-microchip-otpc-add-support.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 537 | `806-v6.0-0002-nvmem-mtk-efuse-Simplify-with-devm_platform_get_and_.patch` | **DROP** | 6.0 | Already in upstream 6.0 |
| 538 | `807-v6.1-0002-nvmem-add-driver-handling-U-Boot-environment-variabl.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 539 | `807-v6.1-0004-nvmem-brcm_nvram-Use-kzalloc-for-allocating-only-one.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 540 | `807-v6.1-0005-nvmem-prefix-all-symbols-with-NVMEM_.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 541 | `807-v6.1-0006-nvmem-sort-config-symbols-alphabetically.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 542 | `807-v6.1-0007-nvmem-u-boot-env-find-Device-Tree-nodes-for-NVMEM-ce.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 543 | `807-v6.1-0008-nvmem-lan9662-otp-add-support.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 544 | `807-v6.1-0009-nvmem-u-boot-env-fix-crc32-casting-type.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 545 | `807-v6.1-0010-nvmem-lan9662-otp-Fix-compatible-string.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 546 | `807-v6.1-0011-nvmem-u-boot-env-fix-crc32_data_offset-on-redundant-.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 547 | `807-v6.1-0013-nvmem-lan9662-otp-Change-return-type-of-lan9662_otp_.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 548 | `808-v6.2-0001-nvmem-stm32-move-STM32MP15_BSEC_NUM_LOWER-in-config.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 549 | `808-v6.2-0002-nvmem-stm32-add-warning-when-upper-OTPs-are-updated.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 550 | `808-v6.2-0003-nvmem-stm32-add-nvmem-type-attribute.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 551 | `808-v6.2-0004-nvmem-stm32-fix-spelling-typo-in-comment.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 552 | `808-v6.2-0005-nvmem-Kconfig-Fix-spelling-mistake-controlls-control.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 553 | `808-v6.2-0006-nvmem-u-boot-env-add-Broadcom-format-support.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 554 | `808-v6.2-0007-nvmem-brcm_nvram-Add-check-for-kzalloc.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 555 | `808-v6.2-0008-nvmem-sunxi_sid-Always-use-32-bit-MMIO-reads.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 556 | `808-v6.2-0013-nvmem-core-fix-device-node-refcounting.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 557 | `809-v6.3-0001-nvmem-core-remove-spurious-white-space.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 558 | `809-v6.3-0002-nvmem-core-add-an-index-parameter-to-the-cell.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 559 | `809-v6.3-0003-nvmem-core-move-struct-nvmem_cell_info-to-nvmem-prov.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 560 | `809-v6.3-0004-nvmem-core-drop-the-removal-of-the-cells-in-nvmem_ad.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 561 | `809-v6.3-0005-nvmem-core-add-nvmem_add_one_cell.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 562 | `809-v6.3-0006-nvmem-core-use-nvmem_add_one_cell-in-nvmem_add_cells.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 563 | `809-v6.3-0007-nvmem-stm32-add-OP-TEE-support-for-STM32MP13x.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 564 | `809-v6.3-0008-nvmem-stm32-detect-bsec-pta-presence-for-STM32MP15x.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 565 | `809-v6.3-0009-nvmem-rave-sp-eeprm-fix-kernel-doc-bad-line-warning.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 566 | `809-v6.3-0010-nvmem-qcom-spmi-sdam-register-at-device-init-time.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 567 | `809-v6.3-0011-nvmem-stm32-fix-OPTEE-dependency.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 568 | `810-v5.17-net-qmi_wwan-add-ZTE-MF286D-modem-19d2-1485.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 569 | `811-v6.4-0001-nvmem-xilinx-zynqmp-make-modular.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 570 | `811-v6.4-0002-nvmem-core-introduce-NVMEM-layouts.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 571 | `811-v6.4-0003-nvmem-core-handle-the-absence-of-expected-layouts.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 572 | `811-v6.4-0004-nvmem-core-request-layout-modules-loading.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 573 | `811-v6.4-0005-nvmem-core-add-per-cell-post-processing.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 574 | `811-v6.4-0006-nvmem-core-allow-to-modify-a-cell-before-adding-it.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 575 | `811-v6.4-0007-nvmem-imx-ocotp-replace-global-post-processing-with-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 576 | `811-v6.4-0008-nvmem-cell-drop-global-cell_post_process.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 577 | `811-v6.4-0009-nvmem-core-provide-own-priv-pointer-in-post-process-.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 578 | `811-v6.4-0010-nvmem-layouts-sl28vpd-Add-new-layout-driver.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 579 | `811-v6.4-0011-nvmem-layouts-onie-tlv-Add-new-layout-driver.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 580 | `811-v6.4-0012-nvmem-stm32-romem-mark-OF-related-data-as-maybe-unus.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 581 | `811-v6.4-0013-nvmem-mtk-efuse-Support-postprocessing-for-GPU-speed.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 582 | `811-v6.4-0014-nvmem-bcm-ocotp-Use-devm_platform_ioremap_resource.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 583 | `811-v6.4-0015-nvmem-nintendo-otp-Use-devm_platform_ioremap_resourc.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 584 | `811-v6.4-0016-nvmem-vf610-ocotp-Use-devm_platform_get_and_ioremap_.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 585 | `811-v6.4-0017-nvmem-core-support-specifying-both-cell-raw-data-pos.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 586 | `811-v6.4-0018-nvmem-u-boot-env-post-process-ethaddr-env-variable.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 587 | `811-v6.4-0019-nvmem-Add-macro-to-register-nvmem-layout-drivers.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 588 | `811-v6.4-0020-nvmem-layouts-sl28vpd-Use-module_nvmem_layout_driver.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 589 | `811-v6.4-0021-nvmem-layouts-onie-tlv-Use-module_nvmem_layout_drive.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 590 | `811-v6.4-0022-nvmem-layouts-onie-tlv-Drop-wrong-module-alias.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 591 | `811-v6.4-0023-nvmem-layouts-sl28vpd-set-varaiable-sl28vpd_layout-s.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 592 | `812-v6.2-firmware-nvram-bcm47xx-support-init-from-IO-memory.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 593 | `813-v6.5-0001-nvmem-imx-ocotp-set-varaiable-imx_ocotp_layout-stora.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 594 | `813-v6.5-0002-nvmem-imx-ocotp-Reverse-MAC-addresses-on-all-i.MX-de.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 595 | `813-v6.5-0003-nvmem-brcm_nvram-add-.read_post_process-for-MACs.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 596 | `813-v6.5-0004-nvmem-rockchip-otp-Add-clks-and-reg_read-to-rockchip.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 597 | `813-v6.5-0005-nvmem-rockchip-otp-Generalize-rockchip_otp_wait_stat.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 598 | `813-v6.5-0006-nvmem-rockchip-otp-Use-devm_reset_control_array_get_.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 599 | `813-v6.5-0007-nvmem-rockchip-otp-Improve-probe-error-handling.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 600 | `813-v6.5-0008-nvmem-rockchip-otp-Add-support-for-RK3588.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 601 | `813-v6.5-0009-nvmem-zynqmp-Switch-xilinx.com-emails-to-amd.com.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 602 | `813-v6.5-0010-nvmem-imx-support-i.MX93-OCOTP.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 603 | `813-v6.5-0011-nvmem-core-add-support-for-fixed-cells-layout.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 604 | `814-v6.3-leds-Move-led_init_default_state_get-to-the-global-h.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 605 | `815-v6.4-01-net-dsa-qca8k-move-qca8k_port_to_phy-to-header.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 606 | `815-v6.4-02-net-dsa-qca8k-add-LEDs-basic-support.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 607 | `815-v6.4-03-net-dsa-qca8k-add-LEDs-blink_set-support.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 608 | `815-v6.4-04-leds-Provide-stubs-for-when-CLASS_LED-NEW_LEDS-are-d.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 609 | `815-v6.4-05-net-phy-Add-a-binding-for-PHY-LEDs.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 610 | `815-v6.4-06-net-phy-phy_device-Call-into-the-PHY-driver-to-set-L.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 611 | `815-v6.4-07-net-phy-marvell-Add-software-control-of-the-LEDs.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 612 | `815-v6.4-08-net-phy-phy_device-Call-into-the-PHY-driver-to-set-L.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 613 | `815-v6.4-09-net-phy-marvell-Implement-led_blink_set.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 614 | `816-v6.4-net-phy-marvell-Fix-inconsistent-indenting-in-led_bl.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 615 | `817-v6.5-02-leds-trigger-netdev-Drop-NETDEV_LED_MODE_LINKUP-from.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 616 | `817-v6.5-03-leds-trigger-netdev-Rename-add-namespace-to-netdev-t.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 617 | `817-v6.5-04-leds-trigger-netdev-Convert-device-attr-to-macro.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 618 | `817-v6.5-05-leds-trigger-netdev-Use-mutex-instead-of-spinlocks.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 619 | `818-v6.5-01-leds-add-APIs-for-LEDs-hw-control.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 620 | `818-v6.5-02-leds-add-API-to-get-attached-device-for-LED-hw-contr.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 621 | `818-v6.5-03-Documentation-leds-leds-class-Document-new-Hardware-.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 622 | `818-v6.5-04-leds-trigger-netdev-refactor-code-setting-device-nam.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 623 | `818-v6.5-05-leds-trigger-netdev-introduce-check-for-possible-hw-.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 624 | `818-v6.5-06-leds-trigger-netdev-add-basic-check-for-hw-control-s.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 625 | `818-v6.5-07-leds-trigger-netdev-reject-interval-store-for-hw_con.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 626 | `818-v6.5-08-leds-trigger-netdev-add-support-for-LED-hw-control.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 627 | `818-v6.5-09-leds-trigger-netdev-validate-configured-netdev.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 628 | `818-v6.5-10-leds-trigger-netdev-init-mode-if-hw-control-already-.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 629 | `818-v6.5-11-leds-trigger-netdev-expose-netdev-trigger-modes-in-l.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 630 | `818-v6.5-12-net-dsa-qca8k-implement-hw_control-ops.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 631 | `818-v6.5-13-net-dsa-qca8k-add-op-to-get-ports-netdev.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 632 | `819-v6.6-0001-nvmem-sunxi_sid-Convert-to-devm_platform_ioremap_res.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 633 | `819-v6.6-0002-nvmem-brcm_nvram-Use-devm_platform_get_and_ioremap_r.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 634 | `819-v6.6-0003-nvmem-lpc18xx_otp-Convert-to-devm_platform_ioremap_r.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 635 | `819-v6.6-0004-nvmem-meson-mx-efuse-Convert-to-devm_platform_iorema.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 636 | `819-v6.6-0005-nvmem-rockchip-efuse-Use-devm_platform_get_and_iorem.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 637 | `819-v6.6-0006-nvmem-stm32-romem-Use-devm_platform_get_and_ioremap_.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 638 | `819-v6.6-0007-nvmem-qfprom-do-some-cleanup.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 639 | `819-v6.6-0008-nvmem-uniphier-Use-devm_platform_get_and_ioremap_res.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 640 | `819-v6.6-0009-nvmem-add-new-NXP-QorIQ-eFuse-driver.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 641 | `819-v6.6-0011-nvmem-Kconfig-Fix-typo-drive-driver.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 642 | `819-v6.6-0012-nvmem-sec-qfprom-Add-Qualcomm-secure-QFPROM-support.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 643 | `819-v6.6-0013-nvmem-u-boot-env-Replace-zero-length-array-with-DECL.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 644 | `819-v6.6-0014-nvmem-core-Create-all-cells-before-adding-the-nvmem-.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 645 | `819-v6.6-0015-nvmem-core-Return-NULL-when-no-nvmem-layout-is-found.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 646 | `819-v6.6-0016-nvmem-core-Do-not-open-code-existing-functions.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 647 | `819-v6.6-0017-nvmem-core-Notify-when-a-new-layout-is-registered.patch` | **DROP** | 6.6 | Already in upstream 6.6 |
| 648 | `820-v6.7-0001-nvmem-qfprom-Mark-core-clk-as-optional.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 649 | `820-v6.7-0002-nvmem-add-explicit-config-option-to-read-old-syntax-.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 650 | `820-v6.7-0003-nvmem-Use-device_get_match_data.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 651 | `820-v6.7-0004-Revert-nvmem-add-new-config-option.patch` | **DROP** | 6.7 | Included in kernel 6.6+ (v6.7) |
| 652 | `821-v5.16-Bluetooth-btusb-Support-public-address-configuration.patch` | **DROP** | 5.16 | Already in upstream 5.16 |
| 653 | `822-v5.17-Bluetooth-btusb-Fix-application-of-sizeof-to-pointer.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 654 | `823-v5.18-Bluetooth-btusb-Add-a-new-PID-VID-13d3-3567-for-MT79.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 655 | `824-v5.19-Bluetooth-btusb-Add-a-new-PID-VID-0489-e0c8-for-MT79.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 656 | `825-v6.1-Bluetooth-btusb-Add-a-new-VID-PID-0e8d-0608-for-MT79.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 657 | `826-v5.17-of-base-make-small-of_parse_phandle-variants-static-.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 658 | `827-v6.3-0001-of-base-add-of_parse_phandle_with_optional_args.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 659 | `827-v6.3-0002-of-property-make-.-cells-optional-for-simple-props.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 660 | `827-v6.3-0003-of-property-add-nvmem-cell-cells-property.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 661 | `827-v6.3-0004-of-device-Ignore-modalias-of-reused-nodes.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 662 | `827-v6.3-0005-of-device-Do-not-ignore-error-code-in-of_device_ueve.patch` | **DROP** | 6.3 | Already in upstream 6.3 |
| 663 | `828-v6.4-0002-of-Update-of_device_get_modalias.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 664 | `828-v6.4-0003-of-Rename-of_modalias_node.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 665 | `828-v6.4-0004-of-Move-of_modalias-to-module.c.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 666 | `828-v6.4-0005-of-Move-the-request-module-helper-logic-to-module.c.patch` | **DROP** | 6.4 | Already in upstream 6.4 |
| 667 | `831-v6.1-dt-bindings-leds-Expand-LED_COLOR_ID-definitions.patch` | **DROP** | 6.1 | Already in upstream 6.1 |
| 668 | `833-v6.8-leds-core-Add-more-colors-from-DT-bindings-to-led_co.patch.patch` | **DROP** | 6.8 | Included in kernel 6.6+ (v6.8) |
| 669 | `835-v6.9-0001-dt-bindings-leds-Add-FUNCTION-defines-for-per-band-W.patch` | **DROP** | 6.9 | Included in kernel 6.6+ (v6.9) |
| 670 | `835-v6.9-0002-dt-bindings-leds-Add-LED_FUNCTION_WAN_ONLINE-for-Int.patch` | **DROP** | 6.9 | Included in kernel 6.6+ (v6.9) |
| 671 | `840-v6.14-gpio-regmap-Use-generic-request-free-ops.patch` | **DROP** | 6.14 | Included in kernel 6.6+ (v6.14) |
| 672 | `860-v5.17-MIPS-ath79-drop-_machine_restart-again.patch` | **DROP** | 5.17 | Already in upstream 5.17 |
| 673 | `870-v5.18-hwmon-lm70-Add-ti-tmp125-support.patch` | **DROP** | 5.18 | Already in upstream 5.18 |
| 674 | `880-v5.19-cdc_ether-export-usbnet_cdc_zte_rx_fixup.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 675 | `881-v5.19-rndis_host-enable-the-bogus-MAC-fixup-for-ZTE-device.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 676 | `882-v5.19-rndis_host-limit-scope-of-bogus-MAC-address-detectio.patch` | **DROP** | 5.19 | Already in upstream 5.19 |
| 677 | `890-v6.2-mtd-spinand-winbond-fix-flash-detection.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 678 | `891-v6.2-mtd-spinand-winbond-add-W25N02KV.patch` | **DROP** | 6.2 | Already in upstream 6.2 |
| 679 | `892-v6.5-mtd-spinand-winbond-Fix-ecc_get_status.patch` | **DROP** | 6.5 | Already in upstream 6.5 |
| 680 | `893-v6.12-mtd-spinand-winbond-add-support-for-W25N01KV.patch` | **DROP** | 6.12 | Included in kernel 6.6+ (v6.12) |
| 681 | `894-v6.8-net-ethtool-implement-ethtool_puts.patch` | **DROP** | 6.8 | Included in kernel 6.6+ (v6.8) |

## Pending Patches (pending-5.15 -> pending-6.6)

Total: 132 patches

| # | Filename | Disposition | Upstream Ver | Reason |
|---|----------|-------------|--------------|--------|
| 1 | `100-compiler.h-only-include-asm-rwonce.h-for-kernel-code.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 2 | `102-MIPS-only-process-negative-stack-offsets-on-stack-tr.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 3 | `103-kbuild-export-SUBARCH.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 4 | `110-v6.3-0002-spidev-Add-Silicon-Labs-SI3210-device-compatible.patch` | **CHECK** | 6.3 | Has v6.3 tag - verify if merged in 6.6 |
| 5 | `111-watchdog-max63xx_wdt-Add-support-for-specifying-WDI-.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 6 | `120-Fix-alloc_node_mem_map-with-ARCH_PFN_OFFSET-calcu.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 7 | `140-jffs2-use-.rename2-and-add-RENAME_WHITEOUT-support.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 8 | `141-jffs2-add-RENAME_EXCHANGE-support.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 9 | `142-jffs2-add-splice-ops.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 10 | `150-bridge_allow_receiption_on_disabled_port.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 11 | `151-net-bridge-do-not-send-arp-replies-if-src-and-target.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 12 | `190-rtc-rs5c372-support_alarms_up_to_1_week.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 13 | `191-rtc-rs5c372-let_the_alarm_to_be_used_as_wakeup_source.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 14 | `203-kallsyms_uncompressed.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 15 | `205-backtrace_module_info.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 16 | `240-remove-unsane-filenames-from-deps_initramfs-list.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 17 | `261-enable_wilink_platform_without_drivers.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 18 | `270-platform-mikrotik-build-bits.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 19 | `300-mips_expose_boot_raw.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 20 | `301-MIPS-Add-barriers-between-dcache-icache-flushes.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 21 | `302-mips_no_branch_likely.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 22 | `305-mips_module_reloc.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 23 | `308-mips32r2_tune.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 24 | `310-arm_module_unresolved_weak_sym.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 25 | `330-MIPS-kexec-Accept-command-line-parameters-from-users.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 26 | `332-arc-add-OWRTDTB-section.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 27 | `333-arc-enable-unaligned-access-in-kernel-mode.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 28 | `342-powerpc-Enable-kernel-XZ-compression-option-on-PPC_8.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 29 | `351-irqchip-bcm-6345-l1-request-memory-region.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 30 | `400-mtd-mtdsplit-support.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 31 | `401-mtd-don-t-register-NVMEM-devices-for-partitions-with.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 32 | `402-mtd-spi-nor-write-support-for-minor-aligned-partitions.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 33 | `420-mtd-redboot_space.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 34 | `430-mtd-add-myloader-partition-parser.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 35 | `431-mtd-bcm47xxpart-check-for-bad-blocks-when-calculatin.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 36 | `432-mtd-bcm47xxpart-detect-T_Meter-partition.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 37 | `435-mtd-add-routerbootpart-parser-config.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 38 | `460-mtd-cfi_cmdset_0002-no-erase_suspend.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 39 | `461-mtd-cfi_cmdset_0002-add-buffer-write-cmd-timeout.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 40 | `465-m25p80-mx-disable-software-protection.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 41 | `476-mtd-spi-nor-add-eon-en25q128.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 42 | `477-mtd-spi-nor-add-eon-en25qx128a.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 43 | `479-mtd-spi-nor-add-xtx-xt25f128b.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 44 | `481-mtd-spi-nor-add-support-for-Gigadevice-GD25D05.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 45 | `482-mtd-spi-nor-add-gd25q512.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 46 | `484-mtd-spi-nor-add-esmt-f25l16pa.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 47 | `485-mtd-spi-nor-add-xmc-xm25qh128c.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 48 | `486-01-mtd-spinand-add-support-for-ESMT-F50x1G41LB.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 49 | `487-mtd-spinand-Add-support-for-Etron-EM73D044VCx.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 50 | `488-mtd-spi-nor-add-xmc-xm25qh64c.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 51 | `490-ubi-auto-attach-mtd-device-named-ubi-or-data-on-boot.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 52 | `491-ubi-auto-create-ubiblock-device-for-rootfs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 53 | `492-try-auto-mounting-ubi0-rootfs-in-init-do_mounts.c.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 54 | `493-ubi-set-ROOT_DEV-to-ubiblock-rootfs-if-unset.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 55 | `494-mtd-ubi-add-EOF-marker-support.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 56 | `496-dt-bindings-add-bindings-for-mtd-concat-devices.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 57 | `497-mtd-mtdconcat-add-dt-driver-for-concat-devices.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 58 | `498-mtd-spi-nor-locking-support-for-MX25L6405D.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 59 | `499-mtd-spi-nor-disable-16-bit-sr-for-macronix.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 60 | `500-fs_cdrom_dependencies.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 61 | `530-jffs2_make_lzma_available.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 62 | `532-jffs2_eofdetect.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 63 | `600-netfilter_conntrack_flush.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 64 | `610-netfilter_match_bypass_default_checks.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 65 | `611-netfilter_match_bypass_default_table.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 66 | `612-netfilter_match_reduce_memory_access.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 67 | `630-packet_socket_type.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 68 | `655-increase_skb_pad.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 69 | `666-Add-support-for-MAP-E-FMRs-mesh-mode.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 70 | `670-ipv6-allow-rejecting-with-source-address-failed-policy.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 71 | `671-net-provide-defines-for-_POLICY_FAILED-until-all-cod.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 72 | `680-NET-skip-GRO-for-foreign-MAC-addresses.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 73 | `682-of_net-add-mac-address-increment-support.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 74 | `683-of_net-add-mac-address-to-of-tree.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 75 | `684-of_net-do-mac-address-increment-only-once.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 76 | `700-netfilter-nft_flow_offload-handle-netdevice-events-f.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 77 | `701-netfilter-nf_tables-ignore-EOPNOTSUPP-on-flowtable-d.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 78 | `702-net-ethernet-mtk_eth_soc-enable-threaded-NAPI.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 79 | `703-phy-add-detach-callback-to-struct-phy_driver.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 80 | `704-01-v6.4-net-mvneta-fix-transmit-path-dma-unmapping-on-error.patch` | **CHECK** | 6.4 | Has v6.4 tag - verify if merged in 6.6 |
| 81 | `704-02-v6.4-net-mvneta-mark-mapped-and-tso-buffers-separately.patch` | **CHECK** | 6.4 | Has v6.4 tag - verify if merged in 6.6 |
| 82 | `704-03-v6.4-net-mvneta-use-buf-type-to-determine-whether-to-dma-.patch` | **CHECK** | 6.4 | Has v6.4 tag - verify if merged in 6.6 |
| 83 | `704-04-v6.4-net-mvneta-move-tso_build_hdr-into-mvneta_tso_put_hd.patch` | **CHECK** | 6.4 | Has v6.4 tag - verify if merged in 6.6 |
| 84 | `704-05-v6.4-net-mvneta-allocate-TSO-header-DMA-memory-in-chunks.patch` | **CHECK** | 6.4 | Has v6.4 tag - verify if merged in 6.6 |
| 85 | `705-net-dsa-tag_mtk-add-padding-for-tx-packets.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 86 | `710-bridge-add-knob-for-filtering-rx-tx-BPDU-pack.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 87 | `721-net-phy-realtek-rtl8221-allow-to-configure-SERDES-mo.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 88 | `722-net-phy-realtek-support-switching-between-SGMII-and-.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 89 | `723-net-mt7531-ensure-all-MACs-are-powered-down-before-r.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 90 | `724-net-phy-realtek-use-genphy_soft_reset-for-2.5G-PHYs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 91 | `725-net-phy-realtek-disable-SGMII-in-band-AN-for-2-5G-PHYs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 92 | `726-net-phy-realtek-make-sure-paged-read-is-protected-by.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 93 | `727-net-phy-realtek-use-inline-functions-for-10GbE-adver.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 94 | `728-net-phy-realtek-check-validity-of-10GbE-link-partner.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 95 | `729-net-phy-realtek-introduce-rtl822x_probe.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 96 | `730-net-phy-realtek-detect-early-version-of-RTL8221B.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 97 | `731-net-phy-realtek-support-interrupt-of-RTL8221B.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 98 | `732-00-net-ethernet-mtk_eth_soc-compile-out-netsys-v2-code-.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 99 | `732-01-net-ethernet-mtk_eth_soc-work-around-issue-with-send.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 100 | `732-02-net-ethernet-mtk_eth_soc-set-NETIF_F_ALL_TSO.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 101 | `732-03-net-ethernet-mtk_eth_soc-fix-remaining-throughput-re.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 102 | `734-net-ethernet-mtk_eth_soc-ppe-fix-L2-offloading-with-.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 103 | `737-net-ethernet-mtk_eth_soc-add-paths-and-SerDes-modes-.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 104 | `738-net-ethernet-mtk_eth_soc-set-coherent-mask-to-get-PP.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 105 | `750-skb-Do-mix-page-pool-and-page-referenced-frags-in-GR.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 106 | `760-net-core-add-optional-threading-for-backlog-processi.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 107 | `768-net-dsa-mv88e6xxx-Request-assisted-learning-on-CPU-port.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 108 | `772-net-dsa-b53-add-support-for-BCM63xx-RGMIIs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 109 | `773-net-dsa-b53-mmap-add-more-63xx-SoCs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 110 | `774-net-dsa-b53-mmap-allow-passing-a-chip-ID.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 111 | `775-net-dsa-b53-add-BCM63268-RGMII-configuration.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 112 | `777-net-dsa-b53-mdio-add-support-for-BCM53134.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 113 | `780-ARM-kirkwood-add-missing-linux-if_ether.h-for-ETH_AL.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 114 | `790-bus-mhi-core-add-SBL-state-callback.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 115 | `795-mt7530-register-OF-node-for-internal-MDIO-bus.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 116 | `796-net-dsa-mt7530-fix-10M-100M-speed-on-MT7988-switch.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 117 | `800-bcma-get-SoC-device-struct-copy-its-DMA-params-to-th.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 118 | `801-gpio-gpio-cascade-add-generic-GPIO-cascade.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 119 | `802-nvmem-u-boot-env-align-endianness-of-crc32-values.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 120 | `803-nvmem-core-fix-support-for-fixed-cells-NVMEM-layout.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 121 | `804-nvmem-core-support-mac-base-fixed-layout-cells.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 122 | `810-pci_disable_common_quirks.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 123 | `811-pci_disable_usb_common_quirks.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 124 | `820-w1-gpio-fix-problem-with-platfom-data-in-w1-gpio.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 125 | `834-ledtrig-libata.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 126 | `840-hwrng-bcm2835-set-quality-to-1000.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 127 | `850-0023-PCI-aardvark-Make-main-irq_chip-structure-a-static-d.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 128 | `850-dt-bindings-clk-add-BCM63268-timer-clock-definitions.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 129 | `851-dt-bindings-reset-add-BCM63268-timer-reset-definitions.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 130 | `852-clk-bcm-Add-BCM63268-timer-clock-and-reset-driver.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 131 | `860-serial-8250_mtk-track-busclk-state-to-avoid-bus-error.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |
| 132 | `920-mangle_bootargs.patch` | **MIGRATE** | None | Port to pending-6.6 (needs rebase check) |

## Hack Patches (hack-5.15 -> hack-6.6)

Total: 56 patches

| # | Filename | Disposition | Reason |
|---|----------|-------------|--------|
| 1 | `204-module_strip.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 2 | `205-kconfig-abort-configuration-on-unset-symbol.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 3 | `210-darwin_scripts_include.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 4 | `211-darwin-uuid-typedef-clash.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 5 | `212-tools_portability.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 6 | `214-spidev_h_portability.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 7 | `220-arm-gc_sections.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 8 | `221-module_exports.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 9 | `230-openwrt_lzma_options.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 10 | `250-netfilter_depends.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 11 | `251-kconfig.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 12 | `253-ksmbd-config.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 13 | `259-regmap_dynamic.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 14 | `260-crypto_test_dependencies.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 15 | `261-lib-arc4-unhide.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 16 | `280-rfkill-stubs.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 17 | `300-MIPS-r4k_cache-use-more-efficient-cache-blast.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 18 | `402-mtd-blktrans-call-add-disks-after-mtd-device.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 19 | `410-block-fit-partition-parser.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 20 | `420-mtd-support-OpenWrt-s-MTD_ROOTFS_ROOT_DEV.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 21 | `421-drivers-mtd-parsers-add-nvmem-support-to-cmdlinepart.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 22 | `430-mtk-bmt-support.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 23 | `601-of_net-add-mac-address-ascii-support.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 24 | `645-netfilter-connmark-introduce-set-dscpmark.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 25 | `650-netfilter-add-xt_FLOWOFFLOAD-target.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 26 | `651-wireless_mesh_header.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 27 | `660-fq_codel_defaults.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 28 | `661-kernel-ct-size-the-hashtable-more-adequately.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 29 | `700-swconfig_switch_drivers.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 30 | `711-net-dsa-mv88e6xxx-disable-ATU-violation.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 31 | `720-net-phy-add-aqr-phys.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 32 | `721-net-add-packet-mangeling.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 33 | `722-net-phy-aquantia-enable-AQR112-and-AQR412.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 34 | `723-net-phy-aquantia-fix-system-side-protocol-mi.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 35 | `724-net-phy-aquantia-Add-AQR113-driver-support.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 36 | `725-net-phy-aquantia-add-PHY_IDs-for-AQR112-variants.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 37 | `726-net-eth-dpaa2-eth-do-not-hold-rtnl_lock.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 38 | `750-net-pcs-mtk-lynxi-workaround-2500BaseX-no-an.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 39 | `760-net-usb-r8152-add-LED-configuration-from-OF.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 40 | `761-dt-bindings-net-add-RTL8152-binding-documentation.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 41 | `765-mxl-gpy-control-LED-reg-from-DT.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 42 | `766-net-phy-mediatek-ge-add-LED-configuration-interface.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 43 | `773-bgmac-add-srab-switch.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 44 | `780-usb-net-MeigLink_modem_support.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 45 | `781-usb-net-rndis-support-asr.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 46 | `790-SFP-GE-T-ignore-TX_FAULT.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 47 | `795-backport-phylink_pcs-helpers.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 48 | `800-GPIO-add-named-gpio-exports.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 49 | `810-bcma-ssb-fallback-sprom.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 50 | `901-debloat_sock_diag.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 51 | `902-debloat_proc.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 52 | `904-debloat_dma_buf.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 53 | `910-kobject_uevent.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 54 | `911-kobject_add_broadcast_uevent.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 55 | `920-device_tree_cmdline.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
| 56 | `930-Revert-Revert-Revert-driver-core-Set-fw_devlink-on-b.patch` | **MIGRATE** | Hack patch - verify still needed in 6.6 |
