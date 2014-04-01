%define _bindir /opt/ruby_2.1.1/bin
%global gemdir /opt/ruby_2.1.1/lib64/ruby/gems/2.1.0
%global geminstdir %{gemdir}/gems/bundler-1.6.0
%global gemname bundler

Name:           rbenv-ruby_2.1.1-bundler
Version:        1.6.0
Release:        1%{?dist}
Summary:        The best way to manage your application's dependencies        

Group:         	Development/Languages 
License:     	MIT   
URL:            https://github.com/ggershoni/offline-rbenv-ruby_2.1.1-bundler-rpm
Source0:       	bundler-1.6.0.gem 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  rbenv-ruby_2.1.1
Requires:       rbenv-ruby_2.1.1

%description
Bundler manages an application's dependencies through its entire life, across
many machines, systematically and repeatably

%prep
%setup -q -c -T
mkdir -p .%{gemdir}
eval "$(rbenv init -)"
rbenv shell 2.1.1
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{_sourcedir}/bundler-1.6.0.gem


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{gemdir}
cp -pa .%{gemdir}/* $RPM_BUILD_ROOT/%{gemdir}/

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp -pa .%{_bindir}/* $RPM_BUILD_ROOT/%{_bindir}/

find $RPM_BUILD_ROOT/%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf $rpm_build_root


%files
%dir %{geminstdir}
%{geminstdir}
%{_bindir}/bundle
%{_bindir}/bundler
%{gemdir}/doc
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Tue Apr 01 2014 Haani Niyaz <haani.niyaz@gmail.com> - 1.6.0-1
- Initial package

