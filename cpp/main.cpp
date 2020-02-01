#include <QtCore/QtCore>

#include "mainwindow.h"

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    MainWindow mw;
    
    mw.setGeometry(100,100,480,640);
    mw.show();
    
    return app.exec();
}
