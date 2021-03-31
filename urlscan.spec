Name:           urlscan
Version:        0.9.6
Release:        1
Summary:        Extract and browse the URLs contained in an email (urlview replacement)

License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        https://github.com/firecat53/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source1:        muttrc

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Requires:       python3dist(urwid)

%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.

%prep
%autosetup -p0

%build
%py_build

%install
%py_install

%files
%license COPYING
%doc README.rst COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python_sitelib}/*
