Summary:	Library for importing and converting Corel WordPerfect(TM) Graphics images
Summary(pl.UTF-8):	Biblioteka do importowania i konwersji obrazów Corel WordPerfect Graphics
Name:		libwpg
Version:	0.2.2
Release:	1
License:	MPL v2.0 or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libwpg/%{name}-%{version}.tar.xz
# Source0-md5:	f5c4c22e291e3313891c88b3fe6d565d
URL:		http://libwpg.sourceforge.net/
BuildRequires:	automake >= 1:1.11
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libwpd >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwpg project is a collection of library and tools to work with
graphics in WPG (WordPerfect Graphics) format. WPG is the format used
among others in Corel software, such as WordPerfect(TM) and
Presentations(TM).

%description -l pl.UTF-8
Projekt libwpg to zestaw biblioteki i narzędzi do pracy z obrazami w
formacie WPG (WordPerfect Graphics). WPG to format używany między
innymi w programach firmy Corel, takich jak WordPerfect(TM) i
Presentations(TM).

%package devel
Summary:	Header files for libwpg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwpg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9

%description devel
Header files for libwpg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwpg.

%package static
Summary:	Static libwpg library
Summary(pl.UTF-8):	Statyczna biblioteka libwpg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwpg library.

%description static -l pl.UTF-8
Statyczna biblioteka libwpg.

%package tools
Summary:	Tools to transform WordPerfect Graphics into other formats
Summary(pl.UTF-8):	Narzędzia do konwersji plików z formatu WordPerfect Graphics do innych
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Graphics (WPG) into other formats.

%description tools -l pl.UTF-8
Narzędzia do konwersji plików z formatu WordPerfect Graphics do innych
formatów.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# packages as %doc in -evel
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libwpg-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwpg-0.2.so.2

%files devel
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
%attr(755,root,root) %{_libdir}/libwpg-0.2.so
%{_includedir}/libwpg-0.2
%{_pkgconfigdir}/libwpg-0.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwpg-0.2.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpg2raw
%attr(755,root,root) %{_bindir}/wpg2svg
%attr(755,root,root) %{_bindir}/wpg2svgbatch.pl
