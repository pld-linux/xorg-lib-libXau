Summary:	Xau - Authorization Protocol for X
Summary(pl):	Xau - protokó³ autoryzacji dla X
Name:		xorg-lib-libXau
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXau-%{version}.tar.bz2
# Source0-md5:	1c5c9779d78f45267cae2e6cc1856517
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXau
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xau - Authorization Protocol for X.

%description -l pl
Xau - protokó³ autoryzacji dla X.

%package devel
Summary:	Header files libXau development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXau
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXau-devel

%description devel
Xau - Authorization Protocol for X.

This package contains the header files needed to develop programs that
use these libXau.

%description devel -l pl
Xau - protokó³ autoryzacji dla X.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXau.

%package static
Summary:	Static libXau library
Summary(pl):	Biblioteka statyczna libXau
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXau-static

%description static
Xau - Authorization Protocol for X.

This package contains the static libXau library.

%description static -l pl
Xau - protokó³ autoryzacji dla X.

Pakiet zawiera statyczn± bibliotekê libXau.

%prep
%setup -q -n libXau-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libXau.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXau.so
%{_libdir}/libXau.la
%{_includedir}/X11/Xauth.h
%{_pkgconfigdir}/xau.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXau.a
