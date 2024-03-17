# [Arch Linux](/ "Return to the main page")

  * [Home](/ "Arch news, packages, projects and more")
  * [Packages](/packages/ "Arch Package Database")
  * [Forums](https://bbs.archlinux.org/ "Community forums")
  * [Wiki](https://wiki.archlinux.org/ "Community documentation")
  * [GitLab](https://gitlab.archlinux.org/archlinux "GitLab")
  * [Security](https://security.archlinux.org/ "Arch Linux Security Tracker")
  * [AUR](https://aur.archlinux.org/ "Arch Linux User Repository")
  * [Download](/download/ "Get Arch Linux")

## A simple, lightweight distribution

You've reached the website for **Arch Linux** , a lightweight and flexible
Linux® distribution that tries to Keep It Simple.

Currently we have official packages optimized for the x86-64 architecture. We
complement our official package sets with a [ community-operated package
repository](https://aur.archlinux.org/ "Arch User Repository \(AUR\)") that
grows in size and quality each and every day.

Our strong community is diverse and helpful, and we pride ourselves on the
range of skillsets and uses for Arch that stem from it. Please check out our
[forums](https://bbs.archlinux.org/ "Arch Forums") and [mailing
lists](https://lists.archlinux.org/ "Arch Mailing Lists") to get your feet
wet. Also glance through our [wiki](https://wiki.archlinux.org/ "Arch Wiki")
if you want to learn more about Arch.

[Learn more...](/about/ "Learn more about Arch Linux")

###  [Latest News](/news/ "Browse the news archives")

[![RSS Feed](/static/rss.ca03bf98a65a.svg)](/feeds/news/ "Arch News RSS Feed")

####  [mkinitcpio hook migration and early microcode](/news/mkinitcpio-hook-
migration-and-early-microcode/ "View full article: mkinitcpio hook migration
and early microcode")

2024-03-04

With the release of [mkinitcpio
v38](https://lists.archlinux.org/hyperkitty/list/arch-
projects@lists.archlinux.org/thread/PZHWLVJLN5EPW6EVK2HEKVBDBNZWHREN/),
several hooks previously provided by Arch packages have been moved to the
mkinitcpio upstream project. The hooks are: systemd, udev, encrypt, sd-
encrypt, lvm2 and mdadm_udev.

To ensure no breakage of users' setup occurs, temporary conflicts have been
introduced into the respective packages to prevent installing packages that
are no longer compatible.

The following packages needs to be upgraded together:

  * mkinitcpio 38-3
  * systemd 255.4-2
  * lvm2 2.03.23-3
  * mdadm 4.3-2
  * cryptsetup 2.7.0-3

Please note that the `mkinitcpio` flag `--microcode`, and the `microcode`
option in the preset files, has been deprecated in favour of a new `microcode`
hook. This also allows you to drop the microcode `initrd` lines from your boot
configuration as they are now packed together with the main initramfs image.

####  [Making dbus-broker our default D-Bus daemon](/news/making-dbus-broker-
our-default-d-bus-daemon/ "View full article: Making dbus-broker our default
D-Bus daemon")

2024-01-09

We are making `dbus-broker` our default implementation of D-Bus, for improved
performance, reliability and integration with systemd.

For the foreseeable future we will still support the use of `dbus-daemon`, the
previous implementation. Pacman will ask you whether to install `dbus-broker-
units` or `dbus-daemon-units`. We recommend picking the default.

For a more detailed rationale, please see our [RFC
25](https://gitlab.archlinux.org/archlinux/rfcs/-/blob/master/rfcs/0025-dbus-
broker-default.rst).

####  [Bugtracker migration to GitLab completed](/news/bugtracker-migration-
to-gitlab-completed/ "View full article: Bugtracker migration to GitLab
completed")

2023-12-03

We are happy to announce that the [migration of the bugtracker to
GitLab](https://lists.archlinux.org/hyperkitty/list/arch-dev-
public@lists.archlinux.org/thread/WYXDTJ3TR2DWRQCDZK44BQDH67IDVGTS/) is done!
🥳

Thanks to everyone who has helped during the migration!

This means the issue tracker and merge requests on the GitLab package repos
are now enabled.

The old bugtracker will subsequently be closed down. For archiving reasons
there will be a static copy so that links (for example the randomly picked
[Task #56716](https://bugs.archlinux.org/task/56716)) are still stable,
migrated bugs have a closing comment pointing to the new URL on GitLab.

Packaging bugs are now opened on the repo hosting the corresponding packaging
sources, the "Add …

####  [Incoming changes in JDK / JRE 21 packages may require manual
intervention](/news/incoming-changes-in-jdk-jre-21-packages-may-require-
manual-intervention/ "View full article: Incoming changes in JDK / JRE 21
packages may require manual intervention")

2023-11-02

We are introducing a change in JDK/JRE packages of our distro. This is
triggered from the way a JRE is build in modern versions of Java (>9). We are
introducing this change in Java 21.

To sum it up instead of having JDK and JRE packages coexist in the same system
we will be making them conflict. The JDK variant package includes the runtime
environment to execute Java applications so if one needs compilation and
runtime of Java they need only the JDK package in the future. If, on the other
hand, they need just runtime of Java then JRE …

####  [Changes to default password hashing algorithm and umask
settings](/news/changes-to-default-password-hashing-algorithm-and-umask-
settings/ "View full article: Changes to default password hashing algorithm
and umask settings")

2023-09-22

With _shadow_ >= `4.14.0`, Arch Linux's default password hashing algorithm
changed from **SHA512** to [**yescrypt**](https://www.openwall.com/yescrypt/).

Furthermore, the [`umask`](https://man.archlinux.org/man/umask.1p) settings
are now configured in `/etc/login.defs` instead of `/etc/profile`.

This should not require any manual intervention.

## Reasons for Yescrypt

The password-based key derivation function (KDF) and password hashing scheme
**yescrypt** has been chosen due to its adoption (readily available in
_libxcrypt_ , which is used by [_pam_](https://wiki.archlinux.org/title/PAM))
and its stronger resilience towards password cracking attempts over
**SHA512**.

Although the winner of the [Password Hashing
Competition](https://www.password-hashing.net/) has been **argon2** , this
algorithm is not yet available in _libxcrypt …_

###  [Older News](/news/ "Browse the news archives")

2023-08-19

     [ansible-core >= 2.15.3-1 update may require manual intervention](/news/ansible-core-2153-1-update-may-require-manual-intervention/ "View full article: ansible-core >= 2.15.3-1 update may require manual intervention")
2023-08-11

     [budgie-desktop >= 10.7.2-6 update requires manual intervention](/news/budgie-desktop-1072-6-update-requires-manual-intervention/ "View full article: budgie-desktop >= 10.7.2-6 update requires manual intervention")
2023-06-18

     [TeX Live package reorganization](/news/tex-live-package-reorganization/ "View full article: TeX Live package reorganization")
2023-06-14

     [OpenBLAS >= 0.3.23-2 update requires manual intervention](/news/openblas-0323-2-update-requires-manual-intervention/ "View full article: OpenBLAS >= 0.3.23-2 update requires manual intervention")
2023-05-21

     [Git migration completed](/news/git-migration-completed/ "View full article: Git migration completed")
2023-05-15

     [Git migration announcement](/news/git-migration-announcement/ "View full article: Git migration announcement")
2023-02-12

     [Switch to the base-devel meta package requires manual intervention](/news/switch-to-the-base-devel-meta-package-requires-manual-intervention/ "View full article: Switch to the base-devel meta package requires manual intervention")
2023-01-13

     [PHP 8.2 update and introduction of legacy branch](/news/php-82-update-and-introduction-of-legacy-branch/ "View full article: PHP 8.2 update and introduction of legacy branch")
2023-01-12

     [In memory of Jonathon Fernyhough](/news/in-memory-of-jonathon-fernyhough/ "View full article: In memory of Jonathon Fernyhough")
2022-09-23

     [Removing python2 from the repositories](/news/removing-python2-from-the-repositories/ "View full article: Removing python2 from the repositories")

Package Search:

### Recent Updates ([more](/packages/?sort=-last_update "Browse all of the
latest packages"))

[![RSS Feed](/static/rss.ca03bf98a65a.svg)](/feeds/packages/ "Arch Package Updates RSS Feed") swell-foop 46.0-1 |  [x86_64](/packages/gnome-unstable/x86_64/swell-foop/ "Details for swell-foop \[gnome-unstable\]")  
---|---  
gnome-initial-setup 46.0-1 |  [x86_64](/packages/gnome-unstable/x86_64/gnome-initial-setup/ "Details for gnome-initial-setup \[gnome-unstable\]")  
lightsoff 46.0-1 |  [x86_64](/packages/gnome-unstable/x86_64/lightsoff/ "Details for lightsoff \[gnome-unstable\]")  
gnome-shell-extensions 46.0-1 |  [any](/packages/gnome-unstable/any/gnome-shell-extensions/ "Details for gnome-shell-extensions \[gnome-unstable\]")  
virtualbox-host-modules-arch 7.0.14-15 |  [x86_64](/packages/extra/x86_64/virtualbox-host-modules-arch/ "Details for virtualbox-host-modules-arch \[extra\]")  
vhba-module 20240202-9 |  [x86_64](/packages/extra/x86_64/vhba-module/ "Details for vhba-module \[extra\]")  
tp_smapi 0.44-43 |  [x86_64](/packages/extra/x86_64/tp_smapi/ "Details for tp_smapi \[extra\]")  
r8168 8.052.01-35 |  [x86_64](/packages/extra/x86_64/r8168/ "Details for r8168 \[extra\]")  
nvidia-open 550.54.14-7 |  [x86_64](/packages/extra/x86_64/nvidia-open/ "Details for nvidia-open \[extra\]")  
nvidia 550.54.14-7 |  [x86_64](/packages/extra/x86_64/nvidia/ "Details for nvidia \[extra\]")  
netfilter-fullconenat r73.0cf3b48-357 |  [x86_64](/packages/extra/x86_64/netfilter-fullconenat/ "Details for netfilter-fullconenat \[extra\]")  
linux 6.8.1.arch1-1 |  [x86_64](/packages/core/x86_64/linux/ "Details for linux \[core\]")  
linux-zen 6.8.1.zen1-1 |  [x86_64](/packages/extra/x86_64/linux-zen/ "Details for linux-zen \[extra\]")  
deepin-anything-arch 6.1.2-58 |  [x86_64](/packages/extra/x86_64/deepin-anything-arch/ "Details for deepin-anything-arch \[extra\]")  
broadcom-wl 6.30.223.271-536 |  [x86_64](/packages/extra/x86_64/broadcom-wl/ "Details for broadcom-wl \[extra\]")  
  
#### Documentation

  * [Wiki](https://wiki.archlinux.org/ "Community documentation")
  * [Manual Pages](https://man.archlinux.org/ "All manpages from Arch packages")
  * [Installation Guide](https://wiki.archlinux.org/title/Installation_guide "Installation guide")

#### Community

  * [Mailing Lists](https://lists.archlinux.org/ "Community and developer mailing lists")
  * [IRC Channels](https://wiki.archlinux.org/title/IRC_channels "Official and regional IRC communities")
  * [Planet Arch](https://planet.archlinux.org/ "Arch in the blogosphere")
  * [International Communities](https://wiki.archlinux.org/title/International_communities "Arch communities in your native language")

#### Support

  * [Donate](/donate/ "Help support Arch Linux")
  * [Products via Unixstickers](https://www.unixstickers.com/tag/archlinux "Arch
	Linux stickers, t-shirts, hoodies, mugs, posters and pins")
  * [T-shirts via Freewear](https://www.freewear.org/?page=list_items&org=Archlinux "T-shirts")
  * [T-shirts via HELLOTUX](https://www.hellotux.com/arch "T-shirts")

#### Tools

  * [Mirrorlist Updater](/mirrorlist/ "Get a custom mirrorlist from our database")
  * [Mirror List](/mirrors/ "See a listing of all available mirrors")
  * [Mirror Status](/mirrors/status/ "Check the status of all known mirrors")

#### Development

  * [Getting involved](https://wiki.archlinux.org/title/Getting_involved "Getting involved")
  * [Projects in Git](https://gitlab.archlinux.org/archlinux/ "Official Arch projects \(git\)")
  * [Developer Wiki](https://wiki.archlinux.org/title/DeveloperWiki "Developer Wiki articles")
  * [Package Groups](/groups/ "View the available package groups")
  * [Todo Lists](/todo/ "Developer Todo Lists")
  * [ISO Release List](/releng/releases/ "Release Engineering ISO listing")
  * [Visualizations](/visualize/ "View visualizations")
  * [Differences Reports](/packages/differences/ "See differences in packages between available architectures")

#### People

  * [Developers](/people/developers/ "More info about Developers")
  * [Package Maintainers](/people/package-maintainers/ "More info about Package Maintainers")
  * [Support Staff](/people/support-staff/ "More info about Support Staff")
  * [Developer Fellows](/people/developer-fellows/ "More info about Developer Fellows")
  * [Package Maintainer Fellows](/people/package-maintainer-fellows/ "More info about Package Maintainer Fellows")
  * [Support Staff Fellows](/people/support-staff-fellows/ "More info about Support Staff Fellows")
  * [Signing Master Keys](/master-keys/ "Package/Database signing master keys")

#### More Resources

  * [Press Coverage](https://wiki.archlinux.org/title/Arch_Linux_press_coverage "Arch Linux in the media")
  * [Logos & Artwork](/art/ "Arch logos and other artwork for promotional use")
  * [News Archives](/news/ "News Archives")
  * [RSS Feeds](/feeds/ "Various RSS Feeds")

[ ![Donate via Click&Pledge to Arch
Linux](/static/click_and_pledge.46105c057763.png)
](https://co.clickandpledge.com/Default.aspx?WID=47294)

[ ![Hetzner logo](/static/hetzner_logo.30fcfd907a4f.png)
](https://www.hetzner.com "Dedicated Root Server, VPS & Hosting - Hetzner
Online GmbH") [ ![Private Internet Access
logo](/static/pia_button.82a468ca1268.png)
](https://www.privateinternetaccess.com/ "Private Internet Access") [ ![Icons8
logo](/static/icons8_logo.91378e9a3b77.png) ](https://icons8.com/ "Icons8") [
![Shells logo](/static/shells_logo.a9dc284565e5.png) ](https://www.shells.com
"Shells.com")

Copyright © 2002-2024 [Judd Vinet](mailto:jvinet@zeroflux.org "Contact Judd
Vinet"), [Aaron Griffin](mailto:aaron@archlinux.org "Contact Aaron Griffin")
and [Levente Polyák](mailto:anthraxx@archlinux.org "Contact Levente Polyák").

The Arch Linux name and logo are recognized
[trademarks](https://terms.archlinux.org/docs/trademark-policy/ "Arch Linux
Trademark Policy"). Some rights reserved.

The registered trademark Linux® is used pursuant to a sublicense from LMI, the
exclusive licensee of Linus Torvalds, owner of the mark on a world-wide basis.

