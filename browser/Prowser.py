#  _______   _______    ______   __       __   ______   ________  _______  
#|       \ |       \  /      \ |  \  _  |  \ /      \ |        \|       \ 
#| $$$$$$$\| $$$$$$$\|  $$$$$$\| $$ / \ | $$|  $$$$$$\| $$$$$$$$| $$$$$$$\
#| $$__/ $$| $$__| $$| $$  | $$| $$/  $\| $$| $$___\$$| $$__    | $$__| $$
#| $$    $$| $$    $$| $$  | $$| $$  $$$\ $$ \$$    \ | $$  \   | $$    $$
#| $$$$$$$ | $$$$$$$\| $$  | $$| $$ $$\$$\$$ _\$$$$$$\| $$$$$   | $$$$$$$\
#| $$      | $$  | $$| $$__/ $$| $$$$  \$$$$|  \__| $$| $$_____ | $$  | $$
#| $$      | $$  | $$ \$$    $$| $$$    \$$$ \$$    $$| $$     \| $$  | $$
# \$$       \$$   \$$  \$$$$$$  \$$      \$$  \$$$$$$  \$$$$$$$$ \$$   \$$
                                                                         
#                                                                         a simple web browser written in Python
# Prowser Developers (C) 2025-2025
# Python Developers (C) 1991-2025
# PyQt Developers (C) 1998-2025



from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QToolBar, QAction, QLineEdit, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
newtab = """<html>
<head>
  <title>New Tab</title>
</head>
<style>
body {
  background-color: black;
}

center {
    color: white;
}

}
</style>
<body>
<a name="top"></a>
<center id="lite_wrapper">
  <br>
  <center><h2>Prowser</h2></center>
  <br><br>

  <form action="https://lite.duckduckgo.com/lite/" method="post">
    <input class='query' type="text" size="40" name="q" autocomplete="off" value="" autofocus />
    <input class='submit' type="submit" value="Search" />






  </form>

  <br>
</center>

</body>
</html>
"""

# main window
class MainWindow(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.polyfill_js = __import__("urllib.request").request.urlopen("https://cdnjs.cloudflare.com/ajax/libs/core-js/3.45.1/minified.js").read().decode()


        # creating a tab widget
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)

        # creating a status bar
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # creating a tool bar for navigation
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # back button
        back_btn = QAction("←", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        # forward button
        next_btn = QAction("➜", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        # reload button
        reload_btn = QAction("🗘", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        # home button
        home_btn = QAction("𖠿", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # separator
        navtb.addSeparator()

        # URL bar
        self.urlbar = QLineEdit()
        self.urlbar.setPlaceholderText("URL")
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Search bar
        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText("Search DuckDuckGo")
        self.searchbar.returnPressed.connect(self.search)  # connect to the method
        navtb.addWidget(self.searchbar)
    
        # stop button
        stop_btn = QAction("󠁪󠁪️݁  ⃠ ", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)


        # creating first tab
        self.add_new_tab(QUrl(), 'Homepage')  # Open empty page first
        self.tabs.currentWidget().setHtml(newtab)

        # show window
        self.show()
        self.setWindowTitle("Prowser")

    # method for adding new tab
    def add_new_tab(self, qurl = None, label =""):
        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.page().runJavaScript("matchMedia = () => ({ matches: true });")
        browser.page().runJavaScript(self.polyfill_js, 0)
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser = browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                     self.tabs.setTabText(i, browser.page().title()))
        browser.page().profile().setHttpUserAgent("Mozilla/5.0 (Android 11; Mobile; rv:90.0) Gecko/90.0 Firefox/90.0")


    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):
       if i == -1:
           self.add_new_tab()
           self.tabs.currentWidget().setHtml(newtab)
    # Add newtab button

    # when tab is changed
    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    # update window title
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - Prowser" % title)

    # navigate home
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl())
        self.tabs.currentWidget().setHtml(newtab)

    # navigate to URL
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)

    # update URL bar
    def update_urlbar(self, q, browser = None):
        if browser != self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    # SEARCH METHOD (inside the class)
    def search(self):
        query = self.searchbar.text().strip()
        if query:
            url = QUrl(f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}")
            self.tabs.currentWidget().setUrl(url)
            self.searchbar.clear()

# creating a PyQt5 application
app = QApplication(sys.argv)
app.setApplicationName("Prowser")
window = MainWindow()
print("Prowser Started. Prowser Developers (C) 2025-2025")
app.exec_()
print("Prowser Stopped.")
