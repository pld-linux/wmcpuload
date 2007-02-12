Summary:	Window Maker dock applet that displays current cpuload
Summary(pl.UTF-8):	Monitor obciążenia procesora dla Window Makera
Name:		wmcpuload
Version:	1.0.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
#Source0Download: http://seiichisato.jp/dockapps/
Source0:	http://seiichisato.jp/dockapps/src/%{name}-%{version}.tar.gz
# Source0-md5:	93a28a62d31d4b283edd78fffafb0835
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
URL:		http://seiichisato.jp/dockapps/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	WMCPULoad
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMCPULoad is a dockapp to monitor cpu load for Window Maker. It works
fine with AfterStep and BlackBox.

%description -l pl.UTF-8
WMCPULoad do dokowalny graficzny monitor obciążenia procesora dla
Window Makera. Można go używać z innymi zarządcami okien, takimi jak
Afterstep czy Blackbox.

%prep
%setup -q
%patch0 -p1

%build
ln -s ../libdockapp src
ln -s ../libdockapp/dockapp.o src/
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/wmcpuload
%{_mandir}/man1/wmcpuload.1*
%{_desktopdir}/docklets/*
