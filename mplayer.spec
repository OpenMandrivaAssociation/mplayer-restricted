%define name		mplayer
%define Name		MPlayer
%define Summary		Movie player for linux
%define prerel		rc2
%define version 1.0
%define fversion %version%prerel
%define svn 0
%if %svn
%define rel		1.%prerel.0.%svn.1
%else 
%define rel 1.%prerel.5
%endif
%define release		%mkrel %rel

%define build_plf 0
%define build_optimization 0
%define build_debug 0
%define build_mencoder 1
%define build_gui 1

%define kernel_version	%(/bin/bash %{SOURCE5})
%define kver 		%(/bin/bash %{SOURCE5} | sed -e 's/-/./')
%define kvername	%(/bin/bash %{SOURCE5} | sed -e 's/-/./' | sed -e 's/mdk//')

%define build_live	1
%define build_vesa	1
%define build_theora	1
%define build_ggi	0
%define build_lirc	1
%define	build_xmms	0
%define build_amr	0
%define	build_arts	0
%define build_aa	1
%define build_cdda	1
%define build_compiz	0
%define build_dirac	0
%define build_dv	1
%define build_dvdread	0
%define build_dvdnav	1
%define build_sdl	1
%define build_lzo	1
%define build_smb	1
%define build_mga	1
%define build_fbdev	1
%define build_dvb	1
%define build_fribidi	1
%define build_enca	1
%define build_alsa	1
%define build_jack	1
%define build_openal	0
%define build_pulse	1
%define build_twolame 0
%define build_lame 0
%define build_faac 0
%define build_x264 0
%define build_xvid 0
%define build_dts 0
%define build_directfb 1
%define build_v4l2 1
%define build_xvmc 1

%if ! %build_dvdnav
%define build_dvdread 1
%endif

%if %mdkversion < 920
%define build_smb 0
%define build_jack 0
%endif

%if %mdkversion < 1000
%define build_openal 0
%define build_theora 0
%define build_directfb 0
%endif

%if %mdkversion < 1020
%define build_v4l2	0
%endif

%if %mdkversion < 200700
%define build_pulse	0
%endif

%if %mdkversion < 200800
%define build_dirac 0
%endif

%ifnarch %ix86
%define build_vesa 0
%endif

