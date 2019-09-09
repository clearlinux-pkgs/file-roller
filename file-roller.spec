#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : file-roller
Version  : 3.32.2
Release  : 15
URL      : https://download.gnome.org/sources/file-roller/3.32/file-roller-3.32.2.tar.xz
Source0  : https://download.gnome.org/sources/file-roller/3.32/file-roller-3.32.2.tar.xz
Summary  : Create and modify archives
Group    : Development/Tools
License  : GPL-2.0
Requires: file-roller-bin = %{version}-%{release}
Requires: file-roller-data = %{version}-%{release}
Requires: file-roller-lib = %{version}-%{release}
Requires: file-roller-libexec = %{version}-%{release}
Requires: file-roller-license = %{version}-%{release}
Requires: file-roller-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : colord
BuildRequires : itstool
BuildRequires : json-glib-dev
BuildRequires : libarchive-dev
BuildRequires : libnotify-dev
BuildRequires : nautilus-dev
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libnautilus-extension)
BuildRequires : pkgconfig(libnotify)

%description
* File Roller *
an archive manager utility for the
GNOME Environment.
* What is it ?

%package bin
Summary: bin components for the file-roller package.
Group: Binaries
Requires: file-roller-data = %{version}-%{release}
Requires: file-roller-libexec = %{version}-%{release}
Requires: file-roller-license = %{version}-%{release}

%description bin
bin components for the file-roller package.


%package data
Summary: data components for the file-roller package.
Group: Data

%description data
data components for the file-roller package.


%package doc
Summary: doc components for the file-roller package.
Group: Documentation

%description doc
doc components for the file-roller package.


%package lib
Summary: lib components for the file-roller package.
Group: Libraries
Requires: file-roller-data = %{version}-%{release}
Requires: file-roller-libexec = %{version}-%{release}
Requires: file-roller-license = %{version}-%{release}

%description lib
lib components for the file-roller package.


%package libexec
Summary: libexec components for the file-roller package.
Group: Default
Requires: file-roller-license = %{version}-%{release}

%description libexec
libexec components for the file-roller package.


%package license
Summary: license components for the file-roller package.
Group: Default

%description license
license components for the file-roller package.


%package locales
Summary: locales components for the file-roller package.
Group: Default

%description locales
locales components for the file-roller package.


