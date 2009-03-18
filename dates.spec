Summary:	Tiny GNOME datebook application
Summary(pl.UTF-8):	Mała aplikacja kalendarza dla GNOME
Name:		dates
Version:	0.4.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://pimlico-project.org/sources/dates/%{name}-%{version}.tar.gz
# Source0-md5:	3f6740c2225344238ea6cb3ca621ae45
URL:		http://pimlico-project.org/dates.html
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Obsoletes:	dates-devel <= 0.4.3
Obsoletes:	dates-static <= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dates is a small, lightweight calendar, featuring an innovative,
unified, zooming view and is designed primarily for use on hand-held
devices. It is available in several flavours; a vanilla GTK+ user
interface, a version for the Nokia 770/N800 Maemo platform and a
version for OpenMoko devices.

%description -l pl.UTF-8
Dates to mały, lekki kalendarz cechujący się innowacyjnym,
ujednoliconym, powiększanym widokiem; jest zaprojektowany głównie do
używania na urządzeniach przenośnych. Jest dostępny w kilku odmianach;
z czystym interfejsen GTK+, w wersji dla platformy Nokia 770/N800
Maemo oraz dla urządzeń OpenMoko.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dates
%{_datadir}/dates/oh-about-logo.png
%{_desktopdir}/dates.desktop
%{_iconsdir}/hicolor/16x16/apps/dates.png
%{_iconsdir}/hicolor/22x22/apps/dates.png
%{_iconsdir}/hicolor/24x24/apps/dates.png
#%{_iconsdir}/hicolor/26x26/apps/dates.png
%{_iconsdir}/hicolor/32x32/apps/dates.png
%{_iconsdir}/hicolor/48x48/apps/dates.png
%{_iconsdir}/hicolor/64x64/apps/dates.png
%{_iconsdir}/hicolor/scalable/apps/dates.svg
%{_mandir}/man1/dates.1*
