Name:		texlive-zebra-goodies
Version:	51554
Release:	1
Summary:	A collection of handy macros for paper writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zebra-goodies
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zebra-goodies.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zebra-goodies.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zebra-goodies.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers a collection of macros to help in the
process of writing a paper. You may add comments, todo notes,
etc. during revision, in a colourful way. The package also
summarizes the inserted notes at the end of the document. There
are some predefined note commands as well as a way of defining
new ones to suit the user's needs. You may safely remove this
package once the paper is finished. This package depends on the
following other LaTeX packages: kvoptions, manfnt, marginnote,
tikzpagenodes, xcolor, and, optionally, microtype. Note:
"zebra" is the name of the package author's lab.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zebra-goodies
%{_texmfdistdir}/tex/latex/zebra-goodies
%doc %{_texmfdistdir}/doc/latex/zebra-goodies

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
