Summary:	Advanced MATE menu
Summary(pl.UTF-8):	Zaawansowane menu dla MATE
Name:		mate-mintmenu
Version:	5.7.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://packages.linuxmint.com/pool/main/m/mintmenu/mintmenu_%{version}.tar.xz
# Source0-md5:	1f3b7a5e403e920f74602a93eb558db7
URL:		http://packages.linuxmint.com/pool/main/m/mintmenu/
BuildRequires:	sed >= 4.0
Requires(post,postun):	glib2 >= 1:2.26
Requires:	gtk+2 >= 1:2.20
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

%description -l pl.UTF-8
Zaawansowane menu dla MATE.

%prep
%setup -q -n mintmenu

%{__sed} -i 's,version = commands.getoutput("/usr/lib/linuxmint/common/version.py mintmenu"),version = "%{version}",' usr/lib/linuxmint/mintMenu/mintMenu.py
grep -rl '%{_prefix}/lib/linuxmint/mintMenu' usr | xargs %{__sed} -i 's,%{_prefix}/lib/linuxmint/mintMenu,%{_datadir}/%{name},g'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}
cp -pr usr/lib/linuxmint/mintMenu $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr usr/share/{dbus-1,glib-2.0,mate-panel} $RPM_BUILD_ROOT%{_datadir}
install -p usr/bin/mintmenu $RPM_BUILD_ROOT%{_bindir}

# (build time) to compile *.py
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/compile.py

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
%{_datadir}/%{name}/capi.py
%{_datadir}/%{name}/keybinding.py
%{_datadir}/%{name}/mintMenuConfig.glade
%attr(755,root,root) %{_datadir}/%{name}/mintMenuConfig.py
%{_datadir}/%{name}/mintMenu.glade
%attr(755,root,root) %{_datadir}/%{name}/mintMenu.py
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/pointerMonitor.py
%{_datadir}/%{name}/popup.xml
%{_datadir}/%{name}/search_engines
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.svg
%{_datadir}/dbus-1/services/org.mate.panel.applet.MintMenuAppletFactory.service
%{_datadir}/glib-2.0/schemas/com.linuxmint.mintmenu.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.MintMenuApplet.mate-panel-applet
