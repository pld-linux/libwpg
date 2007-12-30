Summary:	Library for importing and converting Corel WordPerfect(tm) Graphics images
Name:		libwpg
Version:	0.1.2
Release:	0.1
License:	LGPL v2+
Group:		Libraries
URL:		http://libwpg.sourceforge.net/
Source0:	http://dl.sourceforge.net/libwpg/%{name}-%{version}.tar.gz
# Source0-md5:	317cee27f380c394c6e4eec02d45cab8
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.8
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwpg project is a collection of library and tools to work with
graphics in WPG (WordPerfect Graphics) format. WPG is the format used
among others in Corel sofware, such as WordPerfect(tm) and
Presentations(tm).

%package devel
Summary:	Header files for libwpg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwpg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpg-devel >= 0.8

%description devel
Header files for libwpg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwpg.

%package static
Summary:	Static libwpg library
Summary(pl):	Statyczna biblioteka libwpg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwpg library.

%description static -l pl.UTF-8
Statyczna biblioteka libwpg.

%package tools
Summary:	Tools to transform WordPerfect Graphics into other formats
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Graphics (WPG) into other formats.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libwpg*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpg2raw
%attr(755,root,root) %{_bindir}/wpg2svg
%attr(755,root,root) %{_bindir}/wpg2svgbatch.pl