%prep
%setup -q -n file-roller-3.32.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568072696
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/file-roller
cp COPYING %{buildroot}/usr/share/package-licenses/file-roller/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang file-roller

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/file-roller

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.FileRoller.desktop
/usr/share/dbus-1/services/org.gnome.FileRoller.ArchiveManager1.service
/usr/share/dbus-1/services/org.gnome.FileRoller.service
/usr/share/file-roller/packages.match
/usr/share/glib-2.0/schemas/org.gnome.FileRoller.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.ArchiveManager.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.ArchiveManager-symbolic.svg
/usr/share/metainfo/org.gnome.FileRoller.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/file-roller/archive-create.page
/usr/share/help/C/file-roller/archive-edit.page
/usr/share/help/C/file-roller/archive-extract-advanced-options.page
/usr/share/help/C/file-roller/archive-extract.page
/usr/share/help/C/file-roller/archive-open.page
/usr/share/help/C/file-roller/archive-view.page
/usr/share/help/C/file-roller/figures/file-roller-icon.png
/usr/share/help/C/file-roller/index.page
/usr/share/help/C/file-roller/introduction.page
/usr/share/help/C/file-roller/keyboard-shortcuts.page
/usr/share/help/C/file-roller/legal.xml
/usr/share/help/C/file-roller/password-protection.page
/usr/share/help/C/file-roller/supported-formats.page
/usr/share/help/C/file-roller/test-integrity.page
/usr/share/help/C/file-roller/troubleshooting-archive-open.page
/usr/share/help/C/file-roller/troubleshooting-password.page
/usr/share/help/ca/file-roller/archive-create.page
/usr/share/help/ca/file-roller/archive-edit.page
/usr/share/help/ca/file-roller/archive-extract-advanced-options.page
/usr/share/help/ca/file-roller/archive-extract.page
/usr/share/help/ca/file-roller/archive-open.page
/usr/share/help/ca/file-roller/archive-view.page
/usr/share/help/ca/file-roller/figures/file-roller-icon.png
/usr/share/help/ca/file-roller/index.page
/usr/share/help/ca/file-roller/introduction.page
/usr/share/help/ca/file-roller/keyboard-shortcuts.page
/usr/share/help/ca/file-roller/legal.xml
/usr/share/help/ca/file-roller/password-protection.page
/usr/share/help/ca/file-roller/supported-formats.page
/usr/share/help/ca/file-roller/test-integrity.page
/usr/share/help/ca/file-roller/troubleshooting-archive-open.page
/usr/share/help/ca/file-roller/troubleshooting-password.page
/usr/share/help/cs/file-roller/archive-create.page
/usr/share/help/cs/file-roller/archive-edit.page
/usr/share/help/cs/file-roller/archive-extract-advanced-options.page
/usr/share/help/cs/file-roller/archive-extract.page
/usr/share/help/cs/file-roller/archive-open.page
/usr/share/help/cs/file-roller/archive-view.page
/usr/share/help/cs/file-roller/figures/file-roller-icon.png
/usr/share/help/cs/file-roller/index.page
/usr/share/help/cs/file-roller/introduction.page
/usr/share/help/cs/file-roller/keyboard-shortcuts.page
/usr/share/help/cs/file-roller/legal.xml
/usr/share/help/cs/file-roller/password-protection.page
/usr/share/help/cs/file-roller/supported-formats.page
/usr/share/help/cs/file-roller/test-integrity.page
/usr/share/help/cs/file-roller/troubleshooting-archive-open.page
/usr/share/help/cs/file-roller/troubleshooting-password.page
/usr/share/help/da/file-roller/archive-create.page
/usr/share/help/da/file-roller/archive-edit.page
/usr/share/help/da/file-roller/archive-extract-advanced-options.page
/usr/share/help/da/file-roller/archive-extract.page
/usr/share/help/da/file-roller/archive-open.page
/usr/share/help/da/file-roller/archive-view.page
/usr/share/help/da/file-roller/figures/file-roller-icon.png
/usr/share/help/da/file-roller/index.page
/usr/share/help/da/file-roller/introduction.page
/usr/share/help/da/file-roller/keyboard-shortcuts.page
/usr/share/help/da/file-roller/legal.xml
/usr/share/help/da/file-roller/password-protection.page
/usr/share/help/da/file-roller/supported-formats.page
/usr/share/help/da/file-roller/test-integrity.page
/usr/share/help/da/file-roller/troubleshooting-archive-open.page
/usr/share/help/da/file-roller/troubleshooting-password.page
/usr/share/help/de/file-roller/archive-create.page
/usr/share/help/de/file-roller/archive-edit.page
/usr/share/help/de/file-roller/archive-extract-advanced-options.page
/usr/share/help/de/file-roller/archive-extract.page
/usr/share/help/de/file-roller/archive-open.page
/usr/share/help/de/file-roller/archive-view.page
/usr/share/help/de/file-roller/figures/file-roller-icon.png
/usr/share/help/de/file-roller/index.page
/usr/share/help/de/file-roller/introduction.page
/usr/share/help/de/file-roller/keyboard-shortcuts.page
/usr/share/help/de/file-roller/legal.xml
/usr/share/help/de/file-roller/password-protection.page
/usr/share/help/de/file-roller/supported-formats.page
/usr/share/help/de/file-roller/test-integrity.page
/usr/share/help/de/file-roller/troubleshooting-archive-open.page
/usr/share/help/de/file-roller/troubleshooting-password.page
/usr/share/help/el/file-roller/archive-create.page
/usr/share/help/el/file-roller/archive-edit.page
/usr/share/help/el/file-roller/archive-extract-advanced-options.page
/usr/share/help/el/file-roller/archive-extract.page
/usr/share/help/el/file-roller/archive-open.page
/usr/share/help/el/file-roller/archive-view.page
/usr/share/help/el/file-roller/figures/file-roller-icon.png
/usr/share/help/el/file-roller/index.page
/usr/share/help/el/file-roller/introduction.page
/usr/share/help/el/file-roller/keyboard-shortcuts.page
/usr/share/help/el/file-roller/legal.xml
/usr/share/help/el/file-roller/password-protection.page
/usr/share/help/el/file-roller/supported-formats.page
/usr/share/help/el/file-roller/test-integrity.page
/usr/share/help/el/file-roller/troubleshooting-archive-open.page
/usr/share/help/el/file-roller/troubleshooting-password.page
/usr/share/help/es/file-roller/archive-create.page
/usr/share/help/es/file-roller/archive-edit.page
/usr/share/help/es/file-roller/archive-extract-advanced-options.page
/usr/share/help/es/file-roller/archive-extract.page
/usr/share/help/es/file-roller/archive-open.page
/usr/share/help/es/file-roller/archive-view.page
/usr/share/help/es/file-roller/figures/file-roller-icon.png
/usr/share/help/es/file-roller/index.page
/usr/share/help/es/file-roller/introduction.page
/usr/share/help/es/file-roller/keyboard-shortcuts.page
/usr/share/help/es/file-roller/legal.xml
/usr/share/help/es/file-roller/password-protection.page
/usr/share/help/es/file-roller/supported-formats.page
/usr/share/help/es/file-roller/test-integrity.page
/usr/share/help/es/file-roller/troubleshooting-archive-open.page
/usr/share/help/es/file-roller/troubleshooting-password.page
/usr/share/help/fi/file-roller/archive-create.page
/usr/share/help/fi/file-roller/archive-edit.page
/usr/share/help/fi/file-roller/archive-extract-advanced-options.page
/usr/share/help/fi/file-roller/archive-extract.page
/usr/share/help/fi/file-roller/archive-open.page
/usr/share/help/fi/file-roller/archive-view.page
/usr/share/help/fi/file-roller/figures/file-roller-icon.png
/usr/share/help/fi/file-roller/index.page
/usr/share/help/fi/file-roller/introduction.page
/usr/share/help/fi/file-roller/keyboard-shortcuts.page
/usr/share/help/fi/file-roller/legal.xml
/usr/share/help/fi/file-roller/password-protection.page
/usr/share/help/fi/file-roller/supported-formats.page
/usr/share/help/fi/file-roller/test-integrity.page
/usr/share/help/fi/file-roller/troubleshooting-archive-open.page
/usr/share/help/fi/file-roller/troubleshooting-password.page
/usr/share/help/fr/file-roller/archive-create.page
/usr/share/help/fr/file-roller/archive-edit.page
/usr/share/help/fr/file-roller/archive-extract-advanced-options.page
/usr/share/help/fr/file-roller/archive-extract.page
/usr/share/help/fr/file-roller/archive-open.page
/usr/share/help/fr/file-roller/archive-view.page
/usr/share/help/fr/file-roller/figures/file-roller-icon.png
/usr/share/help/fr/file-roller/index.page
/usr/share/help/fr/file-roller/introduction.page
/usr/share/help/fr/file-roller/keyboard-shortcuts.page
/usr/share/help/fr/file-roller/legal.xml
/usr/share/help/fr/file-roller/password-protection.page
/usr/share/help/fr/file-roller/supported-formats.page
/usr/share/help/fr/file-roller/test-integrity.page
/usr/share/help/fr/file-roller/troubleshooting-archive-open.page
/usr/share/help/fr/file-roller/troubleshooting-password.page
/usr/share/help/gl/file-roller/archive-create.page
/usr/share/help/gl/file-roller/archive-edit.page
/usr/share/help/gl/file-roller/archive-extract-advanced-options.page
/usr/share/help/gl/file-roller/archive-extract.page
/usr/share/help/gl/file-roller/archive-open.page
/usr/share/help/gl/file-roller/archive-view.page
/usr/share/help/gl/file-roller/figures/file-roller-icon.png
/usr/share/help/gl/file-roller/index.page
/usr/share/help/gl/file-roller/introduction.page
/usr/share/help/gl/file-roller/keyboard-shortcuts.page
/usr/share/help/gl/file-roller/legal.xml
/usr/share/help/gl/file-roller/password-protection.page
/usr/share/help/gl/file-roller/supported-formats.page
/usr/share/help/gl/file-roller/test-integrity.page
/usr/share/help/gl/file-roller/troubleshooting-archive-open.page
/usr/share/help/gl/file-roller/troubleshooting-password.page
/usr/share/help/hu/file-roller/archive-create.page
/usr/share/help/hu/file-roller/archive-edit.page
/usr/share/help/hu/file-roller/archive-extract-advanced-options.page
/usr/share/help/hu/file-roller/archive-extract.page
/usr/share/help/hu/file-roller/archive-open.page
/usr/share/help/hu/file-roller/archive-view.page
/usr/share/help/hu/file-roller/figures/file-roller-icon.png
/usr/share/help/hu/file-roller/index.page
/usr/share/help/hu/file-roller/introduction.page
/usr/share/help/hu/file-roller/keyboard-shortcuts.page
/usr/share/help/hu/file-roller/legal.xml
/usr/share/help/hu/file-roller/password-protection.page
/usr/share/help/hu/file-roller/supported-formats.page
/usr/share/help/hu/file-roller/test-integrity.page
/usr/share/help/hu/file-roller/troubleshooting-archive-open.page
/usr/share/help/hu/file-roller/troubleshooting-password.page
/usr/share/help/id/file-roller/archive-create.page
/usr/share/help/id/file-roller/archive-edit.page
/usr/share/help/id/file-roller/archive-extract-advanced-options.page
/usr/share/help/id/file-roller/archive-extract.page
/usr/share/help/id/file-roller/archive-open.page
/usr/share/help/id/file-roller/archive-view.page
/usr/share/help/id/file-roller/figures/file-roller-icon.png
/usr/share/help/id/file-roller/index.page
/usr/share/help/id/file-roller/introduction.page
/usr/share/help/id/file-roller/keyboard-shortcuts.page
/usr/share/help/id/file-roller/legal.xml
/usr/share/help/id/file-roller/password-protection.page
/usr/share/help/id/file-roller/supported-formats.page
/usr/share/help/id/file-roller/test-integrity.page
/usr/share/help/id/file-roller/troubleshooting-archive-open.page
/usr/share/help/id/file-roller/troubleshooting-password.page
/usr/share/help/ja/file-roller/archive-create.page
/usr/share/help/ja/file-roller/archive-edit.page
/usr/share/help/ja/file-roller/archive-extract-advanced-options.page
/usr/share/help/ja/file-roller/archive-extract.page
/usr/share/help/ja/file-roller/archive-open.page
/usr/share/help/ja/file-roller/archive-view.page
/usr/share/help/ja/file-roller/figures/file-roller-icon.png
/usr/share/help/ja/file-roller/index.page
/usr/share/help/ja/file-roller/introduction.page
/usr/share/help/ja/file-roller/keyboard-shortcuts.page
/usr/share/help/ja/file-roller/legal.xml
/usr/share/help/ja/file-roller/password-protection.page
/usr/share/help/ja/file-roller/supported-formats.page
/usr/share/help/ja/file-roller/test-integrity.page
/usr/share/help/ja/file-roller/troubleshooting-archive-open.page
/usr/share/help/ja/file-roller/troubleshooting-password.page
/usr/share/help/ko/file-roller/archive-create.page
/usr/share/help/ko/file-roller/archive-edit.page
/usr/share/help/ko/file-roller/archive-extract-advanced-options.page
/usr/share/help/ko/file-roller/archive-extract.page
/usr/share/help/ko/file-roller/archive-open.page
/usr/share/help/ko/file-roller/archive-view.page
/usr/share/help/ko/file-roller/figures/file-roller-icon.png
/usr/share/help/ko/file-roller/index.page
/usr/share/help/ko/file-roller/introduction.page
/usr/share/help/ko/file-roller/keyboard-shortcuts.page
/usr/share/help/ko/file-roller/legal.xml
/usr/share/help/ko/file-roller/password-protection.page
/usr/share/help/ko/file-roller/supported-formats.page
/usr/share/help/ko/file-roller/test-integrity.page
/usr/share/help/ko/file-roller/troubleshooting-archive-open.page
/usr/share/help/ko/file-roller/troubleshooting-password.page
/usr/share/help/pl/file-roller/archive-create.page
/usr/share/help/pl/file-roller/archive-edit.page
/usr/share/help/pl/file-roller/archive-extract-advanced-options.page
/usr/share/help/pl/file-roller/archive-extract.page
/usr/share/help/pl/file-roller/archive-open.page
/usr/share/help/pl/file-roller/archive-view.page
/usr/share/help/pl/file-roller/figures/file-roller-icon.png
/usr/share/help/pl/file-roller/index.page
/usr/share/help/pl/file-roller/introduction.page
/usr/share/help/pl/file-roller/keyboard-shortcuts.page
/usr/share/help/pl/file-roller/legal.xml
/usr/share/help/pl/file-roller/password-protection.page
/usr/share/help/pl/file-roller/supported-formats.page
/usr/share/help/pl/file-roller/test-integrity.page
/usr/share/help/pl/file-roller/troubleshooting-archive-open.page
/usr/share/help/pl/file-roller/troubleshooting-password.page
/usr/share/help/pt_BR/file-roller/archive-create.page
/usr/share/help/pt_BR/file-roller/archive-edit.page
/usr/share/help/pt_BR/file-roller/archive-extract-advanced-options.page
/usr/share/help/pt_BR/file-roller/archive-extract.page
/usr/share/help/pt_BR/file-roller/archive-open.page
/usr/share/help/pt_BR/file-roller/archive-view.page
/usr/share/help/pt_BR/file-roller/figures/file-roller-icon.png
/usr/share/help/pt_BR/file-roller/index.page
/usr/share/help/pt_BR/file-roller/introduction.page
/usr/share/help/pt_BR/file-roller/keyboard-shortcuts.page
/usr/share/help/pt_BR/file-roller/legal.xml
/usr/share/help/pt_BR/file-roller/password-protection.page
/usr/share/help/pt_BR/file-roller/supported-formats.page
/usr/share/help/pt_BR/file-roller/test-integrity.page
/usr/share/help/pt_BR/file-roller/troubleshooting-archive-open.page
/usr/share/help/pt_BR/file-roller/troubleshooting-password.page
/usr/share/help/ru/file-roller/archive-create.page
/usr/share/help/ru/file-roller/archive-edit.page
/usr/share/help/ru/file-roller/archive-extract-advanced-options.page
/usr/share/help/ru/file-roller/archive-extract.page
/usr/share/help/ru/file-roller/archive-open.page
/usr/share/help/ru/file-roller/archive-view.page
/usr/share/help/ru/file-roller/figures/file-roller-icon.png
/usr/share/help/ru/file-roller/index.page
/usr/share/help/ru/file-roller/introduction.page
/usr/share/help/ru/file-roller/keyboard-shortcuts.page
/usr/share/help/ru/file-roller/legal.xml
/usr/share/help/ru/file-roller/password-protection.page
/usr/share/help/ru/file-roller/supported-formats.page
/usr/share/help/ru/file-roller/test-integrity.page
/usr/share/help/ru/file-roller/troubleshooting-archive-open.page
/usr/share/help/ru/file-roller/troubleshooting-password.page
/usr/share/help/sl/file-roller/archive-create.page
/usr/share/help/sl/file-roller/archive-edit.page
/usr/share/help/sl/file-roller/archive-extract-advanced-options.page
/usr/share/help/sl/file-roller/archive-extract.page
/usr/share/help/sl/file-roller/archive-open.page
/usr/share/help/sl/file-roller/archive-view.page
/usr/share/help/sl/file-roller/figures/file-roller-icon.png
/usr/share/help/sl/file-roller/index.page
/usr/share/help/sl/file-roller/introduction.page
/usr/share/help/sl/file-roller/keyboard-shortcuts.page
/usr/share/help/sl/file-roller/legal.xml
/usr/share/help/sl/file-roller/password-protection.page
/usr/share/help/sl/file-roller/supported-formats.page
/usr/share/help/sl/file-roller/test-integrity.page
/usr/share/help/sl/file-roller/troubleshooting-archive-open.page
/usr/share/help/sl/file-roller/troubleshooting-password.page
/usr/share/help/sv/file-roller/archive-create.page
/usr/share/help/sv/file-roller/archive-edit.page
/usr/share/help/sv/file-roller/archive-extract-advanced-options.page
/usr/share/help/sv/file-roller/archive-extract.page
/usr/share/help/sv/file-roller/archive-open.page
/usr/share/help/sv/file-roller/archive-view.page
/usr/share/help/sv/file-roller/figures/file-roller-icon.png
/usr/share/help/sv/file-roller/index.page
/usr/share/help/sv/file-roller/introduction.page
/usr/share/help/sv/file-roller/keyboard-shortcuts.page
/usr/share/help/sv/file-roller/legal.xml
/usr/share/help/sv/file-roller/password-protection.page
/usr/share/help/sv/file-roller/supported-formats.page
/usr/share/help/sv/file-roller/test-integrity.page
/usr/share/help/sv/file-roller/troubleshooting-archive-open.page
/usr/share/help/sv/file-roller/troubleshooting-password.page
/usr/share/help/te/file-roller/archive-create.page
/usr/share/help/te/file-roller/archive-edit.page
/usr/share/help/te/file-roller/archive-extract-advanced-options.page
/usr/share/help/te/file-roller/archive-extract.page
/usr/share/help/te/file-roller/archive-open.page
/usr/share/help/te/file-roller/archive-view.page
/usr/share/help/te/file-roller/figures/file-roller-icon.png
/usr/share/help/te/file-roller/index.page
/usr/share/help/te/file-roller/introduction.page
/usr/share/help/te/file-roller/keyboard-shortcuts.page
/usr/share/help/te/file-roller/legal.xml
/usr/share/help/te/file-roller/password-protection.page
/usr/share/help/te/file-roller/supported-formats.page
/usr/share/help/te/file-roller/test-integrity.page
/usr/share/help/te/file-roller/troubleshooting-archive-open.page
/usr/share/help/te/file-roller/troubleshooting-password.page
/usr/share/help/zh_CN/file-roller/archive-create.page
/usr/share/help/zh_CN/file-roller/archive-edit.page
/usr/share/help/zh_CN/file-roller/archive-extract-advanced-options.page
/usr/share/help/zh_CN/file-roller/archive-extract.page
/usr/share/help/zh_CN/file-roller/archive-open.page
/usr/share/help/zh_CN/file-roller/archive-view.page
/usr/share/help/zh_CN/file-roller/figures/file-roller-icon.png
/usr/share/help/zh_CN/file-roller/index.page
/usr/share/help/zh_CN/file-roller/introduction.page
/usr/share/help/zh_CN/file-roller/keyboard-shortcuts.page
/usr/share/help/zh_CN/file-roller/legal.xml
/usr/share/help/zh_CN/file-roller/password-protection.page
/usr/share/help/zh_CN/file-roller/supported-formats.page
/usr/share/help/zh_CN/file-roller/test-integrity.page
/usr/share/help/zh_CN/file-roller/troubleshooting-archive-open.page
/usr/share/help/zh_CN/file-roller/troubleshooting-password.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/nautilus/extensions-3.0/libnautilus-fileroller.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/file-roller/isoinfo.sh
/usr/libexec/file-roller/rpm2cpio

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/file-roller/COPYING

%files locales -f file-roller.lang
%defattr(-,root,root,-)

