# LemonWeather.spec
block_cipher = None

a = Analysis(
    ['LemonWeather.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('methods.py', '.'),
    ],
    hiddenimports=[
        'PIL',
        'ttkbootstrap',
        'requests',
        'tkinter'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='LemonWeather',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='icons/weather.ico',
    onefile=True
)