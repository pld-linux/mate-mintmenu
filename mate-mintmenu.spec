Summary:	Advanced MATE menu
Summary(pl.UTF-8):	Zaawansowane menu dla MATE
Name:		mate-mintmenu
Version:	6.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://packages.linuxmint.com/pool/main/m/mintmenu/mintmenu_%{version}.tar.xz
# Source0-md5:	04c6734fb4ef2c6493d6358848088627
Patch0:		%{name}-icon.patch
Patch1:		%{name}-disable-apt.patch
URL:		https://github.com/linuxmint/mintmenu
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26
Requires:	gtk+3
Requires:	gvfs
Requires:	mate-desktop-libs >= 1.18.0
Requires:	mate-menus-libs >= 1.22.0
Requires:	mate-panel >= 1.18.0
Requires:	python3-Xlib
Requires:	python3-configobj
Requires:	python3-modules
Requires:	python3-pygobject3
Requires:	python3-pyxdg
Requires:	python3-setproctitle
Requires:	python3-xapps-overrides
Requires:	xdg-utils
Suggests:	mozo
Suggests:	python3-pyinotify
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced MATE menu.

%description -l pl.UTF-8
Zaawansowane menu dla MATE.

%prep
%setup -qc
%patch -P0 -p1
%patch -P1 -p1
# in case of patching fuzz
rm -f mintmenu/usr/share/glib-2.0/schemas/com.linuxmint.mintmenu.gschema.xml.orig

%{__mv} mintmenu/* .

%{__sed} -i 's,__DEB_VERSION__,%{version},' usr/lib/linuxmint/mintMenu/mintMenu.py
grep -rl 'usr/lib/linuxmint/mintMenu' usr | xargs %{__sed} -i 's,usr/lib/linuxmint/mintMenu,%{_datadir}/%{name},g'
grep -rl 'usr/share/linuxmint/mintmenu' usr | xargs %{__sed} -i 's,usr/share/linuxmint/mintmenu,%{_datadir}/%{name},g'
%{__sed} -i 's,^#!.*python.*,#!%{__python3},' usr/lib/linuxmint/mintMenu/{,plugins/}*.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}
cp -pr usr/lib/linuxmint/mintMenu $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr usr/share/linuxmint/mintmenu/*.ui $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr usr/share/{dbus-1,glib-2.0,man,mate-panel,pixmaps} $RPM_BUILD_ROOT%{_datadir}
install -p usr/bin/mintmenu $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mintmenu
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/applications.list
%{_datadir}/%{name}/keybinding.py
%attr(755,root,root) %{_datadir}/%{name}/mintMenu.py
%attr(755,root,root) %{_datadir}/%{name}/preferences.py
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/*.py
%{_datadir}/%{name}/pointerMonitor.py
%{_datadir}/%{name}/popup.xml
%{_datadir}/%{name}/popup-without-edit.xml
%{_datadir}/%{name}/search_engines
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.svg
%{_datadir}/%{name}/*.ui
%{_datadir}/dbus-1/services/org.mate.panel.applet.MintMenuAppletFactory.service
%{_datadir}/glib-2.0/schemas/com.linuxmint.mintmenu.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MintMenuApplet.mate-panel-applet
%{_mandir}/man1/mintmenu.1*
%{_pixmapsdir}/mintmenu.svg
