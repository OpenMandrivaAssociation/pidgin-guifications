%define version 2.16
%define release %mkrel 8
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




%changelog
* Fri Sep 16 2011 Götz Waschk <waschk@mandriva.org> 2.16-8mdv2012.0
+ Revision: 699959
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.16-7mdv2011.0
+ Revision: 441824
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 2.16-6mdv2009.1
+ Revision: 350211
- 2009.1 rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.16-5mdv2009.0
+ Revision: 259034
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.16-4mdv2009.0
+ Revision: 246942
- rebuild

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.16-2mdv2008.1
+ Revision: 166524
- fix bogus deps

* Tue Jan 08 2008 Götz Waschk <waschk@mandriva.org> 2.16-1mdv2008.1
+ Revision: 146627
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 2.14-2mdv2008.0
+ Revision: 95065
- Rebuild against pidgin 2.2.1

* Sun Jun 03 2007 Götz Waschk <waschk@mandriva.org> 2.14-1mdv2008.0
+ Revision: 34952
- new version

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 2.13-0.beta7.1mdv2008.0
+ Revision: 20633
- new version
- rename

