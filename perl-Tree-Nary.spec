%define upstream_name    Tree-Nary
%define upstream_version 1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Tree::Nary - Perl implementation of N-ary search trees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/F/FS/FSORIANO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Tree::Nary class implements N-ary trees (trees of data with any 
number of branches), providing the organizational structure for a tree
(collection) of any number of nodes, but knowing nothing about the specific
type of node used.  It can be used to display hierarchical database entries in
an internal application (the NIS netgroup file is an example of such a
database). It offers the capability to select nodes on the tree, and attachment
points for nodes on the tree. Each attachment point can support multiple child
nodes.

The data field contains the actual data of the node. The next and previous
fields point to the node's siblings (a sibling is another node with the same
parent). The parent field points to the parent of the node, or is undef if the
node is the root of the tree. The children field points to the first child of
the node. The other children are accessed by using the next pointer of each
child.  This module is a translation (albeit not a direct one) from the C
implementation of N-ary trees, available in the GLIB distribution (see SEE
ALSO).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{perl_vendorlib}/Tree/*.pm
%{_mandir}/*/*


%changelog
* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2010.1
+ Revision: 505279
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3-6mdv2010.0
+ Revision: 430609
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2009.0
+ Revision: 258705
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2009.0
+ Revision: 246662
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.3-2mdv2008.1
+ Revision: 166686
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-2mdv2008.0
+ Revision: 87062
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package

