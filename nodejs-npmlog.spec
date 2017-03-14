%{?scl:%scl_package nodejs-npmlog}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-npmlog
Version:        3.1.2
Release:        1%{?dist}
Summary:        Logger for npm
BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
License:        ISC
URL:            https://github.com/isaacs/npmlog
Source0:        https://registry.npmjs.org/npmlog/-/npmlog-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
The logger utility that npm uses.

This logger is very basic. It does the logging for npm. It supports custom
levels and colored output.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npmlog
cp -pr package.json log.js %{buildroot}%{nodejs_sitelib}/npmlog

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/npmlog
%doc LICENSE README.md

%changelog
* Thu Sep 22 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.2-1
- Updated with script

* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.2-1
- Updated with script

* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.4-1
- Updated with script

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-3
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-1
- Rebase to new upstream release

* Thu Jul 23 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-2
- Remove macro that handles deps

* Thu Jan 08 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-1
- New upstream release 0.1.1

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.6-1
- New upstream release 0.0.6

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.4-2
- replace provides and requires with macro

* Sat Jul 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- new upstream release 0.0.4

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- new upstream release 0.0.3

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-5
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-4
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.2-4
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-2
- add missing build section
- minor description improvement

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-1
- initial package generated by npm2rpm
