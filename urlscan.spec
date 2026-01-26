Name:           urlscan
Version:        1.0.8
Release:        1
Summary:        Extract and browse the URLs contained in an email (urlview replacement)
License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        https://github.com/firecat53/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source1:        muttrc

BuildArch:      noarch

BuildSystem:  python

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(hatchling)
BuildRequires:  python%{pyver}dist(hatch-vcs)

Requires:       python%{pyver}dist(urwid)

%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.

%files
%doc LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{python_sitelib}/*
