# Maintainer: Sahan Rasanjana <sahan.user@gmail.com>
pkgname=('aster-wallpaper')
pkgver=1
pkgrel=1
_destname="/usr"
pkgdesc="Wallpaper Collection for Aster Linux using NASA image api"
arch=("x86_64")
url="https://github.com/asterlinux/aster-wallpaper-template"
license=('GPL')
depends=("git")
source=("${pkgname}.tar.gz")
md5sums=("SKIP")

pkgver() {
  date +%Y%m%d
}

package() {
        install -dm755 ${pkgdir}${_destname}
        cp -r ${srcdir}/${pkgname}${_destname}/* ${pkgdir}${_destname}
}
