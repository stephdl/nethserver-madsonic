%define name nethserver-madsonic
%define version 6.2.9040
%define release 1
Summary: madsonic is a helpdesk system
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Distribution: Nethserver
License: GNU GPL version 3
Source: smeserver-madsonic-%{version}.tar.gz
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-buildroot
BuildRequires: nethserver-devtools
Requires: madsonic 
#Requires: ffmpeg
Requires: java-1.7.0-openjdk >= 1.7
AutoReqProv: no

%description
madsonic is an application adapted as a contrib for nethserver

%changelog

* Mon Jun 16 2014 JP Pialasse <tests@pialasse.com> 5.0.3761-1.sme
- initial import to SME9 contribs

* Wed Nov 20 2013  CONTRIB MAKER <tests@pialasse.com> 5.0.3760-2.sme
- initial release
- builds from unchanged .tar.gz 

%pre
grep '^madsonic:' /etc/passwd > /dev/null || \
/usr/sbin/useradd -c "madsonic" -M -d /usr/share/madsonic   -s /bin/bash madsonic

%prep
%setup

%build
%{makedocs}
perl createlinks
%{__mkdir} -p $RPM_BUILD_ROOT/var/lib/madsonic

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
  --dir /var/lib/madsonic 'attr(0755,madsonic,madsonic)' \
     > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

