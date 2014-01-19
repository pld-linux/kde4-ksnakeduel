%define		_state		stable
%define		orgname		ksnakeduel
%define		qtver		4.8.0

Summary:	Knakeduel
Name:		kde4-%{orgname}
Version:	4.12.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3075cff7f8633d5e84a1ae4346422ed7
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksnakeduel

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang ktron	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ktron.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdesnake
%attr(755,root,root) %{_bindir}/ktron
%{_desktopdir}/kde4/kdesnake.desktop
%{_desktopdir}/kde4/ktron.desktop
%{_datadir}/apps/ktron
%{_datadir}/config.kcfg/ktron.kcfg
%{_datadir}/config/ktron.knsrc
%{_iconsdir}/*/*/apps/kdesnake.png
%{_iconsdir}/*/*/apps/ktron.png