%{?!mkrel:%define mkrel(c:) %{-c:0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.*)(\\d+)$/;$rel=$2-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define realpath %{_libdir}/real
%define distsuffix plf
%define build_dvdread 0
%define build_amr 1
%define build_twolame 1
%define build_lame 1
%define build_faac 1
%define build_x264 1
%define build_xvid 1
%define build_dts 1
%else
%define realpath %{_libdir}/RealPlayer10GOLD/codecs
%endif

%{?_with_amr: %{expand: %%global build_amr 1}}
%{?_without_amr: %{expand: %%global build_amr 0}}
%{?_with_live: %{expand: %%global build_live 1}}
%{?_without_live: %{expand: %%global build_live 0}}
%{?_with_vesa: %{expand: %%global build_vesa 1}}
%{?_without_vesa: %{expand: %%global build_vesa 0}}
%{?_with_optimization: %{expand: %%global build_optimization 1}}
%{?_with_debug: %{expand: %%global build_debug 1}}
%{?_without_debug: %{expand: %%global build_debug 0}}
%{?_with_mencoder: %{expand: %%global build_mencoder 1}}
%{?_without_mencoder: %{expand: %%global build_mencoder 0}}
%{?_with_gui: %{expand: %%global build_gui 1}}
%{?_without_gui: %{expand: %%global build_gui 0}}
%{?_with_theora: %{expand: %%global build_theora 1}}
%{?_without_theora: %{expand: %%global build_theora 0}}
%{?_with_smb: %{expand: %%global build_smb 1}}
%{?_without_smb: %{expand: %%global build_smb 0}}
%{?_with_ggi: %{expand: %%global build_ggi 1}}
%{?_without_ggi: %{expand: %%global build_ggi 0}}
%{?_with_lirc: %{expand: %%global build_lirc 1}}
%{?_without_lirc: %{expand: %%global build_lirc 0}}
%{?_with_xmms: %{expand: %%global build_xmms 1}}
%{?_without_xmms: %{expand: %%global build_xmms 0}}
%{?_with_arts: %{expand: %%global build_arts 1}}
%{?_without_arts: %{expand: %%global build_arts 0}}
%{?_with_aa: %{expand: %%global build_aa 1}}
%{?_without_aa: %{expand: %%global build_aa 0}}
%{?_with_cdda: %{expand: %%global build_cdda 1}}
%{?_without_cdda: %{expand: %%global build_cdda 0}}
%{?_with_dirac: %{expand: %%global build_dirac 1}}
%{?_without_dirac: %{expand: %%global build_dirac 0}}
%{?_with_dv: %{expand: %%global build_dv 1}}
%{?_without_dv: %{expand: %%global build_dv 0}}
%{?_with_dvdread: %{expand: %%global build_dvdread 1}}
%{?_without_dvdread: %{expand: %%global build_dvdread 0}}
%{?_with_dvdnav: %{expand: %%global build_dvdnav 1}}
%{?_without_dvdnav: %{expand: %%global build_dvdnav 0}}
%{?_with_sdl: %{expand: %%global build_sdl 1}}
%{?_without_sdl: %{expand: %%global build_sdl 0}}
%{?_with_lzo: %{expand: %%global build_lzo 1}}
%{?_without_lzo: %{expand: %%global build_lzo 0}}
%{?_with_mga: %{expand: %%global build_mga 1}}
%{?_without_mga: %{expand: %%global build_mga 0}}
%{?_with_fribidi: %{expand: %%global build_fribidi 1}}
%{?_without_fribidi: %{expand: %%global build_fribidi 0}}
%{?_with_enca: %{expand: %%global build_enca 1}}
%{?_without_enca: %{expand: %%global build_enca 0}}
%{?_with_jack: %{expand: %%global build_jack 1}}
%{?_without_jack: %{expand: %%global build_jack 0}}
%{?_with_pulse: %{expand: %%global build_pulse 1}}
%{?_without_pulse: %{expand: %%global build_pulse 0}}
%{?_with_openal: %{expand: %%global build_openal 1}}
%{?_without_openal: %{expand: %%global build_openal 0}}
%{?_with_twolame: %{expand: %%global build_twolame 1}}
%{?_without_twolame: %{expand: %%global build_twolame 0}}
%{?_with_lame: %{expand: %%global build_lame 1}}
%{?_without_lame: %{expand: %%global build_lame 0}}
%{?_with_faac: %{expand: %%global build_faac 1}}
%{?_without_faac: %{expand: %%global build_faac 0}}
%{?_with_x264: %{expand: %%global build_x264 1}}
%{?_without_x264: %{expand: %%global build_x264 0}}
%{?_with_xvid: %{expand: %%global build_xvid 1}}
%{?_without_xvid: %{expand: %%global build_xvid 0}}
%{?_with_dts: %{expand: %%global build_dts 1}}
%{?_without_dts: %{expand: %%global build_dts 0}}
%{?_with_directfb: %{expand: %%global build_directfb 1}}
%{?_without_directfb: %{expand: %%global build_directfb 0}}
%{?_with_v4l2: %{expand: %%global build_v4l2 1}}
%{?_without_v4l2: %{expand: %%global build_v4l2 0}}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
%if %svn
Source0:	%{name}-%{svn}.tar.bz2
%else
Source0:	%{Name}-%{fversion}.tar.bz2
%endif
#gw default skin
Source4:	Blue-1.5.tar.bz2
Source5:	kernel-version.sh
Patch0:		mplayer-mdvconfig.patch
Patch1:		MPlayer-gnome-screensaver.patch
Patch3:		mplayer-mp3lib-no-strict-aliasing.patch
Patch7:		mplayer-1.0pre1-nomgafirst.patch
Patch12:	MPlayer-1.0rc2-desktopentry.patch
Patch19:	MPlayer-1.0pre8-CVE-2006-6172.patch
Patch20:	mplayer-1.0rc2-pulseaudio.patch
Patch21:	mplayer-1.0rc2-compiz.patch
URL:		http://www.mplayerhq.hu
License:	GPLv2
Group:		Video
%if %build_dvb && %mdkversion < 1000
BuildRequires:  kernel-source
%endif
BuildRequires:	libncurses-devel
%if %build_aa
BuildRequires:	libaa-devel
%endif
%if %build_arts
BuildRequires:  libarts-devel
%endif
%if %build_amr
BuildRequires:  libamrnb-devel
BuildRequires:  libamrwb-devel
%endif

%if %build_jack
BuildRequires:  libjack-devel
%endif
%if %build_pulse
BuildRequires:  libpulseaudio-devel
%endif
%if %build_openal
BuildRequires:  libopenal-devel
%endif
%if %build_cdda
BuildRequires:	libcdda-devel
%endif
%if %build_dirac
BuildRequires:	libdirac-devel >= 0.7.0
%endif
%if %build_dv
BuildRequires:	libdv-devel
%endif
BuildRequires:	libdxr3-devel
BuildRequires:	libesound-devel
BuildRequires:	libjpeg-devel
%if %build_lirc
BuildRequires:	liblirc-devel
%endif
%if %build_lzo
BuildRequires:	liblzo-devel
%endif
BuildRequires:  libmad-devel
BuildRequires:  libnas-devel
BuildRequires:	libpng-devel
%if %build_sdl
BuildRequires:	libSDL-devel >= 1.1.8
%endif
BuildRequires:	libtermcap-devel
%if %build_xmms
BuildRequires:  libxmms-devel
%endif
%if %build_ggi
BuildRequires:	libggiwmh-devel
%endif
%if %build_smb
BuildRequires:	libsmbclient-devel > 2.2.8a-7mdk 
%endif
%if %build_twolame
BuildRequires:	libtwolame-devel
%endif
%if %build_faac
BuildRequires:	libfaac-devel
%endif
%if %build_x264
BuildRequires:	libx264-devel
%endif
%if %build_xvid
BuildRequires:	xvid-devel >= 1.0.0-0.beta2.1plf
%endif
%if %build_dts
BuildRequires: dtsdec-devel
%endif
%if %build_lame
BuildRequires: liblame-devel
%endif
%if %build_dvdnav
BuildRequires:	libdvdnav-devel >= 4.1.1
%if %build_plf
Requires: %mklibname dvdcss 2
%endif
%endif
%if %build_dvdread
BuildRequires:	libdvdread-devel >= 0.9.4
%endif
%if %build_live
BuildRequires: live-devel
%endif
%if %build_vesa
BuildRequires: libvbe-devel liblrmi-devel
%endif
%if %build_theora
BuildRequires: libtheora-devel
%endif
%if %build_fribidi
BuildRequires: libfribidi-devel >= 0.10.4
%endif
%if %build_enca
BuildRequires: libenca-devel
%endif
%if %build_directfb
BuildRequires: libdirectfb-devel
%endif
%if %mdkversion >= 200700
BuildRequires: libxvmc-devel
BuildRequires: libmesagl-devel
BuildRequires: libxxf86vm-devel
BuildRequires: libxxf86dga-devel
%endif
BuildRequires: libspeex-devel
BuildRequires: libmpcdec-devel
BuildRequires: ladspa-devel
BuildRequires: libxslt-proc
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtd412-xml
BuildRequires: libcaca-devel
BuildRequires: ungif-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides:	mplayer1.0
Obsoletes:	mplayer1.0


%description
MPlayer is a movie player for LINUX (runs on many other Unices, and
non-x86 CPUs, see the documentation). It plays most MPEG, VOB, AVI,
VIVO, ASF/WMV, QT/MOV, FLI, NuppelVideo, yuv4mpeg, FILM, RoQ, and some
RealMedia files, supported by many native, XAnim, and Win32 DLL codecs.
You can watch VideoCD, SVCD, DVD, 3ivx, FLI, and even DivX movies too
(and you don't need the avifile library at all!). The another big
feature of mplayer is the wide range of supported output drivers. It
works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, but you can use
SDL (and this way all drivers of SDL), VESA (on every VESA compatible
card, even without X!), and some lowlevel card-specific drivers (for
Matrox, 3Dfx and Radeon) too! Most of them supports software or hardware
scaling, so you can enjoy movies in fullscreen. MPlayer supports
displaying through some hardware MPEG decoder boards, such as the DVB
and DXR3/Hollywood+! And what about the nice big antialiased shaded
subtitles (9 supported types!!!) with european/ISO 8859-1,2 (hungarian,
english, czech, etc), cyrillic, korean fonts, and OSD?

%if ! %build_plf
Note: If you want to play Real content, you need to have the content
of RealPlayer's Codecs directory in %realpath
%else
This package is in PLF because some included codecs are covered by
patents.  It also includes support for reading DVDs encrypted with CSS
which might be illegal in some countries.

For non-free binary codecs support you should install the packages
win32-codecs, real-codecs and xanim-codecs.
%endif

%package doc
Summary: %{Name} documentation
Group: Books/Computer books

%description doc
This package contains documentation for %{Name}.

%if %build_gui
%package gui
Summary:	GUI for %{name}
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	gtk+2-devel
BuildRequires:	ImageMagick
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: soundwrapper
Provides:	mplayer1.0-gui
Obsoletes:	mplayer1.0-gui
Conflicts:	mplayer-skins < 1.3-8mdk

%description gui
This package contains a GUI for %{name}.
%endif

%if %build_mencoder
%package -n mencoder
Summary: MPlayer's movie encoder
Group:		Video
Requires:	%{name} = %version
Provides:	mencoder1.0
Obsoletes:	mencoder1.0

%description -n mencoder
MEncoder a movie encoder and is a part of the MPlayer package.
%if !%build_plf
Note: this version doesn't have support for encoding mp3 audio streams in the
video files. 
%else
This PLF build has additional support for AAC decoding with libfaad
and MP3 encoding with lame, both are covered by software patents. It
also includes support for reading DVDs encrypted with CSS which might
be illegal in some countries.
%endif
%endif


%prep
rm -rf $RPM_BUILD_ROOT

%if %svn
%setup -q -n %name -a 4
%else
%setup -q -n MPlayer-%{version}%{prerel} -a 4
%endif
#gw fix permissions
find DOCS -type d|xargs chmod 755
find DOCS -type f|xargs chmod 644
find DOCS -name .svn|xargs rm -rf
chmod 644 AUTHORS Changelog README Copyright
rm -f Blue/README
%patch0 -p1 -b .mdv
%patch1 -p0 -b .gnome-screensaver
%patch3 -p1 -b .mp2
%patch7 -p1 -b .mga
%patch12 -p1 -b .desktopentry
cd stream
%patch19 -p2 -b .cve-2006-6172
cd ..
%patch20 -p0 -b .pulse
%patch21 -p0 -b .compiz

perl -pi -e "s^%fversion^%version-%release^" version.sh

mv DOCS/README README.DOCS

%build
%if !%build_optimization
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
%endif
%if %build_debug
export CFLAGS="$CFLAGS -g"
%endif
%ifarch ppc
export CFLAGS="$CFLAGS -mcpu=7450 -maltivec"
%endif
export CPPFLAGS="-I%_includedir/directfb"
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}/%{name} \
	--confdir=%{_sysconfdir}/%{name} \
	--libdir=%_libdir \
	--enable-largefiles \
%if !%build_optimization
%ifnarch x86_64
	--enable-runtime-cpudetection \
%endif
%ifarch %ix86
        --enable-mmx \
        --enable-3dnow \
        --enable-sse \
        --enable-sse2 \
        --enable-fastmemcpy \
%endif
%endif
	--enable-freetype \
	--enable-nas \
%if %build_debug
	--enable-debug=3 \
%else
	--disable-sighandler \
%endif
%if %build_gui
	--enable-gui \
%endif
	--language=all \
	\
%if !%build_plf
	--disable-faad-internal \
%endif
%if %build_dvdnav
        --enable-dvdnav \
%else
        --disable-dvdnav \
%endif
%if %build_dvdread || ! %build_plf
	--disable-libdvdcss-internal \
%endif
%if %build_lirc
	--enable-lirc \
%else
	--disable-lirc \
%endif
	--enable-tv \
%if ! %build_v4l2
	--disable-tv-v4l2 \
%endif
	--enable-joystick \
	\
	--enable-gl \
        --disable-svga \
%if ! %build_mga
	--disable-mga \
%endif
%if ! %build_fbdev
	--disable-fbdev \
%endif
%if %build_directfb
       --enable-directfb \
%else
       --disable-directfb \
%endif
%if %build_mencoder
	--enable-mencoder \
%else
	--disable-mencoder \
%endif
%if ! %build_live
	--disable-live \
%endif
%if ! %build_vesa
       --disable-vesa \
%endif
%if %build_theora
	--enable-theora \
%else
	--disable-theora \
%endif
	--enable-menu \
%if %build_xmms
	--enable-xmms --with-xmmslibdir=%{_libdir} \
%endif
%if %build_smb
	--enable-smb \
%endif
%if %build_dvb
%if %mdkversion < 1000
	--with-dvbincdir=/usr/src/linux/3rdparty/mod_dvb/include \
%endif
%else
       --disable-dvb \
       --disable-dvbhead \
%endif
	--xanimcodecsdir=%{_prefix}/X11R6/lib/xanim/mods \
	--realcodecsdir=%{realpath} \
%if ! %build_ggi
	--disable-ggi \
%endif
%ifarch %ix86
	\
	--win32codecsdir=%{_prefix}/lib/win32 \
%endif
%if ! %build_arts
	--disable-arts \
%endif
%if ! %build_jack
	--disable-jack \
%endif
%if ! %build_aa
	--disable-aa \
%endif
%if ! %build_cdda
	--disable-cdparanoia \
%endif
%if ! %build_dv
	--disable-libdv \
%endif
%if ! %build_lzo
	--disable-liblzo \
%else
	--with-extraincdir=%_includedir/lzo \
%endif
%if ! %build_sdl
	--disable-sdl \
%endif
%if ! %build_alsa
	--disable-alsa \
%endif
%if %build_fribidi
	--enable-fribidi \
%endif
%if !%build_enca
	--disable-enca \
%endif
%if %build_pulse
	--enable-pulse \
%endif
%if !%build_openal
	--disable-openal \
%endif
	--enable-zr \
%if %build_xvmc
	--enable-xvmc \
%endif



# Keep this line before empty end %%configure (ppc conditionnal pb)
%if %mdkversion == 1000 && %build_optimization
make CC=gcc" -fno-unit-at-a-time"
%else
make
%endif

# build HTML docs
(cd DOCS/xml && make)

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%name
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%name
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/{de,fr,hu,pl,es,zh_CN,""}/man1
install -m 755 mplayer $RPM_BUILD_ROOT%{_bindir}
install -m 644 DOCS/man/en/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 DOCS/man/de/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/de/man1/mplayer.1
install -m 644 DOCS/man/fr/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1/mplayer.1
install -m 644 DOCS/man/hu/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1/mplayer.1
install -m 644 DOCS/man/pl/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1/mplayer.1
install -m 644 DOCS/man/zh/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1/mplayer.1
install -m 644 DOCS/man/es/mplayer.1 $RPM_BUILD_ROOT%{_mandir}/es/man1/mplayer.1

 
%if %build_mencoder
install -m 755 mencoder $RPM_BUILD_ROOT%{_bindir}
for man_dir in $RPM_BUILD_ROOT%{_mandir}/{de,fr,hu,pl,es,zh_CN,""}/man1; do
(cd $man_dir && ln -s mplayer.1 mencoder.1)
done
install -m 755 TOOLS/mencvcd TOOLS/divx2svcd TOOLS/wma2ogg.pl TOOLS/midentify %buildroot%_bindir
%endif
install -m 644 etc/example.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/mplayer.conf
install -m 644 etc/menu.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%if %build_gui
# default Skin
install -d -m 755 %buildroot%_datadir/%name/Skin/
cp -r Blue %buildroot%_datadir/%name/Skin/
ln -s Blue %buildroot%_datadir/%name/Skin/default
# gmplayer equals mplayer -gui
(cd $RPM_BUILD_ROOT%{_bindir} && ln -s mplayer gmplayer)
# icons
mkdir -p $RPM_BUILD_ROOT{%_liconsdir,%_iconsdir,%{_miconsdir}}
convert -transparent white Blue/icons/icon48x48.png $RPM_BUILD_ROOT%{_liconsdir}/gmplayer.png 
convert -transparent white Blue/icons/icon32x32.png $RPM_BUILD_ROOT%{_iconsdir}/gmplayer.png 
convert -transparent white -scale 16x16 Blue/icons/icon48x48.png $RPM_BUILD_ROOT%{_miconsdir}/gmplayer.png
install -D -m 644 etc/mplayer.desktop %buildroot%_datadir/applications/mplayer.desktop
%endif

%if %build_debug
export DONT_STRIP=1
%endif
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %build_gui
%pre gui
if [ -d %_datadir/%name/Skin/default ]
  then rm -rf %_datadir/%name/Skin/default
fi
%post gui
%{update_menus}
%update_desktop_database

%postun gui
%{clean_menus}
%clean_desktop_database
%endif


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changelog README Copyright
%dir %{_sysconfdir}/%name
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/mplayer.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/menu.conf
%{_bindir}/midentify
%{_bindir}/mplayer
%{_mandir}/man1/mplayer.1*
%lang(de) %{_mandir}/de/man1/mplayer.1*
%lang(fr) %{_mandir}/fr/man1/mplayer.1*
%lang(hu) %{_mandir}/hu/man1/mplayer.1*
%lang(pl) %{_mandir}/pl/man1/mplayer.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mplayer.1*
%lang(es) %{_mandir}/es/man1/mplayer.1*
%dir %{_datadir}/%{name}

%files doc
%defattr(-,root,root)
%doc README.DOCS
%doc DOCS/default.css DOCS/HTML DOCS/tech/
%if %build_mencoder
%files -n mencoder
%defattr(-,root,root)
%{_bindir}/mencoder
%{_bindir}/divx2svcd
%{_bindir}/mencvcd
%{_bindir}/wma2ogg.pl
%{_mandir}/man1/mencoder.1*
%lang(de) %{_mandir}/de/man1/mencoder.1*
%lang(fr) %{_mandir}/fr/man1/mencoder.1*
%lang(hu) %{_mandir}/hu/man1/mencoder.1*
%lang(pl) %{_mandir}/pl/man1/mencoder.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/mencoder.1*
%lang(es) %{_mandir}/es/man1/mencoder.1*
%endif

%if %build_gui
%files gui
%defattr(-,root,root)
%{_bindir}/gmplayer
%_datadir/applications/mplayer.desktop
%_datadir/%name/Skin/
%{_iconsdir}/gmplayer.png
%{_miconsdir}/gmplayer.png
%{_liconsdir}/gmplayer.png
%endif


