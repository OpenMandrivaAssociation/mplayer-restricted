%define oname	MPlayer
%define prerel	%{nil}
%define svn	%{nil}
%if "%svn" != ""
%define fversion %{svn}
%else
%define fversion %{version}
%endif
%if "%{prerel}" != ""
%if "%{svn}" != ""
%define rel	1.%{prerel}.0.%{svn}.1
%else 
%define rel 0.%{prerel}.1
%endif
%else
%if "%{svn}" != ""
%define rel 0.%{svn}.1
%else
%define rel 3
%endif
%endif

%define build_plf	0
%define build_debug	0
%define build_mencoder	1
%define build_gui	1
%define build_system_ffmpeg	1

%define kernel_version	%(/bin/bash %{SOURCE5})
%define kver 		%(/bin/bash %{SOURCE5} | sed -e 's/-/./')
%define kvername	%(/bin/bash %{SOURCE5} | sed -e 's/-/./' | sed -e 's/mdk//')

%define build_yasm	1
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
%define build_dirac	1
%define build_dv	1
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
%define build_schroedinger	1
%define build_twolame	0
%define build_lame	0
%define build_faac	0
%define build_faad	0
%define build_x264	0
%define build_xvid	0
%define build_dts	0
%define build_directfb	1
%define build_v4l2	1
%define build_xvmc	1
%define build_vdpau	1
%define build_ivtv	0
%define build_libass	1
%define build_vpx	1
%define build_rtmp	1

%define build_smb	0

%ifnarch %{ix86}
%define build_vesa	0
%endif

%{?_with_plf:	%{expand:	%%global build_plf 1}}

#####################
# Hardcode PLF build
%define build_plf 0
#####################

%if %{build_plf}
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define build_amr	1
%define build_twolame	1
%define build_lame	1
%define build_faac	1
%define build_faad	1
%define build_x264	1
%define build_xvid	1
%define build_dts	1
%define build_yasm	1
%define build_dirac	1
%define build_schroedinger	1
%endif

%if %{build_system_ffmpeg} && ! %{build_plf}
%define build_amr 0
%define build_dirac 0
%define build_schroedinger 0
%define build_vpx 0
%define build_zr 0
%endif

%{?_with_amr: %{expand: %%global build_amr 1}}
%{?_without_amr: %{expand: %%global build_amr 0}}
%{?_with_live: %{expand: %%global build_live 1}}
%{?_without_live: %{expand: %%global build_live 0}}
%{?_with_yasm: %{expand: %%global build_yasm 1}}
%{?_without_yasm: %{expand: %%global build_yasm 0}}
%{?_with_vesa: %{expand: %%global build_vesa 1}}
%{?_without_vesa: %{expand: %%global build_vesa 0}}
%{?_with_debug: %{expand: %%global build_debug 1}}
%{?_without_debug: %{expand: %%global build_debug 0}}
%{?_with_mencoder: %{expand: %%global build_mencoder 1}}
%{?_without_mencoder: %{expand: %%global build_mencoder 0}}
%{?_with_gui: %{expand: %%global build_gui 1}}
%{?_without_gui: %{expand: %%global build_gui 0}}
%{?_with_system_ffmpeg: %{expand: %%global build_system_ffmpeg 1}}
%{?_without_system_ffmpeg: %{expand: %%global build_system_ffmpeg 0}}
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
%{?_with_libass: %{expand: %%global build_libass 1}}
%{?_without_libass: %{expand: %%global build_libass 0}}
%{?_with_pulse: %{expand: %%global build_pulse 1}}
%{?_without_pulse: %{expand: %%global build_pulse 0}}
%{?_with_openal: %{expand: %%global build_openal 1}}
%{?_without_openal: %{expand: %%global build_openal 0}}
%{?_with_schroedinger: %{expand: %%global build_schroedinger 1}}
%{?_without_schroedinger: %{expand: %%global build_schroedinger 0}}
%{?_with_twolame: %{expand: %%global build_twolame 1}}
%{?_without_twolame: %{expand: %%global build_twolame 0}}
%{?_with_lame: %{expand: %%global build_lame 1}}
%{?_without_lame: %{expand: %%global build_lame 0}}
%{?_with_faac: %{expand: %%global build_faac 1}}
%{?_without_faac: %{expand: %%global build_faac 0}}
%{?_with_faad: %{expand: %%global build_faad 1}}
%{?_without_faad: %{expand: %%global build_faad 0}}
%{?_with_x264: %{expand: %%global build_x264 1}}
%{?_without_x264: %{expand: %%global build_x264 0}}
%{?_with_xvid: %{expand: %%global build_xvid 1}}
%{?_without_xvid: %{expand: %%global build_xvid 0}}
%{?_with_dts: %{expand: %%global build_dts 1}}
%{?_without_dts: %{expand: %%global build_dts 0}}
%{?_with_directfb: %{expand: %%global build_directfb 1}}
%{?_without_directfb: %{expand: %%global build_directfb 0}}
%{?_with_rtmp: %{expand: %%global build_rtmp 1}}
%{?_without_rtmp: %{expand: %%global build_rtmp 0}}
%{?_with_v4l2: %{expand: %%global build_v4l2 1}}
%{?_without_v4l2: %{expand: %%global build_v4l2 0}}
%{?_with_xvmc: %{expand: %%global build_xvmc 1}}
%{?_without_xvmc: %{expand: %%global build_xvmc 0}}
%{?_with_vdpau: %{expand: %%global build_vdpau 1}}
%{?_without_vdpau: %{expand: %%global build_vdpau 0}}
%{?_with_vpx: %{expand: %%global build_vpx 1}}
%{?_without_vpx: %{expand: %%global build_vpx 0}}
%ifnarch %arm %mips aarch64
%bcond_without	cpudetection
%endif

