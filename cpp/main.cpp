#include <QtCore/QtCore>

#include "mainwindow.h"

int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    MainWindow mw;
    
    QCursor cursor(Qt::BlankCursor);
    QApplication::setOverrideCursor(cursor);
    QApplication::changeOverrideCursor(cursor);

    mw.setGeometry(100,100,640,480);
    mw.show();
//    mw.showFullScreen();
    
    return app.exec();
}
