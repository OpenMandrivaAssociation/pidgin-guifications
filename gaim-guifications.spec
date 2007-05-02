%define version 2.13
%define pre beta6
%define release %mkrel 0.%pre.1
%define fname %name-%version%pre
%define gaim_version 1:2.0.0

Summary:	MSN Style Popup for Gaim
Name:		gaim-guifications
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
URL:		http://gaim.guifications.org/trac/wiki/Guifications
Source:		http://downloads.guifications.org/gaim-plugins//Guifications2/%{fname}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgaim-devel >= %{gaim_version}
BuildRequires:	gtk+2-devel
BuildRequires:	perl-XML-Parser
Requires:	gaim >= %{gaim_version}

%description
Guifications is a Gaim plugin that displays msn style "toaster" popups
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
rm -f %{buildroot}%{_libdir}/gaim/*.la

%clean
rm -rf %{buildroot}

%files -f guifications.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/gaim/*.so
%{_datadir}/pixmaps/gaim/*


