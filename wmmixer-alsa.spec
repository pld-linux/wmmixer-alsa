Summary:	A hacked version of wmmixer to make it use ALSA
Summary(pl):	Wersja wmmixer przerobiona tak, by u¿ywa³a ALSA
Name:		wmmixer-alsa
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://iznogood.bohemians.org/wmmixer-alsa/%{name}-%{version}.tar.gz
URL:		http://iznogood.bohemians.org/
BuildRequires:	alsa-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A hacked version of wmmixer by Sam Hawker (see README.wmmixer), to
make it use ALSA (Advanced Linux Sound Architecture) in stead of the
OSS sound drivers in the linux kernel. To compile and run this
program, you will need to get alsa-driver and alsa-lib packages.

%description -l pl
Wersja wmmixera autorstwa Sama Hawkera (patrz README.wmmixer),
przerobionaa tak, by u¿ywa³a sterowników ALSA zamiast OSS.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps}
install wmmixer-alsa $RPM_BUILD_ROOT%{_bindir}
install XPM/{icons,wmmixer}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wmmixer-alsa
%{_pixmapsdir}/*
