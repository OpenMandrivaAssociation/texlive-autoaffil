%global tl_name autoaffil
%global tl_revision 79311

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Automatic deduplicated affiliation numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/autoaffil
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/autoaffil.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the author and affiliation layout style common in
physics and related fields. All authors appear in a single block with
superscript numbers linking each name to a list of affiliations printed
below. This is the style native to revtex4-2 with the superscriptaddress
option, and is familiar from journals such as Physical Review Letters.
The package brings this style to the standard article class and
compatible classes, without requiring a specialised document class.

