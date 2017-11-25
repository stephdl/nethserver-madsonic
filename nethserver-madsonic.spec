%define name nethserver-madsonic
%define version 0.0.11
%define release 1
Summary: madsonic is a helpdesk system
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Distribution: Nethserver
License: GNU GPL version 3
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-buildroot
BuildRequires: nethserver-devtools
Requires: madsonic >= 6.2
Requires: nethserver-httpd nethserver-ibays nethserver-samba
#Requires: ffmpeg
Requires: java-1.7.0-openjdk
AutoReqProv: no

%description
madsonic is an application adapted as a contrib for nethserver

%changelog
* Sat Nov 25 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.11-1.ns6
- Open the TCP port of madsonic to private

* Sat Nov 25 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.10-1.ns6
- handle the multi NIC case for finding the dlna port

* Sun Nov 22 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.9-1.ns6
- find the UDP ports for dlna

* Sun Nov 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.7-1.ns6
- translate the error message for bad user

* Sun Nov 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.5-1.ns6
- the action nethserver-madsonic-finf-dlna-port wait 30 seconds maximum

* Sat Nov 11 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.4-1.ns6
- Find the dlna port and open it in the firewall

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3-1.ns6
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2-1.ns6
- Template expansion on trusted-network

*Tue Mar 14 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1-1
- Release for Nethserver 6

* Mon Jun 16 2014 JP Pialasse <tests@pialasse.com> 5.0.3761-1.sme
- initial import to SME9 contribs

* Wed Nov 20 2013  CONTRIB MAKER <tests@pialasse.com> 5.0.3760-2.sme
- initial release
- builds from unchanged .tar.gz

%pre
if ! getent group madsonic >& /dev/null; then
  groupadd -f -r madsonic
fi
if ! id madsonic >& /dev/null; then
  /usr/sbin/useradd -d /var/madsonic -c "madsonic user" -s /bin/bash -M -r -g madsonic madsonic
fi


%prep
%setup

%build
%{makedocs}
perl createlinks
%{__mkdir} -p root/var/media/artists
%{__mkdir} -p root/var/media/incoming
%{__mkdir} -p root/var/media/podcast
%{__mkdir} -p root/var/media/playlists/import
%{__mkdir} -p 'root/var/media/playlists/export'
%{__mkdir} -p root/var/media/playlists/backup

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
  --dir /var/media/artists 'attr(0755,madsonic,madsonic)' \
  --dir /var/media/incoming 'attr(0755,madsonic,madsonic)' \
  --dir /var/media/podcast 'attr(0755,madsonic,madsonic)' \
  --dir /var/media/playlists 'attr(0755,madsonic,madsonic)' \
  --dir /var/media/playlists/import 'attr(0755,madsonic,madsonic)' \
  --dir '/var/media/playlists/export' 'attr(0755,madsonic,madsonic)' \
  --dir /var/media/playlists/backup 'attr(0755,madsonic,madsonic)' \
     > %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
