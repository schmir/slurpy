# Contributor: Randy Morris <randy rsontech net>
pkgname=slurpy-git
pkgver=20090625
pkgrel=1
pkgdesc="An AUR search/download/update helper in Python"
arch=('i686' 'x86_64')
url="http://rsontech.net/projects/"
license=('None')
depends=('python')
conflicts=('slurpy')
provides=('slurpy')
optdepends=('python-cjson: faster processing for large result sets')
makedepends=('git')
source=()
md5sums=()
_gitroot="git://github.com/rson/slurpy.git"
_gitname="slurpy"
build() {
  cd ${srcdir}
  msg "Connecting to github.com GIT server...."

  if [ -d ${srcdir}/$_gitname ] ; then
		cd $_gitname && git pull origin
		msg "The local files are updated."
  else
		git clone $_gitroot
  fi

  msg "GIT checkout done or server timeout"
  msg "Starting make..."
  install -D -m755 ${_gitname}/${_gitname} ${pkgdir}/usr/bin/${_gitname}
}
