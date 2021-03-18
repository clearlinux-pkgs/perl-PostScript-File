#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PostScript-File
Version  : 2.23
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/C/CJ/CJM/PostScript-File-2.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CJ/CJM/PostScript-File-2.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpostscript-file-perl/libpostscript-file-perl_2.23+dfsg-1.debian.tar.xz
Summary  : 'Class for creating Adobe PostScript files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PostScript-File-license = %{version}-%{release}
Requires: perl-PostScript-File-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
PostScript::File version 2.23, released October 10, 2015
This module produces the outline for an Adobe PostScript file. It provides
convenient routines for writing PostScript directly, including reporting
PostScript errors and debugging support.  Although it may be used independently,
the functions provided are also suitable for use in other modules.  See one of
these modules for a top-level object.

%package dev
Summary: dev components for the perl-PostScript-File package.
Group: Development
Provides: perl-PostScript-File-devel = %{version}-%{release}
Requires: perl-PostScript-File = %{version}-%{release}

%description dev
dev components for the perl-PostScript-File package.


%package license
Summary: license components for the perl-PostScript-File package.
Group: Default

%description license
license components for the perl-PostScript-File package.


%package perl
Summary: perl components for the perl-PostScript-File package.
Group: Default
Requires: perl-PostScript-File = %{version}-%{release}

%description perl
perl components for the perl-PostScript-File package.


%prep
%setup -q -n PostScript-File-2.23
cd %{_builddir}
tar xf %{_sourcedir}/libpostscript-file-perl_2.23+dfsg-1.debian.tar.xz
cd %{_builddir}/PostScript-File-2.23
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PostScript-File-2.23/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PostScript-File
cp %{_builddir}/PostScript-File-2.23/LICENSE %{buildroot}/usr/share/package-licenses/perl-PostScript-File/949fcaa7eab875288aa1c07088df9bb3d692b9c2
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PostScript::File.3
/usr/share/man/man3/PostScript::File::Functions.3
/usr/share/man/man3/PostScript::File::Metrics.3
/usr/share/man/man3/PostScript::File::Metrics::Loader.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PostScript-File/949fcaa7eab875288aa1c07088df9bb3d692b9c2

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Functions.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/Loader.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Courier.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Courier/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Courier/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Courier/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Helvetica.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Helvetica/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Helvetica/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Helvetica/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Times/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Times/BoldItalic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Times/Italic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/cp1252/Times/Roman.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Courier.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Courier/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Courier/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Courier/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Helvetica.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Helvetica/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Helvetica/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Helvetica/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Times/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Times/BoldItalic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Times/Italic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/iso_8859_1/Times/Roman.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Courier.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Courier/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Courier/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Courier/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Helvetica.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Helvetica/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Helvetica/BoldOblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Helvetica/Oblique.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Times/Bold.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Times/BoldItalic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Times/Italic.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/std/Times/Roman.pm
/usr/lib/perl5/vendor_perl/5.32.1/PostScript/File/Metrics/sym/Symbol.pm
