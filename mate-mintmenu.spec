Summary:	Advanced MATE menu
Name:		mate-mintmenu
Version:	5.5.8
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://packages.linuxmint.com/pool/main/m/mintmenu/mintmenu_%{version}.tar.gz
# Source0-md5:	21e75f32aed47c78cce222a8d9207f1c
URL:		http://packages.linuxmint.com/pool/main/m/mintmenu/
Requires(post,postun):	glib2
Requires:	mate-panel
Requires:	python-Xlib
Requires:	python-matemenu
Requires:	python-modules
Requires:	python-pygobject3
Requires:	python-pyinotify
Requires:	python-pyxdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced MATE menu.

%prep
%setup -q -n mintmenu

grep -rl '%{_prefix}/lib/linuxmint/mintMenu' usr | xargs %{__sed} -i 's,%{_prefix}/lib/linuxmint/mintMenu,%{_datadir}/mate-mintmenu,g'

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}
%{__cp} -pr usr/lib/linuxmint/mintMenu $RPM_BUILD_ROOT%{_datadir}/mate-mintmenu
%{__cp} -pr usr/share/{dbus-1,glib-2.0,mate-panel} $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%{_datadir}/dbus-1/services/org.mate.panel.applet.MintMenuAppletFactory.service
%{_datadir}/glib-2.0/schemas/com.linuxmint.mintmenu.gschema.xml
%dir %{_datadir}/mate-mintmenu
%{_datadir}/mate-mintmenu/applications.list
%{_datadir}/mate-mintmenu/capi.py
%{_datadir}/mate-mintmenu/keybinding.py
%{_datadir}/mate-mintmenu/mintMenuConfig.glade
%attr(755,root,root) %{_datadir}/mate-mintmenu/mintMenuConfig.py
%{_datadir}/mate-mintmenu/mintMenu.glade
%attr(755,root,root) %{_datadir}/mate-mintmenu/mintMenu.py
%{_datadir}/mate-mintmenu/plugins
%{_datadir}/mate-mintmenu/pointerMonitor.py
%{_datadir}/mate-mintmenu/popup.xml
%{_datadir}/mate-mintmenu/search_engines
%{_datadir}/mate-mintmenu/*.png
%{_datadir}/mate-mintmenu/*.svg
%{_datadir}/mate-panel/applets/org.mate.panel.MintMenuApplet.mate-panel-applet