Summary:	Movie player for linux
Name:		mplayer
Version:	1.1.1
Release:	%{rel}%{?extrarelsuffix}
License:	GPLv2
Group:		Video
Url:		http://www.mplayerhq.hu
%if "%svn" != ""
#gw generated using svn export
Source0:	%{name}-%{svn}.tar.xz
%else
Source0:	ftp://ftp1.mplayerhq.hu/MPlayer/releases/%{oname}-%{fversion}.tar.xz
%endif
#gw default skin
Source4:	Blue-1.8.tar.bz2
Source5:	kernel-version.sh
Patch0:	mplayer-mdvconfig.patch
# fixes for crashes found while fixing CVE-2008-1558
Patch28:	mplayer-rtsp-extra-fixes.patch
Patch31:	mplayer-format-string-literal.patch
#gw HAVE_DLFCN_H isn't defined
Patch33:	mplayer-have-dlfcn_h.patch
#gw fix crash:	https://qa.mandriva.com/show_bug.cgi?id=55443
Patch35:	mplayer-fix-dvd-crash.patch
Patch39:	mplayer-dlopen-libfaac-libfaad-and-libx264.patch
Patch40:	mplayer-r34578-local-copy-of-internal-ffmpeg-type-definition.patch
Patch42:	mplayer-filters-hack-with-shared.patch
Patch43:	mplayer-r34911-dont-use-ffmpeg-functionality-outside-stable-release.patch
Patch44:	mplayer-mp_taglists-declaration.patch

BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd412-xml
BuildRequires:	xsltproc
BuildRequires:	bzip2-devel
BuildRequires:	giflib-devel
BuildRequires:	gsm-devel
BuildRequires:	jpeg-devel
BuildRequires:	ladspa-devel
BuildRequires:	libdxr3-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	mng-devel
BuildRequires:	nas-devel
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(dvdnavmini)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xscrnsaver)
%if %{build_aa}
BuildRequires:	aalib-devel
%endif
BuildRequires:	a52dec-devel
%if %{build_arts}
BuildRequires:	arts-devel
%endif
%if %{build_amr}
BuildRequires:	pkgconfig(opencore-amrnb)
BuildRequires:	pkgconfig(opencore-amrwb)
%endif
%if %{build_jack}
BuildRequires:	pkgconfig(jack)
%endif
%if %{build_pulse}
BuildRequires:	pkgconfig(libpulse)
%endif
%if %{build_openal}
BuildRequires:	pkgconfig(openal)
%endif
%if %{build_cdda}
BuildRequires:	cdda-devel
%endif
%if %{build_dirac}
BuildRequires:	pkgconfig(dirac)  >= 0.9.0
%endif
%if %{build_schroedinger}
BuildRequires:	pkgconfig(schroedinger-1.0)
%endif
%if %{build_dv}
BuildRequires:	pkgconfig(libdv)
%endif
%if %{build_lirc}
BuildRequires:	pkgconfig(liblircclient0)
%endif
%if %{build_lzo}
BuildRequires:	liblzo-devel
%endif
%if %{build_sdl}
BuildRequires:	pkgconfig(sdl) >= 1.1.8
%endif
%if %{build_xmms}
BuildRequires:	xmms-devel
%endif
%if %{build_ggi}
BuildRequires:	libggiwmh-devel
%endif
%if %{build_smb}
BuildRequires:	pkgconfig(smbclient)
%endif
%if %{build_twolame}
BuildRequires:	pkgconfig(twolame)
%endif
%if %{build_faac}
BuildRequires:	libfaac-devel
%endif
%if %{build_faad}
BuildRequires:	libfaad2-devel
%endif
%if %{build_x264}
BuildRequires:	pkgconfig(x264) >= 0.120
%endif
%if %{build_xvid}
BuildRequires:	xvid-devel
%endif
%if %{build_dts}
BuildRequires:	pkgconfig(libdts)
%endif
%if %{build_lame}
BuildRequires:	lame-devel
%endif
%if %{build_live}
BuildRequires:	live-devel
%endif
%if %{build_vesa}
BuildRequires:	libvbe-devel
BuildRequires:	liblrmi-devel
%endif
%if %{build_theora}
BuildRequires:	pkgconfig(theora)
%endif
%if %{build_fribidi}
BuildRequires:	pkgconfig(fribidi) >= 0.10.4
%endif
%if %{build_enca}
BuildRequires:	pkgconfig(enca)
%endif
%if %{build_directfb}
BuildRequires:	pkgconfig(directfb)
%endif
%if %{build_xvmc}
BuildRequires:	pkgconfig(xvmc)
%endif
%if %{build_vdpau}
BuildRequires:	pkgconfig(vdpau)
%endif
%if %{build_libass}
BuildRequires:	pkgconfig(libass)
%endif
%if %{build_vpx}
BuildRequires:	pkgconfig(vpx)
%endif
%if %{build_rtmp}
BuildRequires:	pkgconfig(librtmp)
%endif
%if %{build_yasm}
BuildRequires:	yasm
%endif
%if %{build_system_ffmpeg}
BuildRequires:	ffmpeg-devel
%endif

%if "%{_lib}" == "lib64"
%global	_ext	()(64bit)
%else
%global	_ext	%{nil}
%endif

# With plf build they are auto-required
%if ! %{build_plf}
Suggests:	libfaac.so.0%{_ext}
Suggests:	libfaad.so.2%{_ext}
Suggests:	libx264.so.120%{_ext}
Suggests:	libopencore-amrnb.so.0%{_ext}
Suggests:	libopencore-amrwb.so.0%{_ext}
Suggests:	libtwolame.so.0%{_ext}
Suggests:	libdca.so.0%{_ext}
Suggests:	libdvdcss.so.2%{_ext}
%endif

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

Note: If you want to play Real content, you need to have the content
of RealPlayer's Codecs directory in %{_libdir}/codecs/

%if %{build_plf}
This package is in restricted because some included codecs are covered 
by patents. It also includes support for reading DVDs encrypted with 
CSS which might be illegal in some countries.

For non-free binary codecs support you should install the packages
win32-codecs, real-codecs and xanim-codecs.
%endif

%package doc
Summary:	%{oname} documentation
Group:		Books/Computer books
BuildArch:	noarch

%description doc
This package contains documentation for %{oname}.

%if %{build_gui}
%package gui
Summary:	GUI for %{name}
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	imagemagick
Requires:	soundwrapper

%description gui
This package contains a GUI for %{name}.
%endif

%if %{build_mencoder}
%package -n mencoder
Summary:	MPlayer's movie encoder
Group:		Video
Requires:	%{name}

%description -n mencoder
MEncoder a movie encoder and is a part of the MPlayer package.
%if ! %{build_plf}
Note: this version does not have support for encoding mp3 audio streams in the
video files.
%else
This restricted build has additional support for AAC decoding with libfaad
and MP3 encoding with lame, both are covered by software patents. It
also includes support for reading DVDs encrypted with CSS which might
be illegal in some countries.
%endif
%endif

