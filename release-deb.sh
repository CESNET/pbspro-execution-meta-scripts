#!/bin/bash

dpkg-deb -b debian pbspro-execution-meta-scripts_$(echo $(grep "Version:" debian/DEBIAN/control) | awk '{print $2}')_all.deb
#alien -r pbspro-execution-meta-scripts_$(echo $(grep "Version:" debian/DEBIAN/control) | awk '{print $2}')_all.deb --scripts -k
