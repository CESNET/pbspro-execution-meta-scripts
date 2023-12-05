#!/bin/bash

VERSION="1.0"

cp debian openpbs-execution-meta-scripts-$VERSION -R
rm openpbs-execution-meta-scripts-$VERSION/DEBIAN -rf
tar -cvzf openpbs-execution-meta-scripts-${VERSION}.tar.gz openpbs-execution-meta-scripts-$VERSION
rm openpbs-execution-meta-scripts-$VERSION -rf

mkdir -p ~/rpmbuild/SOURCES/
mv openpbs-execution-meta-scripts-${VERSION}.tar.gz ~/rpmbuild/SOURCES/

rpmbuild -ba openpbs-execution-meta-scripts.spec
rpmbuild -bb openpbs-execution-meta-scripts.spec
