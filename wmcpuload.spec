Summary:	Window Maker dock applet that displays current cpuload
Summary(pl):	Monitor obci±¿enia procesora dla Window Makera
Name:		wmcpuload
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.sh.rim.or.jp/~ssato/wmcpuload-e.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
WMCPULoad is a dockapp to monitor cpu load for Window Maker. It works
fine with AfterStep and BlackBox.

%description -l pl
WMCPULoad do dokowalny graficzny monitor obci±¿enia procesora dla
Window Makera. Mo¿na go u¿ywaæ z innymi zarz±dcami okien, takimi jak
Afterstep czy Blackbox.

%prep
%setup -q -n wmcpuload-%{version}

%build
ln -s ../libdockapp src
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/wmcpuload
%{_mandir}/man1/wmcpuload.1*
#%%{_applnkdir}/DockApplets/WMCPULoad.desktop