%prep
%if "%{svn}" != ""
%setup -q -n %{name} -a 4
%else
%setup -q -n MPlayer-%{version}%{prerel} -a 4
%endif
#gw as we have have used svn export:
echo %{svn}|sed s/^r// > snapshot_version
find DOCS -name .svn|xargs rm -rf
#gw fix permissions
chmod 644 AUTHORS Changelog README Copyright
rm -f Blue/README
%patch0 -p1 -b .mdv~
%patch28 -p1 -b .rtsp-extra-fixes
%patch31 -p1 -b .format~
%patch33 -p1 -b .dlfcn~
%patch35 -p0
%if ! %{build_plf}
%patch39 -p1 -b .dlopen~
%endif
rm -rf ffmpeg
%patch40 -p1 -b .ffmpeg~
%patch42 -p1 -b .internal_filters~
%patch43 -p1 -b .ffm_stable~
%patch44 -p0 -b .mp_taglists~

# Sometimes (1.1.1) mplayer guys forget to update the VERSION file...
# Let's fix it here, but let's not abuse this ;)
echo %{version} >VERSION

perl -pi -e 's^r\$svn_revision^%{release}^' version.sh

mv DOCS/README README.DOCS

%build
export CFLAGS="$CFLAGS %{optflags}"
%if %{build_debug}
export CFLAGS="$CFLAGS -g"
%endif
%ifarch ppc
export CFLAGS="$CFLAGS -mcpu=7450 -maltivec"
%endif
%if %{build_directfb}
export CPPFLAGS="-I%{_includedir}/directfb"
%endif
export LDFLAGS="%{?ldflags}"
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}/%{name} \
	--confdir=%{_sysconfdir}/%{name} \
	--libdir=%{_libdir} \
%if %{with cpudetection}
	--enable-runtime-cpudetection \
%endif
%if ! %{build_dts}
	--disable-libdca \
	--enable-libdca-dlopen \
%endif
%ifarch %{ix86}
	--enable-mmx \
	--enable-3dnow \
	--enable-sse \
	--enable-sse2 \
	--enable-fastmemcpy \
%endif
	--enable-freetype \
	--enable-nas \
%if %{build_debug}
	--enable-debug=3 \
%else
	--disable-sighandler \
%endif
%if %{build_gui}
	--enable-gui \
%endif
%if %{build_system_ffmpeg}
	--disable-ffmpeg_a \
%endif
	--language=all \
%if ! %{build_faad}
	--disable-faad \
	--disable-decoder=AAC \
	--enable-faad-dlopen \
%endif
%if ! %{build_faac}
	--enable-faac-dlopen \
%endif
%if ! %{build_twolame}
	--disable-twolame \
	--enable-twolame-dlopen \
%endif
%if ! %{build_x264}
	--enable-x264-dlopen \
%endif
	--disable-libdvdcss-internal \
	--enable-dvdnav \
	--disable-dvdread-internal \
	--enable-dvdread \
%if %{build_lirc}
	--enable-lirc \
%else
	--disable-lirc \
%endif
	--enable-tv \
%if ! %{build_v4l2}
	--disable-tv-v4l2 \
%endif
	--enable-joystick \
	--enable-gl \
	--disable-svga \
%if ! %{build_mga}
	--disable-mga \
%endif
%if ! %{build_fbdev}
	--disable-fbdev \
%endif
%if %{build_directfb}
	--enable-directfb \
%else
	--disable-directfb \
%endif
%if %{build_mencoder}
	--enable-mencoder \
%else
	--disable-mencoder \
%endif
%if ! %{build_live}
	--disable-live \
%endif
%if ! %{build_vesa}
	--disable-vesa \
%endif
%if %{build_theora}
	--enable-theora \
%else
	--disable-theora \
%endif
	--enable-menu \
%if %{build_xmms}
	--enable-xmms --with-xmmslibdir=%{_libdir} \
%endif
%if %{build_smb}
	--enable-smb \
%endif
%if ! %{build_dvb}
	--disable-dvb \
	--disable-dvbhead \
%endif
%if ! %{build_ggi}
	--disable-ggi \
%endif
	--codecsdir=%{_libdir}/codecs \
%if ! %{build_arts}
	--disable-arts \
%endif
%if ! %{build_jack}
	--disable-jack \
%endif
%if ! %{build_aa}
	--disable-aa \
%endif
%if ! %{build_cdda}
	--disable-cdparanoia \
%endif
%if ! %{build_dv}
	--disable-libdv \
%endif
%if ! %{build_lzo}
	--disable-liblzo \
%endif
%if ! %{build_sdl}
	--disable-sdl \
