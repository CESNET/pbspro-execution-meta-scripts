#!/bin/bash

fakeroot dpkg-deb -b debian openpbs-execution-meta-scripts_$(echo $(grep "Version:" debian/DEBIAN/control) | awk '{print $2}')_all.deb
#alien -r openpbs-execution-meta-scripts_$(echo $(grep "Version:" debian/DEBIAN/control) | awk '{print $2}')_all.deb --scripts -k
