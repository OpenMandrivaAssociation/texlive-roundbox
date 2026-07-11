%global tl_name roundbox
%global tl_revision 29675

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Round boxes in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/roundbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roundbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/roundbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a command \roundbox that can be used, in LaTeX,
for producing boxes, framed with rounded corners.

