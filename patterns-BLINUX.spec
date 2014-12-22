#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:           patterns-BLINUX
Version:        2.0
Release:        15
Summary:        Meta package for pattern base
Group:          Metapackages
License:        BSD-2-Clause
Url:            http://www.blinux.fr
BuildRequires:  patterns
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Provides:       patterns-BLINUX-basesystem
Requires:	BLINUX-release
Requires:	ImageMagick
Requires:	MozillaFirefox
Requires:	MozillaFirefox-branding-upstream
Requires:	aaa_base
Requires:	acl
Requires:	acpica
Requires:	adjtimex
Requires:	alsa
Requires:	alsa-oss
Requires:	alsa-plugins
Requires:	alsa-plugins-pulse
Requires:	alsa-tools
Requires:	alsa-tools-gui
Requires:	alsa-utils
Requires:	alsamixergui
Requires:	apache2
Requires:	apache2-mod_php5
Requires:	attr
Requires:	autofs
Requires:	bc
Requires:	bind-utils
Requires:	branding-BLINUX
Requires:	bzip2
Requires:	camarchepas
Requires:	chromium
Requires:	chromium-desktop-gnome
Requires:	curl
Requires:	dejavu
Requires:	deltarpm
Requires:	dhcpcd
Requires:	diffutils
Requires:	dmidecode
Requires:	dmraid
Requires:	dos2unix
Requires:	dosfstools
Requires:	droid-fonts
Requires:	e2fsprogs
Requires:	ed
Requires:	efont-unicode
Requires:	emacs
Requires:	ethtool
Requires:	evince
Requires:	file
Requires:	fillup
Requires:	findutils
Requires:	flash-player
Requires:	flash-player-gnome
Requires:	gawk
Requires:	ghostscript-fonts-other
Requires:	ghostscript-fonts-std
Requires:	ghostscript-x11
Requires:	glibc-32bit
Requires:	glibc-locale
Requires:	glibc-locale-32bit
Requires:	gnome-screensaver
Requires:	gpart
Requires:	gpg2
Requires:	gpicview
Requires:	gpm
Requires:	groff
Requires:	hdparm
Requires:	hwinfo
Requires:	icewm
Requires:	ifnteuro
Requires:	ifplugd
Requires:	iftop
Requires:	info
Requires:	intlfnts
Requires:	iproute2
Requires:	iputils
Requires:	irqbalance
Requires:	kbd
Requires:	kernel
Requires:	klogd
Requires:	kpartx
Requires:	ksh
Requires:	less
Requires:	libQtWebKit4-32bit
Requires:	libX11-6-32bit
Requires:	libXss1-32bit
Requires:	libXv1-32bit
Requires:	libasound2-32bit
Requires:	libatm1
Requires:	liberation-fonts
Requires:	libpng12-0
Requires:	libpng12-0-32bit
Requires:	libqt4-32bit
Requires:	lightdm
Requires:	linux32
Requires:	lsb-release
Requires:	lsof
Requires:	lsscsi
Requires:	man
Requires:	man-pages
Requires:	man-pages-posix
Requires:	master-boot-code
Requires:	mcelog
Requires:	mkinitrd
Requires:	module-init-tools
Requires:	mtr
Requires:	ncurses-utils
Requires:	netcat-openbsd
Requires:	netcfg
Requires:	network-config-BLINUX
Requires:	nmap
Requires:	ns_auth
Requires:	ntp
Requires:	numactl
Requires:	numlockx
Requires:	openssh
Requires:	openssh-askpass
Requires:	orca
Requires:	p7zip
Requires:	pax
Requires:	pdftk
Requires:	perl-base
Requires:	pm-utils
Requires:	polkit
Requires:	polkit-default-privs
Requires:	procinfo
Requires:	procps
Requires:	providers
Requires:	pulseaudio
Requires:	pulseaudio-module-x11
Requires:	pulseaudio-utils
Requires:	pwdutils
Requires:	python3
Requires:	repo-BLINUX
Requires:	rpcbind
Requires:	rpm
Requires:	rsync
Requires:	sash
Requires:	sbin_init
Requires:	setserial
Requires:	sharutils
Requires:	shim
Requires:	strace
Requires:	suspend
Requires:	sysconfig
Requires:	sysconfig-cli
Requires:	systemd-presets-branding-BLINUX
Requires:	systemd-sysvinit
Requires:	tar
Requires:	tcpdump
Requires:	tcsh
Requires:	telnet
Requires:	terminfo
Requires:	time
Requires:	timezone
Requires:	totem
Requires:	translation-update
Requires:	udev
Requires:	util-linux
Requires:	vgaswitcheroo
Requires:	vim
Requires:	vlan
Requires:	w3m
Requires:	wget
Requires:	which
Requires:	whois
Requires:	wireless-tools
Requires:	wol
Requires:	wpa_supplicant
Requires:	wpa_supplicant-gui
Requires:	x11-tools
Requires:	xdmbgrd
Requires:	xkeyboard-config
Requires:	xlockmore
Requires:	xorg-config-BLINUX
Requires:	xorg-x11-Xvnc
Requires:	xorg-x11-driver-input
Requires:	xorg-x11-driver-video
Requires:	xorg-x11-essentials
Requires:	xorg-x11-fonts
Requires:	xorg-x11-fonts-core
Requires:	xorg-x11-libX11-ccache
Requires:	xorg-x11-libs
Requires:	xorg-x11-server
Requires:	xorg-x11-xauth
Requires:	xscreensaver-data
Requires:	xscreensaver-data-extra
Requires:	xterm
Requires:	xtermset
Requires:	zisofs-tools
Requires:	zsh
Requires:       xscreensaver

Conflicts:	gdm

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

%prep

%build

%install

%files
