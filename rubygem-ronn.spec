%define oname ronn

Name:       rubygem-%{oname}
Version:    0.7.3
Release:    2
Summary:    Builds manuals
Group:      Development/Ruby
License:    MIT
URL:        https://rtomayko.github.com/ronn
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(hpricot) >= 0.8.2
Requires:   rubygem(rdiscount) >= 1.5.8
Requires:   rubygem(mustache) >= 0.7.0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Builds manuals

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/ronn
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/config.ru
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/man/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/AUTHORS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/INSTALLING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%{ruby_gemdir}/gems/%{oname}-%{version}/ronn.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 592941
- import rubygem-ronn

