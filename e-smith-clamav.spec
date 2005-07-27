Summary: e-smith module to configure clamav
%define name e-smith-clamav
Name: %{name}
%define version 1.1.0
%define release 05
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: clamav >= 0.83
Requires: clamd >= 0.83
Requires: clamav-db
BuildRequires: e-smith-devtools

%description
e-smith server enhancement to configure and run clamd and
freshclam

%changelog
* Wed Jul 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-05]
- Exclude /proc, /sys and /usr/share/doc from scans
  [SF: 1243741, 1243831]
- Run freshclam with --quiet instead of --verbose [SF: 1245602]

* Fri Jul 22 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-04]
- Fix typo in en-us lexicon. [SF: 1242585]

* Mon May 30 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-03]
- Fix last-updated section and labels [Gordon: SF-1200428]

* Tue May 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-02]
- Add clamav-update event directory.
- Modify some of the panel code to avoid logging of multiple db property
  transactions.

* Fri May 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr06]
- Read the timestamp of the clamav database files in the panel
  to show the last updated time [SF:1200428]
- Change /sbin/e-smith/freshclam-update-ok to /bin/sh, with no
  content. 
- TODO: make the update mails configurable

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr05]
- And hide the sections

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr04]
- Fix up section bars

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr03]
- Removed the qmailscan_integration part of the panel
- Removed the database mirror select box. Anyone who isn't
  satisfied with using db.local.clamav.net can set the hostname
  in the database directly.
- Hid the updates and proxy sections, based on 
  $clamav{ShowProxySection} and $clamav{ShowUpdatesSection}
  - Panel looks rather bare now
- Read the last updated date from $clamav{SignaturesUpdated}
- Modified /sbin/e-smith/freshclam-update-ok to set the above value
- Morphed /etc/clamscan template into /sbin/e-smith/clamscan,
  which can read the db directly.

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr02]
- Use db.local.clamav.net by default (rather than db.us).

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-01gr01]
- Bump version to 1.1.0-01gr01 to upgrade over Shad's 1.0.0
- Roll new tarball after major merge of Shad's work.

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [0.0.1-06gr02]
- Cleaned up patch and startup symlinks

* Fri May 6 2005 Gordon Rowell <gordonr@gormand.com.au>
- [0.0.1-06gr01]
- Merge in Shad Lords' e-smith-spamassassin work (based in part
  on work from Damien Curtain) and panel
- Moved freshclam run script options to database defaults
- Created /sbin/e-smith/freshclam-update-{failed,ok}

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-06]
- Add missing log directories.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-05]
- Don't start freshclam or clamd until after bootstrap-console.
- Move all symlink creation into createlinks script.

* Mon Mar 21 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-04]
- Fix data directory in freshclam configuration.

* Fri Feb 18 2005 Charlie Brady <charlieb@e-smith.com> 0.0.1-03
- Config fixes for clamav-0.83

* Wed Feb 09 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-02]
- Add Requires headers for clamd and clamav-db.

* Wed Feb 09 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-01]
- Initial

%prep
%setup

%build
perl createlinks
touch root/var/service/freshclam/down
touch root/var/service/clamd/down
mkdir -p root/var/log/clamd root/var/log/freshclam

%pre

%post

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  --file /var/service/freshclam/run 'attr(0755,root,root)' \
  --file /var/service/freshclam/log/run 'attr(0755,root,root)' \
  --dir /var/log/freshclam 'attr(2750,smelog,smelog)' \
  --file /var/service/clamd/run 'attr(0755,root,root)' \
  --file /var/service/clamd/log/run 'attr(0755,root,root)' \
  --dir /var/log/clamd 'attr(2750,smelog,smelog)' \
  --file /sbin/e-smith/freshclam-update-failed 'attr(0755,root,root)' \
  --file /sbin/e-smith/freshclam-update-ok 'attr(0755,root,root)' \
  --file /sbin/e-smith/clamscan 'attr(0755,root,root)' \
  > %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
