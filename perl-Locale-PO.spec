%define upstream_name Locale-PO
%define upstream_version 0.27

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        2
Summary:        Perl module for manipulating .po entries from GNU gettext
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Locale-PO/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CO/COSIMO/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
#-------------------------------------------------------

%description
This module simplifies management of GNU gettext .po files and is an
alternative to using emacs po-mode. It provides an object-oriented
interface in which each entry in a .po file is a Locale::PO object.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make 


%check
%make test

%install
%makeinstall_std
