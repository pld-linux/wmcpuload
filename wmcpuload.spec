# $Revision: 1.3 $ $Date: 2001-10-10 14:09:18 $
Summary:	Window Maker dock applet that displays current cpuload
Summary(pl):	Monitor obci±¿enia procesora dla Window Makera
Name:		WMCPULoad
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.sh.rim.or.jp/~ssato/wmcpuload-e.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
WMCPULoad is a dockapp to monitor cpu load for Window Maker. It works
fine with AfterStep and BlackBox.

%description -l pl
WMCPULoad do dokowalny graficzny monitor obci±¿enia procesora dla
Window Makera. Mo¿na go u¿ywaæ z innymi zarz±dcami okien, takimi jak
Afterstep czy Blackbox.

%prep
%setup  -q

%build
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README ChangeLog AUTHORS NEWS THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/wmcpuload

%{_applnkdir}/DockApplets/WMCPULoad.desktop
