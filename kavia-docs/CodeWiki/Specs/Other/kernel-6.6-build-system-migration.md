# OpenWrt Kernel 6.6 Build System Migration

**Document Type:** Implementation Guide  
**Status:** In Progress  
**Version:** 1.0  
**Last Updated:** 2025-02-09

## Overview

This document describes the build system changes required to migrate OpenWrt from kernel 5.15 to kernel 6.6. It provides detailed explanations of each change and the rationale behind them.

## Summary of Changes

### 1. Kernel Version Definition (`include/kernel-6.6`)

**File:** `openwrt-318270/include/kernel-6.6`

**Purpose:** Defines the specific kernel version and tarball hash for the 6.6 LTS series.

**Changes:**
```makefile
LINUX_VERSION-6.6 = .68
LINUX_KERNEL_HASH-6.6.68 = 0000000000000000000000000000000000000000000000000000000000000000
```

**Rationale:**
- Uses 6.6.68 as it's the latest stable release in the 6.6 LTS series as of creation
- The hash placeholder (all zeros) must be updated with the actual SHA256 hash after downloading the kernel tarball from kernel.org
- Follows the same pattern as `include/kernel-5.15`

**Action Required:**
```bash
# Download the kernel and calculate hash:
wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.6.68.tar.xz
sha256sum linux-6.6.68.tar.xz
# Update LINUX_KERNEL_HASH-6.6.68 with the actual hash
```

### 2. Generic Kernel Configuration (`target/linux/generic/config-6.6`)

**File:** `openwrt-318270/target/linux/generic/config-6.6`

**Purpose:** Provides the baseline kernel configuration for 6.6 across all platforms.

**Key Changes from 5.15:**

#### A. New Options Added

1. **Rust Support**
   - `CONFIG_RUST` - Kernel 6.6 introduces optional Rust support
   - **Impact:** Requires Rust toolchain if enabled
   - **Recommendation:** Keep disabled initially (not set)

2. **BPF Enhancements**
   - `CONFIG_BPF_PRELOAD` - New BPF preloading mechanism
   - `CONFIG_BPF_STREAM_PARSER` - Enhanced BPF networking
   - **Impact:** Improved BPF performance and capabilities
   - **Recommendation:** Evaluate per-platform

3. **Security Features**
   - `CONFIG_SECURITY_LANDLOCK` - New LSM for unprivileged sandboxing
   - `CONFIG_INIT_ON_ALLOC_DEFAULT_ON` - Zero-on-alloc by default
   - `CONFIG_INIT_ON_FREE_DEFAULT_ON` - Zero-on-free by default
   - **Impact:** Enhanced security at cost of slight performance
   - **Recommendation:** Consider enabling for security-focused builds

4. **RCU Improvements**
   - `CONFIG_RCU_LAZY` - Lazy RCU callbacks for power saving
   - `CONFIG_RCU_STRICT_GRACE_PERIOD` - Stricter RCU validation
   - **Impact:** Better power efficiency options
   - **Recommendation:** Test lazy RCU on battery-powered devices

5. **Scheduler Updates**
   - `CONFIG_SCHED_CLASS_EXT` - Extensible scheduler classes
   - `CONFIG_ENERGY_MODEL` - CPU energy modeling
   - **Impact:** Better power-aware scheduling
   - **Recommendation:** Enable energy model for mobile/embedded

6. **Network Stack**
   - `CONFIG_INET_DIAG_DESTROY` - Socket destruction via netlink
   - `CONFIG_MPTCP` - Multipath TCP support
   - **Impact:** Enhanced networking capabilities
   - **Recommendation:** Enable MPTCP for multi-WAN routers

7. **Filesystem Updates**
   - `CONFIG_TMPFS_INODE64` - 64-bit inode numbers in tmpfs
   - **Impact:** Removes 32-bit inode limitation
   - **Recommendation:** Safe to enable on 64-bit platforms

8. **Memory Management**
   - `CONFIG_MEMORY_HOTPLUG` - Runtime memory add/remove
   - `CONFIG_MEMORY_HOTREMOVE` - Runtime memory removal
   - **Impact:** Typically not needed for embedded
   - **Recommendation:** Keep disabled

#### B. Removed/Deprecated Options

The following options from 5.15 are no longer valid in 6.6:

1. **`CONFIG_KCMP`** - Merged into core kernel, always available
2. **`CONFIG_CHECKPOINT_RESTORE`** - Now always enabled with KCMP
3. **Architecture-specific DMA zone changes** - Some ZONE_DMA32 handling changed

#### C. Changed Defaults

Several options have different default values in 6.6:

1. **RCU Configuration** - New lazy callback option available
2. **Security Defaults** - More options for memory zeroing
3. **Network Stack** - MPTCP available as module

### 3. Menuconfig Additions (`config/Config-kernel.in`)

**File:** `openwrt-318270/config/Config-kernel.in`

**Purpose:** Exposes new 6.6 kernel options to OpenWrt's build configuration system.

**New Configuration Sections:**

#### KERNEL_RUST
```kconfig
config KERNEL_RUST
	bool "Enable Rust support in the kernel"
	depends on !SMALL_FLASH
```
- Allows building Rust components in kernel
- Requires Rust toolchain (rustc, bindgen)
- Recommended: Disabled initially

#### KERNEL_RCU_LAZY
```kconfig
config KERNEL_RCU_LAZY
	bool "Enable lazy RCU callbacks"
```
- Defers RCU callbacks to save power
- Useful for battery-powered devices
- Recommended: Test before enabling

#### KERNEL_MPTCP
```kconfig
config KERNEL_MPTCP
	bool "Enable Multipath TCP support"
	depends on KERNEL_IPV6
```
- Enables MPTCP for multiple path redundancy
- Useful for multi-WAN configurations
- Recommended: Enable for advanced routers

#### KERNEL_SECURITY_LANDLOCK
```kconfig
config KERNEL_SECURITY_LANDLOCK
	bool "Enable Landlock security module"
	select KERNEL_SECURITY
```
- Sandboxing for unprivileged processes
- Improves application isolation
- Recommended: Consider for security builds

#### KERNEL_INIT_ON_ALLOC_DEFAULT_ON / KERNEL_INIT_ON_FREE_DEFAULT_ON
```kconfig
config KERNEL_INIT_ON_ALLOC_DEFAULT_ON
	bool "Enable heap memory zeroing on allocation by default"
	
config KERNEL_INIT_ON_FREE_DEFAULT_ON
	bool "Enable heap memory zeroing on free by default"
```
- Hardens against information leaks and use-after-free
- Performance impact (~5-10%)
- Recommended: Enable for security-critical devices

#### KERNEL_ENERGY_MODEL
```kconfig
config KERNEL_ENERGY_MODEL
	bool "Enable energy model for CPUs"
	depends on KERNEL_PM
```
- Enables power-aware scheduling
- Useful for battery-powered devices
- Recommended: Enable for mobile/IoT devices

#### KERNEL_MEMORY_HOTPLUG / KERNEL_MEMORY_HOTREMOVE
```kconfig
config KERNEL_MEMORY_HOTPLUG
	bool "Enable memory hotplug support"
	
config KERNEL_MEMORY_HOTREMOVE
	bool "Enable memory hot-remove support"
	depends on KERNEL_MEMORY_HOTPLUG
```
- Runtime memory management
- Not typically needed for embedded
- Recommended: Keep disabled

## Build System Integration

The kernel version is selected through the existing mechanism:

1. **Version Selection:** Platform Makefiles set `KERNEL_PATCHVER ?= 6.6`
2. **Config Loading:** Build system loads `target/linux/generic/config-6.6`
3. **Platform Override:** Platform-specific configs override generic settings
4. **Menuconfig:** User selections from `Config-kernel.in` merge into final config

## Testing Checklist

Before deploying kernel 6.6, test the following:

- [ ] **Boot Test:** Device boots successfully with new kernel
- [ ] **Network:** All network interfaces function correctly
- [ ] **Wireless:** WiFi drivers load and work (if applicable)
- [ ] **Storage:** Filesystem mount and I/O operations
- [ ] **USB:** USB device detection and operation
- [ ] **Performance:** No significant performance regressions
- [ ] **Power:** Power consumption within acceptable range
- [ ] **Stability:** No kernel panics or crashes in 24-hour stress test
- [ ] **Security:** SELinux/security policies still function
- [ ] **Userspace:** All userspace applications work correctly

## Platform Migration Guide

For platform maintainers to migrate from 5.15 to 6.6:

### Step 1: Update Platform Kernel Version
```makefile
# In target/linux/<platform>/Makefile
KERNEL_PATCHVER:=6.6
```

### Step 2: Review Platform Config
```bash
# Compare platform config with generic config-6.6
diff target/linux/generic/config-6.6 target/linux/<platform>/config-6.6
```

### Step 3: Update Platform-Specific Options
- Review each `REVIEW REQUIRED` comment in generic config
- Update platform config for hardware-specific needs
- Test new options with platform hardware

### Step 4: Update Patches
- Review all patches in `target/linux/<platform>/patches-5.15/`
- Port patches to 6.6 or determine if obsolete
- Create `patches-6.6/` directory with ported patches
- See `openwrt-kernel-5.15-to-6.6-patch-migration-plan.md` for details

### Step 5: Test Thoroughly
- Build test with all common package combinations
- Boot test on representative hardware
- Run platform-specific test suites
- Validate all platform features

## Known Issues and Workarounds

### Issue 1: Rust Toolchain Requirement
**Problem:** If `CONFIG_RUST` is accidentally enabled, build fails without Rust toolchain.  
**Workaround:** Ensure `CONFIG_RUST is not set` in configs, or install Rust toolchain.

### Issue 2: Driver Compatibility
**Problem:** Some out-of-tree drivers may not compile with 6.6 APIs.  
**Workaround:** Port drivers using the API migration guide or temporarily disable.

### Issue 3: Performance Regression with Security Options
**Problem:** Memory zeroing options can cause 5-10% performance impact.  
**Workaround:** Disable for performance-critical deployments, enable for security-focused builds.

## References

- [Linux 6.6 Release Notes](https://kernelnewbies.org/Linux_6.6)
- [OpenWrt Kernel Build System Documentation](https://openwrt.org/docs/guide-developer/kernel)
- [Kernel Config Option Documentation](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html)
- Related CodeWiki Documents:
  - `linux-5.15-to-6.6-kernel-api-migration-guide.md`
  - `openwrt-kernel-5.15-to-6.6-patch-migration-plan.md`
  - `openwrt-kernel-5.15-config-audit-and-6.6-compatibility.md`

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-02-09 | CodeGen Agent | Initial build system migration documentation |

## Next Steps

1. **Calculate Kernel Hash:** Download kernel 6.6.68 and update hash in `include/kernel-6.6`
2. **Test Generic Config:** Build test with generic config on multiple architectures
3. **Platform Migration:** Begin platform-by-platform migration following guide above
4. **CI Integration:** Update CI/CD pipelines to test both 5.15 and 6.6
5. **Documentation:** Update user-facing documentation with kernel version info
