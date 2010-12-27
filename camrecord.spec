Summary: Record video from IP cameras
Name: camrecord
Version: 1.0.0
Release: 3.el5
License: GPL
Group: Applications/Multimedia
URL: http://www.stellanetworks.com/software/camrecord
Source1: camrecord
Source2: camrecord.init
Source3: example.conf-dist
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ffmpeg >= 0.6.1, mencoder >= 1.0, curl
BuildArch: noarch

%description
camrecord is a Perl program that records video from IP cameras such as
Axis cameras and TRENDnet cameras. It features robust handling of
network interruptions and camera failures, splitting apart of video
files into four hour blocks, and syslogging of detected problems.


%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_initrddir}
install -d %{buildroot}/%{_sysconfdir}/camrecord
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/camrecord
install -p -m 755 %{SOURCE2} %{buildroot}/%{_initrddir}/camrecord
install -p -m 444 %{SOURCE3} %{buildroot}/%{_sysconfdir}/camrecord/example.conf-dist


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/chkconfig --add camrecord
/sbin/service camrecord condrestart
exit 0


%preun
if [ $1 = 0 ]; then
  /sbin/service camrecord stop > /dev/null 2>&1
  /sbin/chkconfig --del camrecord
fi
exit 0


%files
%defattr(-,root,root,-)
%{_bindir}/camrecord
%{_initrddir}/camrecord
%config %{_sysconfdir}/camrecord/example.conf-dist


%changelog
* Sun Dec 26 2010 Wellie Chao <wchao@microoffice.com> - 
- Initial build.

