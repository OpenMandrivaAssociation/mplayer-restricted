%define build_3264bit     0
%{?_with_3264bit: %{expand: %%global build_3264bit 1}}
%{?_without_3264bit: %{expand: %%global build_3264bit 0}}
%if %{build_3264bit}
%define	pkgext	32
%else
%define pkgext	%{nil}
%endif

%define name		mplayer%{pkgext}
%define Name		MPlayer
%define Summary		Movie player for linux
%define prerel		%nil
%define version 1.1
%define svn %nil
%if "%svn" != ""
%define fversion %{svn}
%else
%define fversion %{version}
%endif
%if "%{prerel}" != ""
%if "%{svn}" != ""
%define rel		1.%{prerel}.0.%{svn}.1
%else 
%define rel 1.%{prerel}.6
%endif
%else
%if "%{svn}" != ""
%define rel 0.%{svn}.1
%else
%define rel 5
%endif
%endif

%define build_plf	0
%define build_optimization	0
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

%{?_with_plf: %{expand: %%global build_plf 1}}

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
%{?_with_optimization: %{expand: %%global build_optimization 1}}
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


Name:		%{name}
Version:	%{version}
Release:	%{rel}%{?extrarelsuffix}
Summary:	%{Summary}
%if "%svn" != ""
#gw generated using svn export
Source0:	%{name}-%{svn}.tar.xz
%else
Source0:	ftp://ftp1.mplayerhq.hu/MPlayer/releases/%{Name}-%{fversion}.tar.xz
%endif
#gw default skin
Source4:	Blue-1.8.tar.bz2
Source5:	kernel-version.sh
Patch0:		mplayer-mdvconfig.patch
# fixes for crashes found while fixing CVE-2008-1558
Patch28:	mplayer-rtsp-extra-fixes.patch
Patch31:       mplayer-format-string-literal.patch
#gw HAVE_DLFCN_H isn't defined
Patch33:       mplayer-have-dlfcn_h.patch
#gw fix crash: https://qa.mandriva.com/show_bug.cgi?id=55443
Patch35:	mplayer-fix-dvd-crash.patch
Patch39:	mplayer-dlopen-libfaac-libfaad-and-libx264.patch
Patch40:	mplayer-r34578-local-copy-of-internal-ffmpeg-type-definition.patch
Patch42:	mplayer-filters-hack-with-shared.patch
Patch43:	mplayer-r34911-dont-use-ffmpeg-functionality-outside-stable-release.patch
Patch44:        mplayer-mp_taglists-declaration.patch
URL:		http://www.mplayerhq.hu
License:	GPLv2
Group:		Video
BuildRequires:	pkgconfig(ncursesw)
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
BuildRequires:	libdxr3-devel
BuildRequires:	jpeg-devel
BuildRequires:	openjpeg-devel
%if %{build_lirc}
BuildRequires:	pkgconfig(liblircclient0)
%endif
%if %{build_lzo}
BuildRequires:	liblzo-devel
%endif
BuildRequires:  pkgconfig(mad)
BuildRequires:  nas-devel
BuildRequires:	pkgconfig(libpng15)
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
# require samba < 3.2.0 to avoid shipping GPLv2 vs GPLv3
BuildRequires:	libsmbclient-devel < 3.2.0
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
BuildRequires:	gsm-devel
BuildRequires:	pkgconfig(libmpg123)
%if %{build_vpx}
BuildRequires:	pkgconfig(vpx)
%endif
%if %{build_rtmp}
BuildRequires:	pkgconfig(librtmp)
%endif
BuildRequires:	bzip2-devel
BuildRequires:	mng-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(speex)
BuildRequires:	libmpcdec-devel
BuildRequires:	ladspa-devel
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd412-xml
BuildRequires:	pkgconfig(caca)
BuildRequires:	giflib-devel
%if %{build_yasm}
BuildRequires:	yasm
%endif
BuildRequires:	pkgconfig(libbs2b)
%if %{build_system_ffmpeg}
BuildRequires:	ffmpeg-devel
%endif
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(dvdnavmini)

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

%rename		mplayer%{pkgext}1.0

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
Summary:	%{Name} documentation
Group:		Books/Computer books
BuildArch:	noarch

%description doc
This package contains documentation for %{Name}.

