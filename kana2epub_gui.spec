# -*- pyinstaller设置文件 -*-
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['kana2epub_gui.py','kana2epub_ui.py','kanasouphtml.py'],
    pathex=['D:\SoftwareFile\VScode\python\kana2epub_gui'],
    binaries=[],
    datas=[("D:\InstallPath\PYTHON\Lib\site-packages\pykakasi\data\*.db","pykakasi\data"),("D:\SoftwareFile\VScode\python\kana2epub_gui\src\wallpaper.png",".\src"),("D:\SoftwareFile\VScode\python\kana2epub_gui\src\open_folder_file_icon_219486.ico",".\src"),("D:\SoftwareFile\VScode\python\kana2epub_gui\src\sound.wav",".\src"),("D:\SoftwareFile\VScode\python\kana2epub_gui\src\sound1.wav",".\src"),],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='kana2epub_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='.\\src\\kana2epub.ico',
)
