# 仅提供启动入口，真正的界面布局见 guiLayout.py

from module.guiLayout import layout

def main():
    lo = layout("phone")
    lo.createWindow()
    lo.run()

if __name__ == '__main__':
    main()