%if %{build_gui}
%package gui
Summary:	GUI for %{name}
Group:		Video
Requires:	%{name} = %{version}
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	imagemagick
Requires:	soundwrapper
%rename		mplayer%{pkgext}1.0-gui
Conflicts:	mplayer-skins < 1.3

%description gui
This package contains a GUI for %{name}.
%endif

%if %{build_mencoder}
%package -n mencoder%{pkgext}
Summary:	MPlayer's movie encoder
Group:		Video
Requires:	%{name}
%rename		mencoder%{pkgext}1.0

%description -n mencoder%{pkgext}
MEncoder a movie encoder and is a part of the MPlayer package.
%if ! %{build_plf}
Note: this version doesn't have support for encoding mp3 audio streams in the
video files.
%else
This restricted build has additional support for AAC decoding with libfaad
and MP3 encoding with lame, both are covered by software patents. It
also includes support for reading DVDs encrypted with CSS which might
be illegal in some countries.
%endif
%endif


#' close.. vim syntax highlight workaround.. ;p

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
%patch33 -p0
%patch35 -p0
%if ! %{build_plf}
%patch39 -p1 -b .dlopen~
%endif
rm -rf ffmpeg
%patch40 -p1 -b .ffmpeg~
%patch42 -p1 -b .internal_filters~
%patch43 -p1 -b .ffm_stable~
%patch44 -p0 -b .mp_taglists~

perl -pi -e 's^r\$svn_revision^%{release}^' version.sh

mv DOCS/README README.DOCS

%build
%if !%{build_optimization}
export CFLAGS="$CFLAGS %{optflags}"
%endif
%if %{build_debug}
export CFLAGS="$CFLAGS -g"
%endif
%ifarch ppc
export CFLAGS="$CFLAGS -mcpu=7450 -maltivec"
%endif
%if %{build_directfb}
export CPPFLAGS="-I%{_includedir}/directfb"
%endif
%if %{build_3264bit}
export EXESUF=32
%endif
export LDFLAGS="%{?ldflags}"
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir}/%{name} \
	--confdir=%{_sysconfdir}/%{name} \
	--libdir=%{_libdir} \
%if ! %{build_optimization}
	--enable-runtime-cpudetection \
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
make EXESUF=%{pkgext}
#gw make sure we have our version string included:
fgrep %{version} version.h

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -m755 mplayer%{pkgext} -D %{buildroot}%{_bindir}/mplayer%{pkgext}
for lang in de fr hu pl es it zh_CN en; do
    install -m644 DOCS/man/$lang/mplayer.1 -D %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mplayer%{pkgext}.1
done

%find_lang mplayer%{pkgext} --with-man

######################### Mencoder #########################
%if %{build_mencoder}
install -m755 mencoder%{pkgext} -D %{buildroot}%{_bindir}/mencoder%{pkgext}

for lang in de fr hu pl es it zh_CN en; do
    ln -s mplayer%{pkgext}.1 %{buildroot}%{_mandir}/$([ "$lang" != "en" ] && echo $lang)/man1/mencoder%{pkgext}.1
done

%find_lang mencoder%{pkgext} --with-man

