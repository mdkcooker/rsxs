Name:		rsxs
Version:	1.0
Release:	2
License:	GPLv3
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:		rsxs-1.0-add-missing-linkage.patch
Patch1:		rsxs-1.0-string-format-fixes.patch
Patch2:		rsxs-1.0-libpng16.patch
URL:		http://rsxs.sourceforge.net/
BuildRequires:	pkgconfig(sm) pkgconfig(ice) pkgconfig(xmu) pkgconfig(xt)
BuildRequires:	pkgconfig(gl) pkgconfig(glu) pkgconfig(libpng)
BuildRequires:	pkgconfig(openal) pkgconfig(vorbis)
BuildRequires:	xscreensaver-base >= 5.26-2
Summary:	Really Slick XScreenSavers
Group:		Graphical desktop/Other
Requires:	xscreensaver-base >= 5.26-2 xscreensaver-gl

%description
The Really Slick XScreenSavers package is an X11/GLX port of the
Really Slick Screensavers collection, by Terry Welsh
(http://www.reallyslick.com).

%prep
%setup -q
%apply_patches
autoreconf -fiv

%build
%global optflags %{optflags} -Ofast
%configure	--with-xscreensaver \
		--with-hackdir=%{_bindir} \
		--with-moduledir=%{_datadir}/xscreensaver/hacks.conf.d \
		--with-defaultdir \
		--with-configdir=%{_datadir}/xscreensaver/config \
		--enable-image \
		--enable-sound=dlopen \
		--with-openal \
		--with-vorbisfile \
		--with-png \
		--with-x	
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README THANKS
%{_bindir}/rs-*
%{_datadir}/xscreensaver/hacks.conf.d/rs-*
%{_datadir}/xscreensaver/config/rs-*.xml
%{_datadir}/rsxs

%changelog
* Wed Apr  8 2014 Per Øyvind Karlsen <proyvind@moondrake.org>
- initial Moondrake release

* Fri Nov 21 2008 Michael Chapman <foonly@users.sourceforge.net> 1.0-1
- bump license to GPLv3
- another package overhaul, for even more modern OSs
- moved hack config into separate files, to be compatible with "modular"
  XScreenSaver configurations (eg, Fedora)
- fixed skyrocket window reshape handler
- attempt to maximize or use "real" fullscreen mode with --fullscreen option

* Sat Jul 15 2005 Michael Chapman <foonly@users.sourceforge.net> 0.9-1
- fixed skyrocket memory allocation
- fixed xscreensaver config files
- added hyperspace screensaver
- package overhaul; it now actually builds on modern OSs!
- added libltdl so sound can be dynamically loaded; this simplifies
  the RPM packaging considerably

* Fri Jul 11 2003 Michael Chapman <foonly@users.sourceforge.net> 0.8-1
- major package restructure
- added skyrocket screensaver

* Wed Dec 11 2002 Michael Chapman <foonly@users.sourceforge.net> 0.7-1
- added flocks screensaver
- added flux screensaver
- added solarwinds screensaver
- cleaned up command-line argument handling
- added support for pre-4.0 versions of xscreensaver

* Sat Dec 07 2002 Michael Chapman <foonly@users.sourceforge.net> 0.6-1
- added lattice screensaver
- converted textures to PNG format
- small Makefile fix to build correctly on Gentoo

* Tue Nov 28 2002 Michael Chapman <foonly@users.sourceforge.net> 0.5-1
- added euphoria screensaver
- fixed bug in timing delay
- removed unnecessary #include <ios>

* Tue Nov 27 2002 Michael Chapman <foonly@users.sourceforge.net> 0.4-2
- fixed uninstall script -- should upgrade properly now
- fixed bug in timing delay

* Tue Nov 26 2002 Michael Chapman <mchapman@student.usyd.edu.au> 0.4-1
- added helios screensaver
- expanded screensaver descriptions
- removed unnecessary labels

* Mon Nov 19 2002 Michael Chapman <mchapman@student.usyd.edu.au> 0.3-1
- added fieldlines screensaver
- fixed bug in this changelog (!)
- fixed bug in uninstall and verify scripts

* Mon Nov 18 2002 Michael Chapman <mchapman@student.usyd.edu.au> 0.2-1
- added cyclone screensaver

* Tue Nov 12 2002 Michael Chapman <mchapman@student.usyd.edu.au> 0.1-1
- initial version
