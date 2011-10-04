# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.20
# 
# >> macros
# << macros

Name:       crda
Summary:    Central regulatory domain agent for 802.11 wireless networking
Version:    1.1.1
Release:    1
Group:      System/Networking
License:    ISC
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    http://wireless.kernel.org/download/crda/crda-%{version}.tar.bz2
Source100:  crda.yaml
Requires:   udev
Requires:   iw
Requires:   wireless-regdb
BuildRequires:  pkgconfig(libnl-1)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  python
BuildRequires:  m2crypto
BuildRequires:  wireless-regdb


%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz
# >> files
# << files

