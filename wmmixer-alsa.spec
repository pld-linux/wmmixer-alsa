Summary: A hacked version of wmmixer to make it use ALSA
Name: wmmixer-alsa
Version: 0.5
Release: 1
Source: http://bohemians.org/~iznogood/wmmixer-alsa/%{name}-%{version}.tar.gz
URL: http://iznogood.bohemians.org/
Copyright: GPL
Group: Applications/Sound
Packager: Anders Semb Hermansen <ahermans@vf.telia.no>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A hacked version of wmmixer by Sam Hawker (see README.wmmixer),
to make it use ALSA (Advanced Linux Sound Architecture) in
stead of the OSS sound drivers in the linux kernel. To compile
and run this program, you will need to get alsa-driver and alsa-lib
from alsa.jcu.cz !

%prep
%setup -n %{name}-%{version} 

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m0755 wmmixer-alsa $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(-,root,root) %doc COPYING README README.xamixer
%attr(-,root,root) %{_bindir}/wmmixer-alsa
