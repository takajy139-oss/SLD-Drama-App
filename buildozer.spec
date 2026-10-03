[app]
title = SLD download Drama
package.name = slddownloaddrama
package.domain = com.sld
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.2.1,requests,urllib3,certifi,idna,charset_normalizer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 28c
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
