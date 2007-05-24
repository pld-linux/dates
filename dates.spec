#
# TODO:
# - dates-devel and dates-static
#
Summary:	tiny GNOME datebook app
Name:		dates
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://pimlico-project.org/sources/dates/%{name}-%{version}.tar.gz
# Source0-md5:	b3e5e32462a2f52f42ec3daea1a55ebd
URL:		http://pimlico-project.org/dates.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gtk+2-devel >= 2:2.10.7
#BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dates is a small, lightweight calendar, featuring an innovative,
unified, zooming view and is designed primarily for use on hand-held
devices. It is available in several flavours; a vanilla GTK+ user
interface, a version for the Nokia 770/N800 Maemo platform and a
version for OpenMoko devices.

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
/sbin/ldconfig
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%scrollkeeper_update_postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgtkdatesview.so.0.0.0
%{_desktopdir}/dates.desktop
%{_iconsdir}/hicolor/48x48/apps/dates.png
%dir %{_datadir}/dates
%{_datadir}/dates/oh-about-logo.png
%{_iconsdir}/hicolor/16x16/apps/dates.png
%{_iconsdir}/hicolor/22x22/apps/dates.png
%{_iconsdir}/hicolor/24x24/apps/dates.png
%{_iconsdir}/hicolor/32x32/apps/dates.png
%{_iconsdir}/hicolor/scalable/apps/dates.svg
%{_mandir}/man1/dates.1*

%if 0
%{_includedir}/gtkdatesview/dates_view.h
%{_libdir}/libgtkdatesview.a
%{_libdir}/libgtkdatesview.la
%{_pkgconfigdir}/libgtkdatesview.pc
%endif
