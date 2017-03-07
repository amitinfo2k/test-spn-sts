Name: dummy
Version:  %{version}
Release:  %{release}%{?dist}
Summary:  dummy rpm packg

License:  GPL
URL:   None
Source:  dummy.tar

%description
dummy rpm image

%prep
%setup -n dummy

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tmp/dummy
cp -R * $RPM_BUILD_ROOT/tmp/dummy

%file
/opt/

%clean
rm -rf $RPM_BUILD_ROOT
