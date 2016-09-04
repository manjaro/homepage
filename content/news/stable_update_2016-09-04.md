+++
author = "Philip Müller"
date = "2016-09-04T23:51:14+02:00"
forumdiscussion = ""
tags = []
title = "[Stable Update] 2016-09-04 - MATE, Calamares, Pamac, Deepin"
type = "news-post"

+++

Hi community,

Manjaro Ellada seems to be a great release. We also managed to release some of our community editions already. Bernhard is now working on our Deepin edition. Therefore he updated some of the Deepin packages. Additionally he fixed some issue with our realtime kernel. To round-up this package set, I managed to update some of the MATE packages to their latest release and Pamac. We now support a tray-icon for the KDE desktop. Please install it separately.

With the first point-release of Calamares v2.4 some issues got fixed:

* fixed how the timezone setting is applied, so certain environments like KDE Plasma always obey the setting on first boot
* fixed timezone selector behavior, so that a timezone changes affect the live system immediately
* improved partition scanner code so it always excludes ISO9660 volumes (to avoid showing the live USB stick or optical disk in the devices list)
* future-proofed and optimized the codebase a bit to remove the soon to be deprecated Q_FOREACH construct and avoid deep copies of Qt containers

The first two, we already added to our original package of Calamares. If needed, please update Calamares before you try to install Manjaro Ellada in live-session.

Archlinux upstream fixes are still from: Mon Aug 29 19:34:28 CEST 2016.

Please report any issues you may have with this update. Also read our **troubleshoots** to avoid known issues.

Kind regards,
Philip Müller and the Manjaro Development Team
