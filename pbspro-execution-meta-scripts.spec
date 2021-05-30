Name:    pbspro-execution-meta-scripts
Version: 1.0
Release: 8
Summary: pbspro-execution-meta-scripts

License: Public Domain
Source0: pbspro-execution-meta-scripts-%{version}.tar.gz

Requires: pbspro-execution

%define debug_packages %{nil}
%define debug_package %{nil} 

%description
pbspro-execution-meta-scripts

%prep
%setup

%build

%install
mkdir -p %{buildroot}/etc/cron.d/
mkdir -p %{buildroot}/etc/cron.daily/
mkdir -p %{buildroot}/var/spool/pbs/mom_scripts/
cp %{_builddir}/pbspro-execution-meta-scripts-%{version}/etc/* %{buildroot}/etc -R
cp %{_builddir}/pbspro-execution-meta-scripts-%{version}/var/spool/pbs/mom_scripts/* %{buildroot}/var/spool/pbs/mom_scripts/ -R

%post
chmod 644 /etc/cron.d/pbspro-execution-meta
chmod 755 /etc/cron.daily/pbspro-execution-meta
service crond reload

%files
/*


%changelog
