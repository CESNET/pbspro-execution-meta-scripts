#!/bin/bash

VERSION="1.0"

cp debian pbspro-execution-meta-scripts-$VERSION -R
rm pbspro-execution-meta-scripts-$VERSION/DEBIAN -rf
tar -cvzf pbspro-execution-meta-scripts-${VERSION}.tar.gz pbspro-execution-meta-scripts-$VERSION
rm pbspro-execution-meta-scripts-$VERSION -rf

mkdir -p ~/rpmbuild/SOURCES/
mv pbspro-execution-meta-scripts-${VERSION}.tar.gz ~/rpmbuild/SOURCES/

rpmbuild -ba pbspro-execution-meta-scripts.spec
rpmbuild -bb pbspro-execution-meta-scripts.spec
