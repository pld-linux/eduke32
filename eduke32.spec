# TODO
# - http://wiki.eduke32.com/wiki/Building_EDuke32_on_Linux
%define		snap	20090131
%define		patch	20090313
%define		rel		0.2
Summary:	Duke Nukem 3D
Name:		eduke32
Version:	1.5.0
Release:	0.%{patch}.%{rel}
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dukeworld.duke4.net/eduke32/source_code/%{name}_src_%{snap}.zip
# Source0-md5:	cf5eb51de024f28e8b24aae2702d459e
Source1:	http://dukeworld.duke4.net/eduke32/source_code/%{name}_src_%{patch}.diff
# Source1-md5:	fd9fa13146c9a31b2eb709aff93a4afa
Patch0:		make.patch
URL:		http://www.eduke32.com/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	nasm
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
EDuke32 is a port of the classic 3D Realms game Duke Nukem 3D (or
Duke3D for short) to Windows, Linux and OSX. EDuke32 adds many new
convenient features and modernizations for casual players and many
editing features and scripting extensions for mod authors.

EDuke32 screams cool so loud you'll think Bruce Dickinson got uppercut
in the balls by Freddy Krueger. It even comes with Mapster32, an
enhanced version of that good ol' Build editor you remember messing
around with when you were a kid.

EDuke32 requires a copy of Duke Nukem 3D to run.

%description -l pl.UTF-8
Duke Nukem 3D.

Aby uruchomić grę wymagane są pliki z Atomic Edition.

%prep
%setup -q -n %{name}_src_%{snap}
%{__patch} -p1 < %{SOURCE1}
%patch0 -p1

%{__sed} -i -e 's,\r$,,' *.sample
mv duke3d.def.sample duke3d.def
mv enhance.con.sample enhance.con

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	STRIP=echo \
	PRETTY_OUTPUT=0 \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
install -p eduke32 mapster32 $RPM_BUILD_ROOT%{_bindir}
#cp -a *.def *.con $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc buildlic.txt
%attr(755,root,root) %{_bindir}/eduke32
%attr(755,root,root) %{_bindir}/mapster32
%{_appdir}