%endif
%if ! %{build_alsa}
	--disable-alsa \
%endif
%if ! %{build_fribidi}
	--disable-fribidi \
%endif
%if ! %{build_enca}
	--disable-enca \
%endif
%if %{build_pulse}
	--enable-pulse \
%endif
%if ! %{build_openal}
	--disable-openal \
%endif
	--disable-zr \
%if %{build_xvmc}
	--enable-xvmc \
%endif
%if ! %{build_ivtv}
	--disable-ivtv \
%endif
%if ! %{build_vdpau}
	--disable-vdpau \
%endif
%if ! %{build_amr}
	--disable-libopencore_amrnb \
	--disable-libopencore_amrwb \
	--enable-libopencore_amrnb-dlopen \
	--enable-libopencore_amrwb-dlopen
%endif


# Keep this line before empty end %%configure (ppc conditionnal pb)
make
#gw make sure we have our version string included:
fgrep %{version} version.h

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m755 mplayer -D %{buildroot}%{_bindir}/mplayer
for lang in de fr hu pl es it zh_CN en; do
    install -m644 DOCS/man/$lang/mplayer.1 -D %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mplayer.1
done

%find_lang mplayer --with-man

######################### Mencoder #########################
%if %{build_mencoder}
install -m755 mencoder -D %{buildroot}%{_bindir}/mencoder

for lang in de fr hu pl es it zh_CN en; do
    ln -s mplayer.1 %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mencoder.1
done

%find_lang mencoder --with-man

install -m 755 TOOLS/mencvcd.sh %{buildroot}%{_bindir}/mencvcd
install -m 755 TOOLS/divx2svcd.sh %{buildroot}%{_bindir}/divx2svcd
install -m 755 TOOLS/wma2ogg.pl %{buildroot}%{_bindir}/wma2ogg.pl
install -m 755 TOOLS/midentify.sh %{buildroot}%{_bindir}/midentify
%endif
######################### /Mencoder #########################

install -m 644 etc/example.conf %{buildroot}%{_sysconfdir}/%{name}/mplayer.conf
install -m 644 etc/menu.conf %{buildroot}%{_sysconfdir}/%{name}

%if %{build_gui}
# default Skin
install -d -m 755 %{buildroot}%{_datadir}/%{name}/skins/
cp -r Blue %{buildroot}%{_datadir}/%{name}/skins/
ln -s Blue %{buildroot}%{_datadir}/%{name}/skins/default
# gmplayer equals mplayer -gui
ln -s mplayer %{buildroot}%{_bindir}/gmplayer
# icons
mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
convert -transparent white Blue/icons/icon48x48.png %{buildroot}%{_liconsdir}/mplayer.png 
convert -transparent white Blue/icons/icon32x32.png %{buildroot}%{_iconsdir}/mplayer.png 
convert -transparent white -scale 16x16 Blue/icons/icon48x48.png %{buildroot}%{_miconsdir}/mplayer.png
install -D -m 644 etc/mplayer.desktop %{buildroot}%{_datadir}/applications/mplayer.desktop
perl -pi -e 's@mplayer$@mplayer@g' %{buildroot}%{_datadir}/applications/mplayer.desktop
%endif

%if %{build_debug}
export DONT_STRIP=1
%endif

%if %{build_gui}
%pre gui
if [ -d %{_datadir}/%{name}/skins/default ]
  then rm -rf %{_datadir}/%{name}/skins/default
fi
%endif

%files -f mplayer.lang
%doc AUTHORS Changelog README Copyright
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/mplayer.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/menu.conf
%{_bindir}/midentify
%{_bindir}/mplayer
%{_mandir}/man1/mplayer.1*
%dir %{_datadir}/%{name}

%files doc
%doc README.DOCS
%doc DOCS/default.css DOCS/xml DOCS/tech/

%if %{build_mencoder}
%files -n mencoder -f mencoder.lang
%{_bindir}/mencoder
%{_bindir}/divx2svcd
%{_bindir}/mencvcd
%{_bindir}/wma2ogg.pl
%{_mandir}/man1/mencoder.1*
%endif

%if %{build_gui}
%files gui
%{_bindir}/gmplayer
%{_datadir}/applications/mplayer.desktop
%{_datadir}/%{name}/skins
%{_iconsdir}/mplayer.png
%{_miconsdir}/mplayer.png
%{_liconsdir}/mplayer.png
%endif