install -m 755 TOOLS/mencvcd.sh %{buildroot}%{_bindir}/mencvcd%{pkgext}
install -m 755 TOOLS/divx2svcd.sh %{buildroot}%{_bindir}/divx2svcd%{pkgext}
install -m 755 TOOLS/wma2ogg.pl %{buildroot}%{_bindir}/wma2ogg%{pkgext}.pl
install -m 755 TOOLS/midentify.sh %{buildroot}%{_bindir}/midentify%{pkgext}
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
ln -s mplayer%{pkgext} %{buildroot}%{_bindir}/gmplayer%{pkgext}
# icons
mkdir -p %{buildroot}{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
convert -transparent white Blue/icons/icon48x48.png %{buildroot}%{_liconsdir}/mplayer%{pkgext}.png 
convert -transparent white Blue/icons/icon32x32.png %{buildroot}%{_iconsdir}/mplayer%{pkgext}.png 
convert -transparent white -scale 16x16 Blue/icons/icon48x48.png %{buildroot}%{_miconsdir}/mplayer%{pkgext}.png
install -D -m 644 etc/mplayer.desktop %{buildroot}%{_datadir}/applications/mplayer%{pkgext}.desktop
perl -pi -e 's@mplayer$@mplayer%{pkgext}@g' %{buildroot}%{_datadir}/applications/mplayer%{pkgext}.desktop
%endif

%if %{build_3264bit}
if [ -e %{buildroot}%{_liconsdir}/mplayer%{pkgext}.png ]; then
	convert %{buildroot}%{_liconsdir}/mplayer%{pkgext}.png -channel green -negate \
		%{buildroot}%{_liconsdir}/mplayer%{pkgext}.png
fi
if [ -e %{buildroot}%{_iconsdir}/mplayer%{pkgext}.png ]; then
	convert %{buildroot}%{_iconsdir}/mplayer%{pkgext}.png -channel green -negate \
		%{buildroot}%{_iconsdir}/mplayer%{pkgext}.png
fi
if [ -e %{buildroot}%{_miconsdir}/mplayer%{pkgext}.png ]; then
	convert %{buildroot}%{_miconsdir}/mplayer%{pkgext}.png -channel green -negate \
		%{buildroot}%{_miconsdir}/mplayer%{pkgext}.png
fi
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

%files -f mplayer%{pkgext}.lang
%doc AUTHORS Changelog README Copyright
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/mplayer.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/menu.conf
%{_bindir}/midentify%{pkgext}
%{_bindir}/mplayer%{pkgext}
%{_mandir}/man1/mplayer%{pkgext}.1*
%dir %{_datadir}/%{name}

%files doc
%defattr(-,root,root,755)
%doc README.DOCS
%doc DOCS/default.css DOCS/xml DOCS/tech/

%if %{build_mencoder}
%files -n mencoder%{pkgext} -f mencoder%{pkgext}.lang
%{_bindir}/mencoder%{pkgext}
%{_bindir}/divx2svcd%{pkgext}
%{_bindir}/mencvcd%{pkgext}
%{_bindir}/wma2ogg%{pkgext}.pl
%{_mandir}/man1/mencoder%{pkgext}.1*
%endif

%if %{build_gui}
%files gui
%{_bindir}/gmplayer%{pkgext}
%{_datadir}/applications/mplayer%{pkgext}.desktop
%{_datadir}/%{name}/skins
%{_iconsdir}/mplayer%{pkgext}.png
%{_miconsdir}/mplayer%{pkgext}.png
%{_liconsdir}/mplayer%{pkgext}.png
%endif


%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.1-2mdv2012.0
+ Revision: 803487
- Rebuild for ffmpeg 0.11

* Thu Jun 07 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.1-1
+ Revision: 803108
- Update to 1.1 Final

* Tue Jun 05 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34991.1
+ Revision: 802529
- new svn snapshot

* Thu May 17 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34911.1
+ Revision: 799325
- don't use ffmpeg functionality not in stable release (P43)
- new svn snapshot
- rebuild to get rid of rpmlib(DistEpoch) dep

* Tue Mar 13 2012 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r34578.4
+ Revision: 784777
- update default skin (bug #65376)

* Wed Feb 01 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34578.3
+ Revision: 770472
- ship with (latest) local copies of a few internal ffmpeg headers after all...
- fix missing FFmpeg filters (bug #4191, lavcac3enc-build-with-shared.patch,
  filters-hack-with-shared.patch, from Mageia)

* Sat Jan 21 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34578.2
+ Revision: 764826
- be sure to not build against any local copy of ffmpeg headers (P40)

* Tue Jan 17 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34578.1
+ Revision: 761959
- build against system dvdnavn & dvdread
- doc subpackage shouuld be noarch
- remove versioned dependency on mplayer for mencoder (to work with ie. mplayer2)
- build against system ffmpeg
- new svn snapshot
- fix loading of x264_encoder_open() through dlopen()..

  + Anssi Hannula <anssi@mandriva.org>
    - drop .spec comment referring to a removed patch

* Wed Jan 11 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34537.4
+ Revision: 759782
- fix libfaac library not getting dlopen()'ed
- be sure to load the correct functions when dlopen()'ing opencore-amrwb

* Wed Jan 11 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34537.3
+ Revision: 759725
- really fix libx264 dlopen support and make sure to actually enable it for real

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix opencore build dep

* Wed Jan 11 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34537.2
+ Revision: 759711
- fix broken path to skins (from Z?\195?\169)
- fix libx264 being loaded at the wrong place in dlopen patch

* Tue Jan 10 2012 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r34537.1
+ Revision: 759288
- change plf specific requires on libdvdcss package into a suggests on soname
- bump major of libx264 soname
- fix permissions of directories in doc package
- drop soundwrapper patch (P12)
- new version
- use pkgconfig() or at least multilib-neutral dependencies
--enable-runtime-cpudetection on x86_64 as well as newer instruction sets
  available may be used

* Wed Nov 23 2011 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r32713.8
+ Revision: 732994
- fix typo
- fix dlopen() patch and add support for opencore-amr[wn]b, twolame & libdca too
- again, don't do things un subshell..
- remove useless dependencies on desktop-file-utils
- apply some cosmetics to man page installation etc..
- don't do stuff in sub-shells where we don't get the return code
- use %%rename macro
- clean out old rpm junk & conditionals to support build on ancient releases
- add suggests on libraries to be dlopen()'ed
- dlopen() libfaad, libfaac & libx264 so that regular mplayer build may support
  these without separate build linked against those (more to come)

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-1.rc4.0.r32713.7
+ Revision: 702687
- fix build against libpng-1.5.x
- attempt to relink against libpng15.so.15

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 1.0-1.rc4.0.r32713.6
+ Revision: 677477
- rebuild for updated mimehandler

* Wed May 11 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1.rc4.0.r32713.5
+ Revision: 673440
- Fix ff_imdct_calc_sse() on gcc-4.6.

* Sat May 07 2011 Per Ãyvind Karlsen <peroyvind@mandriva.org> 1.0-1.rc4.0.r32713.4
+ Revision: 672318
- fix high pitch hiss sound with mp3lib when building with gcc 4.6 (P36)

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.0-1.rc4.0.r32713.3
+ Revision: 670212
- disable zr, it is requireing v4l1

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - plf: append "plf" to Release on cooker to make plf build have higher EVR
      again with the rpm5-style mkrel now in use

* Fri Dec 17 2010 Funda Wang <fwang@mandriva.org> 1.0-1.rc4.0.r32713.2mdv2011.0
+ Revision: 622495
- rebuild for new directfb

* Tue Dec 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r32713.1mdv2011.0
+ Revision: 621733
- new snapshot
- rediff patch 0
- bump x264 dep
- disable rtmp for backports
- disable vpx for backports
- disable libass for backports
- cleanup

* Mon Dec 06 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r32675.1mdv2011.0
+ Revision: 612232
- enable libass, gsm, mpg123, vpx and rtmp
- new snapshot
- use svn exported tarball to reduce source package size
- drop patches 1,26,36
- rediff patches 12,31
- disable integrated AAC decoder

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-1.rc4.0.r31086.4mdv2011.0
+ Revision: 606663
- rebuild

* Wed May 05 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r31086.3mdv2010.1
+ Revision: 542309
- rebuild
- bump x264 dep

* Sun May 02 2010 Anssi Hannula <anssi@mandriva.org> 1.0-1.rc4.0.r31086.2mdv2010.1
+ Revision: 541619
- fix regression in playback of VP6F video streams (e.g. some flv files)
  (fix-vp6f.patch)

* Sun Apr 25 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r31086.1mdv2010.1
+ Revision: 538606
- new snapshot
- move all binary codecs to %%_libdir/codecs

* Sat Jan 23 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r30392.1mdv2010.1
+ Revision: 495207
- new snapshot

* Sun Jan 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r30268.1mdv2010.1
+ Revision: 489248
- new snapshot
- fix giflib detection
- build with a52dec and openjpeg support
- fix fribidi build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libjpeg v8

* Sun Dec 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r30130.1mdv2010.1
+ Revision: 482824
- new version
- drop patch 34

* Thu Dec 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r29987.1mdv2010.1
+ Revision: 476009
- new version
- rediff patch 0

* Tue Nov 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r29964.1mdv2010.1
+ Revision: 469542
- new snapshot
- add patch for DVD crash (bug #55443)

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 1.0-1.rc4.0.r29850.3mdv2010.1
+ Revision: 463088
- rebuild for new dfb

* Sat Nov 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc4.0.r29850.2mdv2010.1
+ Revision: 462398
- new snapshot

* Fri Oct 16 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0-1.rc3.0.r29554.2mdv2010.0
+ Revision: 457955
- Fix initial volume setting with pulseaudio

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - increase version number

* Thu Aug 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.25.r29554.1mdv2010.0
+ Revision: 421677
- new snapshot

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-1.rc2.25.r29434.2mdv2010.0
+ Revision: 416529
- rebuilt against libjpeg v7

* Tue Jul 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.25.r29434.1mdv2010.0
+ Revision: 398417
- new snapshot
- build with bs2b support

* Mon Jul 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.25.r29433.1mdv2010.0
+ Revision: 398107
- use default linker flags (Anssi)
- new snapshot
- build with opencore-amr

* Fri Jul 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r29416.1mdv2010.0
+ Revision: 394085
- new snapshot
- fix version string patching

* Wed Jul 01 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r29409.1mdv2010.0
+ Revision: 391373
- new snapshot
- update patches 12,28,33
- spec fix

* Mon Mar 02 2009 Anssi Hannula <anssi@mandriva.org> 1.0-1.rc2.23.r28791.2mdv2009.1
+ Revision: 347009
- fix --with(out) xvmc build option
- enable vdpau support, enabled on 2009.0 and newer

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r28791.1mdv2009.1
+ Revision: 346961
- new snapshot
- rediff patch 31
- update build deps
- enable bzip2 support

* Thu Jan 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r28387.1mdv2009.1
+ Revision: 335187
- new snapshot
- fix customization of the version string
- disable dirac and schroedinger on 2009.0

* Fri Jan 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r28348.1mdv2009.1
+ Revision: 332710
- new snapshot
- drop patch 1
- fix icon

* Thu Jan 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23.r28347.1mdv2009.1
+ Revision: 332605
- new snapshot
- enable dirac, schroedinger, mng support
- always use included libdvdnav and libdvdread
- drop source 6
- drop patches 2,4,19,20,22,23,24,25,27,29,30
- rediff patch 12, 31
- disable patches 1,3,7,21
- fix build

  + Per Ãyvind Karlsen <peroyvind@mandriva.org>
    - fix issue with attempting to free an invalid pointer when opening rar files (P32)
    - fix build with -Werror=format-security (P31)

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Oct 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.23mdv2009.1
+ Revision: 298652
- fix for CVS-2008-0073

* Sun Oct 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.22mdv2009.1
+ Revision: 295423
- rebuild

* Mon Oct 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.21mdv2009.1
+ Revision: 293180
- rebuild

* Mon Oct 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.20mdv2009.1
+ Revision: 293089
- fix build with new libx264

* Sun Oct 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.19mdv2009.1
+ Revision: 292980
- rebuild

* Mon Sep 29 2008 Frederik Himpe <fhimpe@mandriva.org> 1.0-1.rc2.18mdv2009.0
+ Revision: 289726
- Add security patch fixing integer buffer underflow
  (http://www.ocert.org/advisories/ocert-2008-013.html)

* Tue Sep 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.17mdv2009.0
+ Revision: 285191
- P27: security fix for CVE-2008-1558
- P28: fixes for crashes found together with CVE-2008-1558
- disable ivtv, it does not build

* Fri Sep 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.16mdv2009.0
+ Revision: 281075
- patch to add scaletempo filter (bug #43529)
- build with new fribidi

* Sun Aug 17 2008 Funda Wang <fwang@mandriva.org> 1.0-1.rc2.15mdv2009.0
+ Revision: 273058
- disable smb in mdv > 2009 due to license incompatible
- rebuild for new dfb

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - disable dirac by default

* Fri Jul 18 2008 Buchan Milne <bgmilne@mandriva.org> 1.0-1.rc2.14mdv2009.0
+ Revision: 238214
- Buildrequire libsmbclient-devel < 3.2.0 to avoid GPLv2 vs GPLv3 issues

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 30 2008 Funda Wang <fwang@mandriva.org> 1.0-1.rc2.13mdv2009.0
+ Revision: 213500
- rebuild for new directfb

* Fri May 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.12mdv2009.0
+ Revision: 208085
- support building with external faad again
- spec cleanup

* Thu Apr 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.11mdv2009.0
+ Revision: 197147
- fix build with new libdvdnav

* Wed Feb 13 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0-1.rc2.10mdv2008.1
+ Revision: 167031
- Update patch20 with SVN version of pulseaudio plugin, fixes Mdv bug #36461
- Update patch0 to check pulse output first, if present

* Tue Feb 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.9mdv2008.1
+ Revision: 162707
- add four official security patches
- fix bug #37263 (default video output)

* Sun Jan 27 2008 Giuseppe GhibÃ² <ghibo@mandriva.com> 1.0-1.rc2.8mdv2008.1
+ Revision: 158705
- Add support for mplayer32 (to allow coexisting with 64bit mplayer in X86_64 arch, to be rebuild with --with 3264bit flag).

* Sat Jan 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.7mdv2008.1
+ Revision: 158373
- update dirac patch and enable it
- add support for building with dirac

* Thu Jan 17 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.6mdv2008.1
+ Revision: 154482
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jan 02 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.5mdv2008.1
+ Revision: 140382
- stop screensaver by default (bug #35863)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.4mdv2008.1
+ Revision: 112144
- remove input.conf to fix bug #35516
- remove URL parameter from the desktop file (bug #35248)

* Sat Oct 13 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0-1.rc2.3mdv2008.1
+ Revision: 97955
- Reenable Compiz and PulseAudio support by applying updated patches

* Wed Oct 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.2mdv2008.1
+ Revision: 96835
- remove codecs.conf

* Wed Oct 10 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc2.1mdv2008.1
+ Revision: 96634
- drop patch 11
- new version
- disable compiz and pulse support
- drop amr sources, now external libamrnb/wb is supported
- drop vidix
- drop patches 2,4,5,6,8,9,10,12,13,14,15,16,17,18,20,21,22
- rediff patches 3,12
- bump dvdnav dep
- drop legacy menu

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild

* Fri Sep 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.20mdv2008.0
+ Revision: 85498
- security fix for avi index reader

* Sun Jul 15 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0-1.rc1.19mdv2008.0
+ Revision: 52228
- Rebuild due to build system hiccup

* Sat Jul 14 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0-1.rc1.18mdv2008.0
+ Revision: 52121
- Add compiz support to xv output (needs compiz 'video' plugin to be active)

* Wed Jun 27 2007 Andreas Hasenack <andreas@mandriva.com> 1.0-1.rc1.17mdv2008.0
+ Revision: 44944
- rebuild with new rpm-mandriva-setup (-fstack-protector)

* Thu Jun 07 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.16mdv2008.0
+ Revision: 36497
- security fix for CDDB overflow

* Mon Jun 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.15mdv2008.0
+ Revision: 35218
- curity fix for CVE-2006-6172 (realmedia buffer overflow)
- amrwb update

* Mon May 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.14mdv2008.0
+ Revision: 29464
- rebuild

* Sat May 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.13mdv2008.0
+ Revision: 26466
- disable dirac again, it was breaking MPEG detection

* Fri May 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.12mdv2008.0
+ Revision: 26249
- patch for dirac support


* Thu Mar 15 2007 Olivier Blin <oblin@mandriva.com> 1.0-1.rc1.11mdv2007.1
+ Revision: 144524
- move HTML doc in a mplayer-doc sub-package

* Tue Mar 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.10mdv2007.1
+ Revision: 143064
- security fix for CVE-2007-1387

* Thu Mar 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.9mdv2007.1
+ Revision: 138476
- security patch for CVE-2007-1246
- support libggiwmh build

* Fri Feb 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.8mdv2007.1
+ Revision: 124957
- rebuild for new libmpcdec

* Thu Feb 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.7mdv2007.1
+ Revision: 124646
- sync with Ubuntu:
 * replace patch 1 by simple call to gconf
 * patch 14: fix buffer overflow in rtsp code
 * patch 15: pulseaudio support
- make mplayer report the package version
- depend on soundwrapper as it is used in the menu entry

* Fri Jan 05 2007 Anssi Hannula <anssi@mandriva.org> 1.0-1.rc1.6mdv2007.1
+ Revision: 104624
- fix -use-filedir-conf option (patch6, from SVN)

* Wed Nov 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.5mdv2007.1
+ Revision: 78192
- fix desktop entry

* Tue Nov 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.4mdv2007.0
+ Revision: 77317
- fix xv with mplayer plugin (ghibo)
- add soundwrapper to the menu entry
- disable dvdread, which is obsoleted by dvdnav

* Thu Oct 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.3mdv2007.1
+ Revision: 72651
- disable arts
- patch to add missing WMVA FourCC

* Wed Oct 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.rc1.2mdv2007.0
+ Revision: 72295
- bot rebuild
- new version
  enable dvdnav
  fix buildrequires
  rediff patches 1,3,11
  drop patch 2,14
  fix directfb detection
  remove obsoleted options

  + Anssi Hannula <anssi@mandriva.org>
    - fix non-plf real codecs dir

* Fri Oct 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.pre8.17mdv2007.0
+ Revision: 71231
- fix patch 2

* Fri Oct 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.pre8.16mdv2007.1
+ Revision: 71203
- update patch 2 for new x264

* Fri Oct 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-1.pre8.15mdv2007.0
+ Revision: 71172
- rebuild
- fix description
- Import mplayer

* Wed Oct 11 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.14mdv2007.1
- disable joystick by default (bug #26334)

* Thu Sep 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-1.pre8.13mdv2007.0
- Rebuild agaisnt ncurse

* Fri Sep 01 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.12mdv2007.0
- fix build on x86_64

* Wed Aug 30 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.11mdv2007.0
- patch for new x264

* Tue Aug 08 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.10mdv2007.0
- fix ogm seek (bug #23897)

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.9mdv2007.0
- rebuild for dbus

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.8mdv2007.0
- disable polypaudio

* Sat Jul 08 2006 Anssi Hannula <anssi@mandriva.org> 1.0-1.pre8.7mdv2007.0
- fix buildrequires

* Sat Jul 08 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.6mdv2007.0
- fix buildrequires

* Tue Jul 04 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.5mdv2007.0
- disable optimization by default

* Mon Jul 03 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.4mdv2007.0
- update amr

* Sun Jul 02 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.3mdv2007.0
- rebuild

* Thu Jun 22 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.2mdv2007.0
- disable dbus on 2006.0
- xdg menu

* Tue Jun 13 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.1mdv2007.0
- rediff patch 1
- new version

* Thu Jun 08 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre8.0.18614.1mdv2007.0
- fix buildrequires
- svn snapshot

* Sat May 06 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060505.1mdk
- add gnome-screensaver suspend support via dbus
- new snapshot

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060415.1mdk
- new snapshot

* Tue Apr 04 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060403.1mdk
- add vesa support
- new snapshot

* Thu Mar 23 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060323.1mdk
- fix build
- fix buildrequires
- workaround for bug 21713 (enabled optimization flag)
- new snapshot

* Tue Mar 21 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060321.1mdk
- disable openal
- new snapshot

* Thu Feb 23 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060223.1mdk
- depend on openal
- disable xmms plugin
- new snapshot

* Wed Feb 22 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060222.1mdk
- new snapshot

* Fri Jan 27 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060127.1mdk
- build fix
- rediff patch 0
- new snapshot

* Sun Jan 01 2006 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20060101.1mdk
- enable xvmc
- rediff patch 13
- new version

* Tue Dec 20 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20051220.1mdk
- fixes for 10.1
- new version

* Mon Dec 19 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20051219.1mdk
- fix dvb build (Anssi)
- disable ggi and enable directfb instead
- new snapshot

* Fri Dec 16 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20051216.1mdk
- add more build options
- update Blue skin
- new snapshot

* Thu Dec 15 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.20051215.1mdk
- drop postproc package
- fix buildrequires
- fix build
- drop patches 1,2,4,6,12,14
- rediff patches 0,13
- new version

* Wed Dec 14 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.15mdk
- patch for CVE-2005-4048 (bug #20186)

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.14mdk
- fix real path

* Sun Oct 30 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.13mdk
- configuration fixes for x86_64

* Fri Sep 09 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.12mdk
- patch for pcm overflow

* Thu Sep 08 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0-1.pre7.11mdk
- 64-bit fixes
- further gcc4 fixes from current CVS

* Wed Jun 29 2005 Götz Waschk <waschk@mandriva.org> 1.0-1.pre7.10mdk
- update patch 5 for new liblzo

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.9mdk
- patch 5 for new lzo

* Sun May 22 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0-0.pre7.8mdk
- patch12: fix ppc build with gcc 4.0

* Thu May 19 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.7mdk
- patch 3 from Austin Acton: fix creation of noisy mp2 audio files

* Wed May 11 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.6mdk
- patches 1 and 2 for gcc 4.0

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.5mdk
- rebuild for new libtheora

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.4mdk
- add midentify

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.3mdk
- add separate conditional build option for amr
- drop patches 12,13,14

* Wed Apr 20 2005 Götz Waschk <waschk@mandriva.org> 1.0-0.pre7.2mdk
- amr support (disabled by default)

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre7.1mdk
- update patch 0
- fix deps
- disable divx, it's obsolete
- mkrel support
- new version

* Tue Apr 05 2005 Buchan Milne <bgmilne@linux-mandrake.com> 1.0-0.pre6.8mdk
- Rebuild for libsmbclient

* Tue Jan 04 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre6.7mdk
- add polpyaudio support

* Tue Dec 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre6.6mdk
- drop kernel modules

* Tue Dec 28 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-0.pre6.5mdk
- Upgraded Patch11,12,13,14 for X86-64.

* Tue Dec 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre6.4mdk
- enable ladspa
- enable live
- enable dvb (fixes bug #12812)
- update patch 0 to fix bug #12834

* Mon Dec 27 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-0.pre6.3mdk
- Increased OSD font to size 3 (previous 2).

* Mon Dec 27 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-0.pre6.2mdk
- Added Martin Braun Patch13 for fixing vidix savage building
  under X86_64.

* Mon Dec 27 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-0.pre6.1mdk
- Readapted Patch0 (config), and let default OSD fonts slightly smaller.
- Removed Patch1, 2, 11, 12, 13, 14 merged upstream.
- Removed build_semistatic build flag.
- Disabled build with live library for now (doesn't build).
- Disabled parallel building.
- Added Martin Braun Patches for X86_64 (Patch11, 12).

* Thu Dec 16 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.9mdk
- new version 1.0pre5try2

* Thu Dec 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.8mdk
- fix upgrade of mplayer-gui from < 1.0-0.pre5.6mdk
- add bio2jack support

* Tue Sep 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.7mdk
- patch 1: fix GL scaling

* Thu Sep 23 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.6mdk
- disable fullscreen by default
- enable zoom by default
- merge patch1 and patch3 as new patch0
- drop support for mdk 9.0
- link default to Blue skin
- drop patch0

* Tue Sep 21 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0-0.pre5.5mdk
- patch13: fix compilation of new altivec code in postproc (for ppc)

* Tue Sep 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.4mdk
- enable v4l2 (bug #11231)

* Mon Aug 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.3mdk
- make icon transparent
- fix patch 11

* Tue Jul 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.2mdk
- enable enca 
- include patches 11 and 12 from official package
- use Blue icon
- patch2: fix build with newer live.com
- enable zr

* Fri Jul 16 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre5.1mdk
- disable alsa on 9.0
- add wma2ogg.pl
- libdha major 1.0
- patch 4: fix build with our kernel 2.6 headers
- drop merged patches 2,11
- new version

* Wed Jun 16 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0-0.pre4.8mdk
- ppc build fixes

* Thu Jun 10 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.7mdk
- add fribidi support

* Wed Jun 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.6mdk
- use parallel build
- rebuild

* Thu Jun 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.5mdk
- fix metacity fullscreen issue

* Wed Jun 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.4mdk
- add divx2svcd script

* Sat May 01 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.3mdk
- use fontconfig instead of supplied font for OSD (Michael Reinsch)

* Fri Apr 30 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.2mdk
- drop patch 2

* Thu Apr 29 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre4.1mdk
- don't depend on libmatroska and libflac anymore
- drop patch 1
- 1.0pre4

* Fri Apr 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre3.15mdk
- don't rename Blue skin to default
- always enable live

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre3.14mdk
- fix naming of the package

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre3try2.2mdk
- add Copyright file
- fix doc permissions

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-0.pre3try2.1mdk
- enable libtheora
- new libdv
- new version

