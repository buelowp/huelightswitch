TEMPLATE = app
CONFIG += debug
QT += widgets gui network

LIBS = -lhue
SOURCES += main.cpp mainwindow.cpp huemanager.cpp keystore.cpp
HEADERS += mainwindow.h huemanager.h keystore.h

MOC_DIR = build
OBJECTS_DIR = build
DESTDIR = build
