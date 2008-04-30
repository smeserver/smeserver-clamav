Summary: SME Server module to configure clamav
%define name smeserver-clamav
Name: %{name}
%define version 1.2.0
%define release 24
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: clamav >= 0.93
Requires: clamd >= 0.93
Requires: clamav-db
Requires: e-smith-formmagick >= 1.4.0-12
Provides: e-smith-clamav
Obsoletes: e-smith-clamav
Obsoletes: clamav-es
Obsoletes: clamav-es-libs
BuildRequires: e-smith-devtools

%description
e-smith server enhancement to configure and run clamd and
freshclam

%changelog
* Wed Apr 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-24
- Remove /etc/cron.d/clamav causing second instance of clamav to run [SME: 4266]
  which was caused by a partial migration of the template fragments [SME: 1047]

* Sun Apr 27 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-23
- Add common <base> tags to e-smith-formmagick's general [SME: 4288]

* Fri Apr 25 2008 Charlie Brady <charlie_brady@mitel.com> 1.2.0-22
- Add Obsoletes headers to force removal of clamav-es and
  clamav-es-libs. [SME 4167]

* Fri Apr 18 2008 Shad L. Lords <slords@mail.com> 1.2.0-21
- Update defaults for clamav 0.93 [SME: 4223]

* Fri Apr 18 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-20
- Move cron template from cron.d to crontab [SME: 1047]

* Tue Mar 18 2008 Shad L. Lords <slords@mail.com> 1.2.0-19
- Fix clamav version string [SME: 4060]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 1.2.0-18
- Remove <base> tags now in general [SME: 3915]

* Sun Feb 10 2008 Stephen Noble <support@dungog.net> 1.2.0-17
- Remove duplicate <base> entries [SME: 3890]

* Mon Jan 07 2008 Stephen Noble <support@dungog.net> 1.2.0-16
- Cosmetic removal of word entire on panel [SME: 3483]

* Thu Sep 06 2007  Filippo Carletti <filippo.carletti@gmail.com> 1.2.0-15
- Fix freshclam.conf permissions [SME: 3375]

* Fri Jun 08 2007 Charlie Brady <charlie_brady@mitel.com> 1.2.0-14
- Use full paths in update-failed script - tai64nlocal was not
  being found in $PATH. [SME: 1686]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Wed Apr 18 2007 Shad L. Lords <slords@mail.com> 1.2.0-13
- Up memory limit for clamd again [SME: 2743]

* Wed Feb 21 2007 Shad L. Lords <slords@mail.com> 1.2.0-12
- Up memory limit for clamd [SME: 2528]

* Wed Feb 14 2007 Shad L. Lords <slords@mail.com> 1.2.0-11
- Update for clamav v0.90 [SME: 2508]

* Tue Feb 13 2007 Shad L. Lords <slords@mail.com> 1.2.0-10
- Improve algorithm for displaying errors [SME: 1686]

* Mon Feb 12 2007 Shad L. Lords <slords@mail.com> 1.2.0-9
- Improve sed expression for freshclam failures [SME: 1686]

* Mon Feb 12 2007 Shad L. Lords <slords@mail.com> 1.2.0-8
- Allow clamav to read freshclam update log [SME: 1686]

* Fri Jan 26 2007 Shad L. Lords <slords@mail.com> 1.2.0-7
- Provide more feedback on freshclam events [SME: 1686]

* Wed Dec 13 2006 Federico Simoncelli <federico.simoncelli@gmail.com> 1.2.0-6
- Added support for options: max-ratio, no-html, no-mail. [SME: 2024]
- Redirected the stderr output to /var/log/clamd/smeserver-clamscan.log.
  [SME: 2004]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Nov 29 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-04
- Restrict filesystem scan to /home/e-smith/files by default [SME: 2082]

* Sun Aug 27 2006 Charlie Brady <charlieb@e-smith.com> 1.2.0-03
- Fix --exclude arg syntax. [SME: 1889]

