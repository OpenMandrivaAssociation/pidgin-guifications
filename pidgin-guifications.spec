%define version 2.16
%define release %mkrel 4
%define fname %name-%version
%define pidgin_version 2.2.1

Summary:	MSN Style Popup for Pidgin
Name:		pidgin-guifications
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
URL:		http://plugins.guifications.org/trac/wiki/Guifications
Source:		http://downloads.guifications.org/plugins//Guifications2/%{fname}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	gtk+2-devel
BuildRequires:	perl-XML-Parser
Requires: pidgin >= %{pidgin_version}
Provides: gaim-guifications
Obsoletes: gaim-guifications

%description
Guifications is a Pidgin plugin that displays msn style "toaster" popups
in a user defined corner of the screen. It's highly configurable,
easy to use, and has theme support.


%prep
%setup -q -n %{fname}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang guifications
# remove files not bundled
rm -f %{buildroot}%{_libdir}/*/*.la

%clean
rm -rf %{buildroot}

%files -f guifications.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/pidgin/*.so
%{_datadir}/pixmaps/pidgin/*


