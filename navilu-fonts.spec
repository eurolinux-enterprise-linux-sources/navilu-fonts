%global fontname navilu
%global fontconf 67-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        1.2
Release:        2%{?dist}
Summary:        Free Kannada opentype sans-serif font

Group:          User Interface/X
License:        OFL
URL:            https://github.com/aravindavk/Navilu
Source0:         http://cloud.github.com/downloads/aravindavk/Navilu/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Source1: 67-navilu.conf


%description
This package provides a free Kannada sans-serif opentype font.


%prep
%setup -q -n %{fontname}-%{version} 

%build
make

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYING README


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Pravin Satpute <psatpute@redhat.com> - 1.2-1
- Resolves bug 842960

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Pravin Satpute <psatpute@redhat.com> - 1.1-1
- Initial build

