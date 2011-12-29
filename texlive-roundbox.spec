# revision 17896
# category Package
# catalog-ctan /macros/latex/contrib/roundbox
# catalog-date 2010-04-29 07:59:03 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-roundbox
Version:	0.1
Release:	1
Summary:	Round boxes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/roundbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roundbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/roundbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements \roundbox command that can be used for
producing round boxes in LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/roundbox/roundbox.sty
%doc %{_texmfdistdir}/doc/latex/roundbox/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
