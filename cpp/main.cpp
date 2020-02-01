#include <QtCore/QtCore>

#include "mainwindow.h"

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    MainWindow mw;
    
//    mw.setGeometry(100,100,640,480);
    mw.showFullScreen();
    
    return app.exec();
}
