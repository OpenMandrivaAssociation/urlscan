Name:           urlscan
Version:        1.0.7
Release:        1
Summary:        Extract and browse the URLs contained in an email (urlview replacement)

License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        https://github.com/firecat53/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source1:        muttrc

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{py_ver}dist(setuptools)
BuildRequires:  python%{py_ver}dist(hatchling)
BuildRequires:  python%{py_ver}dist(hatch-vcs)
Requires:       python%{py_ver}dist(urwid)


%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.

%prep
%autosetup

%build
%py_build

%install
%py_install

%files
/usr/share/doc/%{name}/LICENSE
/usr/share/doc/%{name}/README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python_sitelib}/*