* Fri Jun 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-02
- Fix typo in ArchiveBlockEntrypted [SME: 1584]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Tue Mar 14 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-10
- Restart crond in clamav-update so cron notices cron.d/clamav [SME: 966]

* Wed Feb 8 2006 Gavin Weight <gweight@gmail.com> 1.1.2-09
- Added migrate fragment for clamav DatabaseMirror. [SME: 83]

* Fri Jan 27 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-08
- Bump release number to ensure patch is in CVS

* Wed Jan 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-07
- Expand MEMLIMIT in bootstrap-console-save (and don't attempt to
  restart the service there)

* Wed Jan 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-06
- Change back to softlimit -a [SME: 426]

* Wed Jan 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-05
- Set db default for clamd{MemLimit}==80M and use it in the run script
- Expand templates in events rather than run file [SME: 426]

* Mon Oct 17 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-04
- Fix typos in smeserver-clamscan [SF: 1304217]

* Fri Oct 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-03
- Move all L10Ns to smeserver-locale [SF: 1309520]

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-02
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.2-01
- Roll patches to 1.1.1-06
- Add German L10N

* Mon Sep 26 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.1-06
- Exclude /var and all of /usr/share (not just /usr/share/doc) from
  filesystem scan [SF: 1304217]

* Fri Sep 23 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.1-05
- French L10N fixes [SF: 1242586]

* Sat Aug 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.1-04
- French L10N - Merci Didier Rambeau  [SF: 1242586]

* Sat Aug 20 2005 Gordon Rowell <gordonr@gormand.com.au> 1.1.1-03
- Don't scan quarantine area, even if quarantining is disabled [SF: 1245655]

* Fri Aug 19 2005 Charlie Brady <charlieb@e-smith.com> 1.1.1-02
- Add Provides: header, to satisfy any package which requires defunct
  e-smith-clamav.

* Thu Aug 18 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.1-01]
- Package renamed to smeserver-clamav [SF: 1263460]

* Thu Aug 18 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-08sme02]
- Rename /sbin/e-smith/clamscan to smeserver-clamscan [SF: 1263460]

* Thu Aug 18 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-08sme01]
- Disable quarantining by default, add panel toggle [SF: 1245655]

* Tue Aug  9 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.1.0-08]
- Add --move=$clamav{QuarantineDirectory} to clamscan,
  exclude directory from being scanned, add database default 
  and set permissions in spec file [SF: 1245655]

* Thu Aug  4 2005 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-07]
- Remove freshclam runs from clamav crontab template - we
  now run supervised freshclam instance. [SF: 1251944]

* Thu Aug  4 2005 Shad Lords <slords@mail.com>
- [1.1.0-06]
- Include db entry to exclude /proc, /sys and
  /usr/share/doc from scans [SF: 1243741, 1243831]

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
mkdir -p root/var/service/clamd/env
mkdir -p root/var/log/clamd root/var/log/freshclam
mkdir -p root/var/spool/clamav/quarantine

%pre

%post
rm -f /etc/cron.d/clamav

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  --file /var/service/freshclam/run 'attr(0755,root,root)' \
  --file /var/service/freshclam/log/run 'attr(0755,root,root)' \
  --dir /var/log/freshclam 'attr(2750,smelog,clamav)' \
  --file /var/service/clamd/run 'attr(0755,root,root)' \
  --file /var/service/clamd/log/run 'attr(0755,root,root)' \
  --dir /var/log/clamd 'attr(2750,smelog,smelog)' \
  --dir /var/spool/clamav/quarantine 'attr(2750,clamav,clamav)' \
  --file /sbin/e-smith/freshclam-update-failed 'attr(0755,root,root)' \
  --file /sbin/e-smith/freshclam-update-ok 'attr(0755,root,root)' \
  --file /sbin/e-smith/smeserver-clamscan 'attr(0755,root,root)' \
  > %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
