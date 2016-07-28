Name:       crda
Summary:    Central regulatory domain agent for 802.11 wireless networking
Version:    3.18
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

%package devel
Summary:    Header files for use with libreg. 
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
Header files to make use of libreg for accessing regulatory info.


%prep
%setup -q -n %{name}-%{version}/crda

%build
# Drop ldconfig as it breaks the build in OBS. Also we need this only in package install time
# which is handled by %post
sed -i '/$(Q)ldconfig/d' Makefile
PUBKEY_DIR=%{_libdir}/crda/pubkeys/ RUNTIME_PUBKEY_DIR=%{_libdir}/crda/pubkeys/ make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
/lib/udev/rules.d/85-regulatory.rules
/sbin/crda
/sbin/regdbdump
%{_libdir}/libreg.so
%{_mandir}/man8/crda.8.gz
%{_mandir}/man8/regdbdump.8.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/reglib/nl80211.h
%{_includedir}/reglib/regdb.h
%{_includedir}/reglib/reglib.h

