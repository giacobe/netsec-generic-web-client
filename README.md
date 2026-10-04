# Generic NetSec web client

Reproducible Buildroot 2025.02.15 profile, v86-compatible Linux 6.12.27 kernel, and example root filesystem overlay. NetSurf GTK2, X.org, Matchbox, automatic root console login and graphical startup, readiness markers. Address 10.0.0.20.

Clone this repository and https://github.com/giacobe/buildroot-builder-netsec on a Linux filesystem (WSL home directory is suitable; do not compile in OneDrive or /mnt/c). From the builder directory:

`scripts/01-setup-buildroot.sh`
`scripts/02-build-baseline.sh --config ../netsec-generic-web-client --name client`

Stage 02 includes the example overlay and writes a timestamped package beneath artifacts/ with images, final configuration, source revision, and SHA256 manifest. Client and server build their own copies of the compatible kernel; neither depends on a previously built server image.

To package changed payloads without rebuilding Buildroot:

`scripts/03-package-payload.sh --repo https://github.com/giacobe/netsec-generic-web-client.git --baseline artifacts/<client-timestamp> --output artifacts/client-updated --payload-subdir payload/rootfs-overlay --archive-dest / --permissions-file payload/permissions.txt --output-prefix client`

Stage 03 emits `client.bzImage` and `client.rootfs.cpio.gz`. For the platform rename these to `client-bzImage` and `client-rootfs.cpio.gz` and place them in netsec/web/images/. Changed files must use explicit permissions in payload/permissions.txt. Keep updated payloads in a separate repository and pass its URL to --repo for future exercises. Packaging only replaces/adds files; it cannot install packages absent from the baseline or delete old archive entries.

No generated kernel, filesystem, disk images, downloaded sources, or build directories are committed. Distribute image pairs and checksums separately. Boot-test new images in v86 before classroom distribution.
