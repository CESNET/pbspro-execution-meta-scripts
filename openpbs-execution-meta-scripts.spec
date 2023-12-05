Name:    openpbs-execution-meta-scripts
Version: 1.0
Release: 8
Summary: openpbs-execution-meta-scripts

License: Public Domain
Source0: openpbs-execution-meta-scripts-%{version}.tar.gz

Requires: openpbs-execution

%define debug_packages %{nil}
%define debug_package %{nil} 

%description
openpbs-execution-meta-scripts

%prep
%setup

%build

%install
mkdir -p %{buildroot}/etc/cron.d/
mkdir -p %{buildroot}/etc/cron.daily/
mkdir -p %{buildroot}/var/spool/pbs/mom_scripts/
cp %{_builddir}/openpbs-execution-meta-scripts-%{version}/etc/* %{buildroot}/etc -R
cp %{_builddir}/openpbs-execution-meta-scripts-%{version}/var/spool/pbs/mom_scripts/* %{buildroot}/var/spool/pbs/mom_scripts/ -R

%post
chmod 644 /etc/cron.d/openpbs-execution-meta
chmod 755 /etc/cron.daily/openpbs-execution-meta
service crond reload

%files
/*


%changelog
