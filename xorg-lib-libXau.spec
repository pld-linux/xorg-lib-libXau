Summary:	Xau - X authorization file management library
Summary(pl.UTF-8):	Xau - biblioteka zarządzająca plikami autoryzacji X
Name:		xorg-lib-libXau
Version:	1.0.12
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.xz
# Source0-md5:	4c9f81acf00b62e5de56a912691bd737
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	libXau < 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xau is the X authorization file management library, conforming to X
Authorization Protocol.

%description -l pl.UTF-8
Xau to biblioteka zarządzająca plikami autoryzacji X zgodnie z
protokołem autoryzacji X.

%package devel
Summary:	Header files for libXau library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXau
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xproto-devel
Obsoletes:	libXau-devel < 0.2

%description devel
Header files for libXau library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libXau.

%package static
Summary:	Static libXau library
Summary(pl.UTF-8):	Biblioteka statyczna libXau
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXau-static < 0.2

%description static
Static libXau library.

%description static -l pl.UTF-8
Biblioteka statyczna libXau.

%prep
%setup -q -n libXau-%{version}

# support __libmansuffix__ with "x" suffix (per FHS 2.3)
%{__sed} -i -e 's,^\.so man__libmansuffix__/,.so man3/,' man/*.man

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXau.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXau.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXau.so
%{_libdir}/libXau.la
%{_includedir}/X11/Xauth.h
%{_pkgconfigdir}/xau.pc
%{_mandir}/man3/Xau*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXau.a
