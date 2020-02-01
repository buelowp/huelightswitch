/*
 * Copyright (c) 2020 Peter Buelow <email>
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */

#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    setStyleSheet("background-color: black;");
    
    m_light1 = new QPushButton("Light1");
    m_light1->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    m_light1->setStyleSheet("QPushButton{background-color: white; border-style: solid; border-color: black; border-width: 2px; border-radius: 10px;}"); 
    connect(m_light1, SIGNAL(released()), this, SLOT(lightOneTouched()));
    m_light2 = new QPushButton("Light2");
    m_light2->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    m_light2->setStyleSheet("QPushButton{background-color: white; border-style: solid; border-color: black; border-width: 2px; border-radius: 10px;}"); 
    connect(m_light2, SIGNAL(released()), this, SLOT(lightTwoTouched()));

    m_bright1 = new QSlider(Qt::Horizontal);
    m_bright2 = new QSlider(Qt::Horizontal);
    m_layout = new QVBoxLayout();
    m_layout->setSpacing(5);
    
    m_layout->addWidget(m_light1);
    m_layout->addWidget(m_bright1);
    m_layout->addWidget(m_light2);
    m_layout->addWidget(m_bright2);
    QWidget *widget = new QWidget();
    widget->setLayout(m_layout);
    setCentralWidget(widget);
}

MainWindow::~MainWindow()
{
}

void MainWindow::styleSlider()
{
    QString styleSheet("\
    QSlider::groove:horizontal { \
        border: 1px solid #bbb; \
        background: white; \
        height: 10px; \
        border-radius: 4px; \
    } \
 \
    QSlider::sub-page:horizontal { \
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1, \
            stop: 0 #66e, stop: 1 #bbf); \
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, \
            stop: 0 #bbf, stop: 1 #55f); \
        border: 1px solid #777; \
        height: 10px; \
        border-radius: 4px; \
    } \
 \
    QSlider::add-page:horizontal { \
        background: #fff; \
        border: 1px solid #777; \
        height: 10px; \
        border-radius: 4px; \
    } \
 \
    QSlider::handle:horizontal { \
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc); \
        border: 1px solid #777; \
        width: 13px; \
        margin-top: -2px; \
        margin-bottom: -2px; \
        border-radius: 4px; \
    } \
 \
    QSlider::handle:horizontal:hover { \
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd); \
        border: 1px solid #444; \
        border-radius: 4px; \
    } \
 \
    QSlider::sub-page:horizontal:disabled { \
        background: #bbb; \
        border-color: #999; \
    } \
 \
    QSlider::add-page:horizontal:disabled { \
        background: #eee; \
        border-color: #999; \
    } \
 \
    QSlider::handle:horizontal:disabled { \
        background: #eee; \
        border: 1px solid #aaa; \
        border-radius: 4px; \
    }");
    
    m_bright1->setStyleSheet(styleSheet);
    m_bright2->setStyleSheet(styleSheet);
}

void MainWindow::showEvent(QShowEvent*)
{
}

void MainWindow::allLightsUpdated()
{
}

void MainWindow::bridgeFound()
{
}

void MainWindow::lightsFound(int)
{
}

void MainWindow::newLightState(int, bool)
{
}

void MainWindow::noLightsTurnedOff()
{
}

void MainWindow::noLightsTurnedOn()
{
}

void MainWindow::updateTurnOffCount()
{
}

void MainWindow::updateTurnOnCount()
{
}

void MainWindow::lightOneTouched()
{
}

void MainWindow::lightTwoTouched()
{
}





