Name:       crda
Summary:    Central regulatory domain agent for 802.11 wireless networking
Version:    1.1.3
Release:    1
Group:      System/Networking
License:    ISC
URL:        http://wireless.kernel.org/en/developers/Regulatory/
Source0:    %{name}-%{version}.tar.bz2
Requires:   udev
Requires:   iw
Requires:   wireless-regdb
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  python
BuildRequires:  python-M2Crypto
BuildRequires:  wireless-regdb

%description
CRDA acts as the udev helper for communication between the kernel
and userspace for regulatory compliance. It relies on nl80211
for communication. CRDA is intended to be run only through udev
communication from the kernel.


%prep
%setup -q -n %{name}-%{version}/crda

%build
PUBKEY_DIR=%{_libdir}/crda/pubkeys/ RUNTIME_PUBKEY_DIR=%{_libdir}/crda/pubkeys/ make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz

