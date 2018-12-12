%global plugin_name octavia_tempest_plugin
%global service octavia

Name:       python-octavia-tests-golang
Version:    0.1.0
Release:    2%{?dist}
Summary:    Octavia tests golang

License:    ASL 2.0
URL:        http://launchpad.net/octavia/

Source0:    https://tarballs.openstack.org/octavia-tempest-plugin/octavia-tempest-plugin-%{version}.tar.gz
BuildRequires:   golang
BuildRequires:   glibc-static
# NOTE(jpena): we only want to build the package for ppc64le and aarch64
ExcludeArch: x86_64
Provides: python-%{service}-tests-tempest-golang = %{version}-%{release}
Provides: python2-%{service}-tests-tempest-golang = %{version}-%{release}
Provides: python2-octavia-tests-golang = %{version}-%{release}

%description
Golang httpd binary for Octavia tempest tests

%prep
%autosetup -n octavia-tempest-plugin-%{version}

%build
# Generate octavia-tests-httpd binary from httpd.go
pushd %{plugin_name}/contrib/httpd
 go build -ldflags '-linkmode external -extldflags -static' -o %{service}-tests-httpd httpd.go
popd

%install
# Move httpd binary to proper place
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 %{plugin_name}/contrib/httpd/%{service}-tests-httpd %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/%{service}-tests-httpd

%changelog
* Wed Dec 12 2018 Alfredo Moralejo <amoralej@redhat.com> 0.1.0-2
- Add provides to python2 subpackages.
